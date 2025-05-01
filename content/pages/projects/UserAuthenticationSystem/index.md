---
Title: User Authentication System (Facade Pattern)
Date: 2025-04-30 15:30
Modified: 2025-04-30 15:30
Lang: en
Category: Projects
Tags: design patterns, facade, authentication, python
Slug: projects/UserAuthenticationSystem
Authors: Alin Morosanu
Summary: A user authentication system implementing the Facade design pattern in Python.
---

## Overview

This project demonstrates how to implement a user authentication system using the **Facade design pattern** in Python. The Facade pattern provides a simplified interface to a complex subsystem of classes, making the subsystem easier to use.

In modern web applications, authentication involves several complex operations:
- Password hashing and verification
- Token generation and validation
- Session management
- Permission checking
- Account locking for security
- Two-factor authentication

The Facade pattern helps us hide this complexity behind a clean, simple interface.

## Problem

Without using a design pattern, authentication code often becomes:
- **Tightly coupled** - Authentication logic scattered throughout the codebase
- **Hard to maintain** - Changes to security requirements affect multiple places
- **Difficult to test** - Complex dependencies make unit testing challenging
- **Inconsistent** - Different parts of the app might implement security differently

## Solution: The Facade Pattern

The Facade pattern solves these problems by:
- Providing a **unified interface** to the authentication subsystem
- **Decoupling** client code from authentication implementation details
- Making the system **easier to test** through clear boundaries
- Ensuring **consistent security** throughout the application

## Implementation

### Structure

```
auth_system/
├── __init__.py
├── facade.py            # Main Facade class
├── password_handler.py  # Password hashing and verification
├── token_service.py     # JWT token generation and validation
├── user_store.py        # User data access layer
├── session_manager.py   # Session tracking and management
└── security_service.py  # Security features (account locking, 2FA)
```

### Code Example

```python
# facade.py
from typing import Dict, Optional, Any, Tuple

from .password_handler import PasswordHandler
from .token_service import TokenService
from .user_store import UserStore
from .session_manager import SessionManager
from .security_service import SecurityService


class AuthFacade:
    """
    Facade for the authentication subsystem.
    Provides a simplified interface for client code.
    """
    
    def __init__(self):
        self.password_handler = PasswordHandler()
        self.token_service = TokenService()
        self.user_store = UserStore()
        self.session_manager = SessionManager()
        self.security_service = SecurityService()
        
    def register_user(self, username: str, password: str, email: str) -> Dict[str, Any]:
        """Register a new user"""
        # Check if username already exists
        if self.user_store.get_user_by_username(username):
            return {"success": False, "message": "Username already exists"}
        
        # Hash the password
        password_hash = self.password_handler.hash_password(password)
        
        # Store user in database
        user_id = self.user_store.create_user(username, password_hash, email)
        
        return {"success": True, "user_id": user_id}
    
    def login(self, username: str, password: str, ip_address: str) -> Dict[str, Any]:
        """Authenticate a user and return tokens if successful"""
        # Check for too many failed attempts
        if self.security_service.is_account_locked(username):
            return {"success": False, "message": "Account is temporarily locked"}
        
        # Get user from database
        user = self.user_store.get_user_by_username(username)
        if not user:
            return {"success": False, "message": "Invalid credentials"}
        
        # Verify password
        if not self.password_handler.verify_password(password, user["password_hash"]):
            # Record failed attempt
            self.security_service.record_failed_attempt(username, ip_address)
            return {"success": False, "message": "Invalid credentials"}
        
        # Clear any failed attempts
        self.security_service.clear_failed_attempts(username)
        
        # Create session
        session_id = self.session_manager.create_session(user["id"], ip_address)
        
        # Generate tokens
        access_token = self.token_service.generate_access_token(user["id"])
        refresh_token = self.token_service.generate_refresh_token(user["id"])
        
        return {
            "success": True,
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user": {
                "id": user["id"],
                "username": user["username"],
                "email": user["email"]
            }
        }
        
    def logout(self, user_id: int, session_id: str) -> Dict[str, Any]:
        """End a user session"""
        self.session_manager.end_session(user_id, session_id)
        return {"success": True}
        
    def verify_token(self, token: str) -> Tuple[bool, Optional[Dict[str, Any]]]:
        """Verify an access token and return user data if valid"""
        payload = self.token_service.validate_access_token(token)
        if not payload:
            return False, None
            
        user_id = payload.get("user_id")
        user = self.user_store.get_user_by_id(user_id)
        
        return True, user
        
    def refresh_tokens(self, refresh_token: str) -> Dict[str, Any]:
        """Generate new tokens using a refresh token"""
        payload = self.token_service.validate_refresh_token(refresh_token)
        if not payload:
            return {"success": False, "message": "Invalid refresh token"}
            
        user_id = payload.get("user_id")
        
        # Generate new tokens
        access_token = self.token_service.generate_access_token(user_id)
        new_refresh_token = self.token_service.generate_refresh_token(user_id)
        
        return {
            "success": True,
            "access_token": access_token,
            "refresh_token": new_refresh_token
        }
        
    def change_password(self, user_id: int, old_password: str, new_password: str) -> Dict[str, Any]:
        """Change a user's password"""
        user = self.user_store.get_user_by_id(user_id)
        if not user:
            return {"success": False, "message": "User not found"}
            
        # Verify old password
        if not self.password_handler.verify_password(old_password, user["password_hash"]):
            return {"success": False, "message": "Current password is incorrect"}
            
        # Hash new password
        new_hash = self.password_handler.hash_password(new_password)
        
        # Update in database
        self.user_store.update_password(user_id, new_hash)
        
        # Invalidate all sessions (force re-login with new password)
        self.session_manager.invalidate_all_sessions(user_id)
        
        return {"success": True}
```

### Client Usage Example

```python
# Example usage in a Flask or Django view
from auth_system.facade import AuthFacade

auth = AuthFacade()

def register_view(request):
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    
    # Simple, clean interface for client code
    result = auth.register_user(username, password, email)
    
    if result["success"]:
        return {"message": "Registration successful"}, 201
    else:
        return {"error": result["message"]}, 400

def login_view(request):
    username = request.form.get('username')
    password = request.form.get('password')
    ip_address = request.remote_addr
    
    # Single method call handles all authentication complexity
    result = auth.login(username, password, ip_address)
    
    if result["success"]:
        return result, 200
    else:
        return {"error": result["message"]}, 401
```

## Benefits of the Facade Pattern

1. **Simplifies client code** - Client code doesn't need to know about subsystem complexity
2. **Improves maintainability** - Security implementation changes only affect the facade
3. **Easier testing** - Components can be tested in isolation
4. **Better organization** - Each security concern has its own dedicated component
5. **Flexibility** - Implementation details can change without affecting client code

## When to Use the Facade Pattern

The Facade pattern is particularly useful when:

- You need to provide a simple interface to a complex subsystem
- You want to decouple your subsystem from clients and other subsystems
- You need to layer your subsystems (the facade acts as an entry point)
- You have a system with many interdependent classes that are difficult to understand

## Related Patterns

- **Adapter Pattern**: Unlike Facade, Adapter makes existing interfaces work together
- **Proxy Pattern**: While Facade simplifies, Proxy controls access to an object
- **Mediator Pattern**: Similar to Facade but focuses on colleague objects communicating

--- 

**(End of project series)**

*Previous:* [Order Processing Workflow (State Pattern)](OrderProcessingWorkflow.html)

## Explore other resources
- [Design Pattern on Refactoring Guru](https://refactoring.guru/design-patterns)
- [Python Design Patterns guide](https://python-patterns.guide/)
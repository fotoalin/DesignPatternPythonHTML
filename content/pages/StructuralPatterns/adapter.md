Title: Adapter Pattern
Date: 2025-04-30 17:15
Modified: 2025-04-30
Category: Structural Patterns
Tags: adapter, wrapper, structural pattern, design patterns, python
Slug: structural/adapter
Authors: Alin Morosanu
Summary: Learn about the Adapter pattern, which allows objects with incompatible interfaces to collaborate.

---

## Adapter Pattern (Wrapper)

**Type:** Structural

### Intent

**Convert the interface** of a class into another interface clients expect. Adapter lets classes work together that couldn't otherwise because of **incompatible interfaces**.

It acts as a bridge or translator between two incompatible interfaces.

### Problem

Imagine you have an existing application that works with a specific set of classes or interfaces. Now, you want to integrate a new third-party library or component, but its interface doesn't match what your application expects.

For example:
*   Your application expects data in XML format, but the new library provides JSON.
*   Your application uses methods like `connect()` and `fetch_data()`, but the new component has `initialize()` and `get_records()`.
*   You have a modern class, but need it to work with legacy code that expects an older interface.

Rewriting the existing application or the third-party library is often impractical or impossible. You need a way to make them work together without modifying their core code.

### Solution

The Adapter pattern introduces a new class (the Adapter) that:

1.  **Implements the target interface:** This is the interface your client code expects to work with.
2.  **Wraps the adaptee object:** This is the object with the incompatible interface that you want to use.
3.  **Translates calls:** When the client calls a method on the Adapter (using the target interface), the Adapter translates this call into one or more calls to the wrapped adaptee object (using the adaptee's interface).

There are two main ways to implement the Adapter pattern:

*   **Object Adapter:** The Adapter holds an instance of the Adaptee and delegates calls to it. (Uses composition).
*   **Class Adapter:** The Adapter inherits from both the Target interface (or class) and the Adaptee class. (Uses multiple inheritance - less common in Python than composition).

Object Adapter is generally preferred as it favors composition over inheritance.

### Python Implementation Example (Object Adapter)

Let's say our application works with a `Logger` interface that has a `log(message)` method, but we want to use a third-party `LegacyLogger` that has a `write_entry(entry)` method.

```python
from abc import ABC, abstractmethod

# --- Target Interface (What the client expects) ---
class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

# --- Adaptee (The incompatible class we want to use) ---
class LegacyLogger:
    def write_entry(self, entry: str):
        print(f"LegacyLogger: Writing entry - '{entry}'")

# --- Adapter Class ---
class LoggerAdapter(Logger):
    """Adapts LegacyLogger to the Logger interface using composition."""
    def __init__(self, legacy_logger: LegacyLogger):
        self._legacy_logger = legacy_logger
        print("LoggerAdapter: Initialized with LegacyLogger.")

    def log(self, message: str):
        """Translates the log call to write_entry."""
        print(f"LoggerAdapter: Received log request: '{message}'")
        # Translation logic (could be more complex)
        entry = f"LOG: {message}"
        self._legacy_logger.write_entry(entry)

# --- Client Code ---
def client_code(logger: Logger):
    """The client code works with the Target interface (Logger)."""
    print("\nClient: Sending log messages...")
    logger.log("System startup complete.")
    logger.log("User logged in.")

# Usage
legacy_logger_instance = LegacyLogger()
adapter = LoggerAdapter(legacy_logger_instance)

client_code(adapter)
# Output:
# LoggerAdapter: Initialized with LegacyLogger.
#
# Client: Sending log messages...
# LoggerAdapter: Received log request: 'System startup complete.'
# LegacyLogger: Writing entry - 'LOG: System startup complete.'
# LoggerAdapter: Received log request: 'User logged in.'
# LegacyLogger: Writing entry - 'LOG: User logged in.'

# If we had a modern logger that already implements the interface:
class ModernLogger(Logger):
    def log(self, message: str):
        print(f"ModernLogger: Logging - '{message}'")

modern_logger_instance = ModernLogger()
client_code(modern_logger_instance)
# Output:
#
# Client: Sending log messages...
# ModernLogger: Logging - 'System startup complete.'
# ModernLogger: Logging - 'User logged in.'

```
*Explanation:* The `LoggerAdapter` implements the `Logger` interface expected by the `client_code`. It holds an instance of `LegacyLogger`. When `client_code` calls `adapter.log()`, the adapter translates this into a call to `self._legacy_logger.write_entry()`, making the incompatible `LegacyLogger` usable by the client.

### Pros

*   **Reusability:** Allows existing classes to work together without modification.
*   **Single Responsibility Principle:** Separates the interface conversion logic from the core business logic of both the client and the adaptee.
*   **Open/Closed Principle:** You can introduce new adapters to support new incompatible classes without changing the existing client code (as long as the client works with the target interface).

### Cons

*   **Increased Complexity:** Introduces an extra layer of indirection (the adapter class).
*   **Potential Overhead:** The translation step might introduce minor performance overhead, though usually negligible.

### When to Use

*   When you want to use an existing class, but its interface does not match the one you need.
*   When you want to create a reusable class that cooperates with unrelated or unforeseen classes (classes that don't necessarily have compatible interfaces).
*   (Object adapter) When you need to use several existing subclasses, but it's impractical to adapt their interface by subclassing every one. An object adapter can adapt the interface of its parent class.

---

**Next:** [Decorator Pattern](./decorator.html) 

Title: Singleton Pattern
Date: 2025-04-30 16:00
Modified: 2025-04-30
Category: Creational Patterns
Tags: singleton, creational pattern, design patterns, python
Slug: creational/singleton
Authors: Alin Morosanu
Summary: Learn about the Singleton design pattern, ensuring a class has only one instance and providing a global point of access to it.

---

## Singleton Pattern

**Type:** Creational

### Intent

Ensure a class only has **one instance**, and provide a **global point of access** to it.

### Problem

Sometimes you need to control the instantiation of a class strictly, ensuring that no matter how many times you try to create an object of that class, you always get the *same* object back. This is useful for things like:

*   Managing a shared resource (e.g., a database connection pool, a hardware interface).
*   A global configuration object.
*   Logging services.
*   Caching mechanisms.

If you just let clients create instances freely, you might end up with multiple objects managing the same resource, leading to conflicts, inconsistent state, or inefficient resource use.

### Solution

The Singleton pattern solves this by making the class itself responsible for managing its sole instance. This typically involves:

1.  Making the constructor **private** (or otherwise preventing direct instantiation from outside).
2.  Creating a **static method** (or equivalent) that acts as the constructor. This method checks if an instance already exists. If it does, it returns the existing instance; otherwise, it creates a new instance, stores it, and returns it.

### Python Implementation Examples

Python doesn't have explicit private constructors like Java or C++, but we can achieve the Singleton behavior in several ways.

#### 1. Using a Metaclass

Metaclasses control the creation of classes themselves. We can use one to intercept the class instantiation process.

```python
class SingletonMeta(type):
    """
    A metaclass for creating Singleton classes.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Override the default call behavior. If an instance of this class
        doesn't exist, create it and store it. Otherwise, return the
        existing instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

# Usage
class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self, config):
        # Simulate initializing connection with config
        self.config = config
        print(f"Initializing DB connection with {config}")

    def query(self, sql):
        print(f"Executing query: {sql} using config {self.config}")

# Test it
db1 = DatabaseConnection("prod_db_config")
db2 = DatabaseConnection("test_db_config") # This config will be ignored

print(f"db1 is db2: {db1 is db2}") # Output: True
print(f"db1 config: {db1.config}") # Output: prod_db_config
print(f"db2 config: {db2.config}") # Output: prod_db_config (same instance)
db1.query("SELECT * FROM users")
db2.query("SELECT * FROM orders")
```
*Explanation:* The `SingletonMeta.__call__` method is invoked when you try to create an instance like `DatabaseConnection(...)`. It checks a dictionary `_instances` to see if an instance of `DatabaseConnection` already exists. If not, it calls the original `__call__` (using `super()`) to create the instance and stores it. Subsequent calls return the stored instance.

#### 2. Using a Decorator

Decorators can wrap class definitions to modify their behavior.

```python
def singleton(cls):
    """
    A decorator to turn a class into a Singleton.
    """
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

# Usage
@singleton
class AppSettings:
    def __init__(self, theme):
        self.theme = theme
        print(f"Loading settings with theme: {theme}")

# Test it
settings1 = AppSettings("dark")
settings2 = AppSettings("light") # This theme will be ignored

print(f"settings1 is settings2: {settings1 is settings2}") # Output: True
print(f"settings1 theme: {settings1.theme}") # Output: dark
print(f"settings2 theme: {settings2.theme}") # Output: dark (same instance)
```
*Explanation:* The `singleton` decorator replaces the original class (`AppSettings`) with the `get_instance` function. When you call `AppSettings("dark")`, you're actually calling `get_instance("dark")`. This function maintains a dictionary `instances` and ensures only one instance of the original `AppSettings` class is created and returned.

#### 3. Using `__new__` (Base Class Approach)

You can override the `__new__` method, which is called before `__init__` during object creation.

```python
class SingletonBase:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Optional: Initialize only once if needed
            # cls._instance._initialized = False
        return cls._instance

# Usage
class Logger(SingletonBase):
    def __init__(self, log_file):
        # Be careful: __init__ runs every time you call Logger()
        # Use a flag if initialization should only happen once.
        # if not getattr(self, '_initialized', False):
        self.log_file = log_file
        print(f"Logger configured with file: {log_file}")
            # self._initialized = True

    def log(self, message):
        print(f"Logging to {self.log_file}: {message}")

# Test it
logger1 = Logger("app.log")
logger2 = Logger("error.log") # This file name might be ignored depending on init logic

print(f"logger1 is logger2: {logger1 is logger2}") # Output: True
print(f"logger1 file: {logger1.log_file}") # Output: error.log (because __init__ ran again)
print(f"logger2 file: {logger2.log_file}") # Output: error.log
logger1.log("Application started.")
logger2.log("An error occurred.")
```
*Explanation:* `__new__` controls the object creation process itself. It checks if `_instance` exists for the class. If not, it creates it using `super().__new__(cls)`. It always returns the stored `_instance`. A common pitfall here is that `__init__` is still called *every time* you attempt to instantiate the class (e.g., `Logger(...)`), potentially re-initializing state unless you add guards (like the commented-out `_initialized` flag).

### Pros

*   **Guaranteed Single Instance:** Ensures only one object exists for a class.
*   **Global Access Point:** Provides a well-known point to access the instance.
*   **Lazy Initialization:** The instance is created only when it's first requested (in most implementations).

### Cons

*   **Violates Single Responsibility Principle:** The class is responsible for both its core logic *and* managing its own instantiation lifecycle.
*   **Global State:** Singletons introduce global state, which can make code harder to reason about and test. Dependencies become hidden.
*   **Testing Challenges:** Code that depends on a Singleton can be difficult to test in isolation, as you can't easily replace the Singleton instance with a mock or stub.
*   **Concurrency Issues:** In multi-threaded environments, naive Singleton implementations might create multiple instances if not properly synchronized (though the Python examples shown are generally thread-safe due to the Global Interpreter Lock for simple assignments).

### When to Use (Use Sparingly!)

*   When exactly one instance is logically required (e.g., managing a single hardware resource).
*   For services like logging or configuration where a single, globally accessible point makes sense.

**Consider alternatives first:**

*   **Dependency Injection:** Pass the shared object (which might be created once at the application root) to the classes that need it. This is often more testable and flexible.
*   **Module-level variables:** In Python, modules themselves are singletons. You can often achieve similar results by defining functions and variables at the module level.

---

**Next:** [Factory Pattern](link-to-factory-pattern.html) 

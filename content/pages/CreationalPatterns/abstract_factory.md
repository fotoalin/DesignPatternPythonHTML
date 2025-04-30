Title: Abstract Factory Pattern
Date: 2025-04-30 16:30
Modified: 2025-04-30
Category: Creational Patterns
Tags: abstract factory, creational pattern, design patterns, python
Slug: creational/abstract-factory
Authors: Alin Morosanu
Summary: Learn about the Abstract Factory pattern for creating families of related or dependent objects without specifying their concrete classes.

---

## Abstract Factory Pattern

**Type:** Creational

### Intent

Provide an interface for creating **families of related or dependent objects** without specifying their concrete classes.

Think of it as a "factory of factories."

### Problem

Imagine you're building a UI toolkit that needs to support multiple operating systems (e.g., Windows, macOS, Linux). Each OS has its own style for UI elements like buttons, checkboxes, and windows.

You want your application code to create UI elements without being tightly coupled to the specific OS implementation. For example, when you ask for a button, you should get a `WindowsButton` on Windows and a `MacButton` on macOS, but your core application logic shouldn't need `if os == 'windows': ... elif os == 'macos': ...` checks everywhere.

Furthermore, you need to ensure consistency. You shouldn't accidentally mix a Windows button with a macOS checkbox in the same UI. All elements created for a specific context (like an OS) should belong to the same family.

Using Simple Factory or Factory Method for *each* element type (button factory, checkbox factory) doesn't solve the consistency problem – you could still mix products from different families.

### Solution

The Abstract Factory pattern introduces:

1.  **Abstract Factory Interface:** Declares a set of methods for creating each type of abstract product (e.g., `create_button()`, `create_checkbox()`).
2.  **Concrete Factories:** Implement the Abstract Factory interface. Each concrete factory corresponds to a specific family of products (e.g., `WindowsFactory`, `MacFactory`). It implements the creation methods to return concrete products belonging to that family (e.g., `WindowsFactory.create_button()` returns a `WindowsButton`).
3.  **Abstract Product Interfaces:** Define interfaces for each distinct type of product in the family (e.g., `Button`, `Checkbox`).
4.  **Concrete Products:** Implement the Abstract Product interfaces for each family (e.g., `WindowsButton`, `MacButton`, `WindowsCheckbox`, `MacCheckbox`).

Client code works with the Abstract Factory and Abstract Product interfaces. You choose *one* concrete factory based on the context (e.g., the current OS) and use it to create all related UI elements, ensuring consistency.

### Python Implementation Example

```python
from abc import ABC, abstractmethod

# --- Abstract Product Interfaces ---
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

# --- Concrete Products (Windows Family) ---
class WindowsButton(Button):
    def paint(self):
        print("Painting a Windows-style button.")

class WindowsCheckbox(Checkbox):
    def paint(self):
        print("Painting a Windows-style checkbox.")

# --- Concrete Products (macOS Family) ---
class MacButton(Button):
    def paint(self):
        print("Painting a macOS-style button.")

class MacCheckbox(Checkbox):
    def paint(self):
        print("Painting a macOS-style checkbox.")

# --- Abstract Factory Interface ---
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# --- Concrete Factories ---
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        print("WindowsFactory: Creating WindowsButton.")
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        print("WindowsFactory: Creating WindowsCheckbox.")
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        print("MacFactory: Creating MacButton.")
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        print("MacFactory: Creating MacCheckbox.")
        return MacCheckbox()

# --- Client Code ---
class Application:
    def __init__(self, factory: GUIFactory):
        self._factory = factory
        self._button = None
        self._checkbox = None

    def create_ui(self):
        print("Application: Creating UI elements using the provided factory.")
        self._button = self._factory.create_button()
        self._checkbox = self._factory.create_checkbox()

    def paint_ui(self):
        if self._button and self._checkbox:
            print("Application: Painting UI elements.")
            self._button.paint()
            self._checkbox.paint()
        else:
            print("Application: UI not created yet.")

# --- Configuration and Execution ---
def configure_app(os_type: str) -> Application:
    """Selects the appropriate factory based on OS type."""
    if os_type == "windows":
        factory = WindowsFactory()
    elif os_type == "macos":
        factory = MacFactory()
    else:
        raise ValueError(f"Unsupported OS type: {os_type}")
    return Application(factory)

# Simulate running on Windows
print("--- Running on Windows ---")
app_win = configure_app("windows")
app_win.create_ui()
app_win.paint_ui()
# Output:
# --- Running on Windows ---
# Application: Creating UI elements using the provided factory.
# WindowsFactory: Creating WindowsButton.
# WindowsFactory: Creating WindowsCheckbox.
# Application: Painting UI elements.
# Painting a Windows-style button.
# Painting a Windows-style checkbox.

# Simulate running on macOS
print("\n--- Running on macOS ---")
app_mac = configure_app("macos")
app_mac.create_ui()
app_mac.paint_ui()
# Output:
# --- Running on macOS ---
# Application: Creating UI elements using the provided factory.
# MacFactory: Creating MacButton.
# MacFactory: Creating MacCheckbox.
# Application: Painting UI elements.
# Painting a macOS-style button.
# Painting a macOS-style checkbox.
```
*Explanation:* The `Application` class only knows about the `GUIFactory`, `Button`, and `Checkbox` interfaces. The `configure_app` function selects the concrete factory (`WindowsFactory` or `MacFactory`). The chosen factory is then passed to the `Application`, which uses it to create a consistent family of UI elements (`WindowsButton` and `WindowsCheckbox`, or `MacButton` and `MacCheckbox`).

### Pros

*   **Isolation of Concrete Classes:** The client code works with interfaces, decoupling it from specific product implementations.
*   **Enforces Product Consistency:** Guarantees that products created by a factory belong to the same family.
*   **Easy Exchange of Product Families:** Switching the entire product family is as simple as changing the concrete factory instance used by the client.
*   **Promotes Open/Closed Principle:** Introducing new families of products is done by adding a new concrete factory and concrete product classes, without modifying existing client code (though the configuration part that selects the factory might need updating).

### Cons

*   **Increased Complexity:** Introduces many new interfaces and classes (Abstract Factory, Concrete Factories, Abstract Products, Concrete Products).
*   **Difficult to Add New Product Types:** Adding a new *type* of product (e.g., a `TextField`) requires modifying the Abstract Factory interface and *all* its concrete subclasses, violating the Open/Closed Principle in that dimension.

### When to Use

*   When your system needs to be independent of how its products are created, composed, and represented.
*   When a system needs to be configured with one of multiple families of products.
*   When you want to provide a class library of products, revealing only their interfaces, not their implementations.
*   When a family of related product objects is designed to be used together, and you need to enforce this constraint.

---

**Next:** [Builder Pattern](link-to-builder-pattern.html) *(Link TBD)*

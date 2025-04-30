Title: Decorator Pattern
Date: 2025-04-30 17:30
Modified: 2025-04-30
Category: Structural Patterns
Tags: decorator, wrapper, structural pattern, design patterns, python
Slug: structural/decorator
Authors: Alin Morosanu
Summary: Learn about the Decorator pattern, which allows adding new behaviors to objects dynamically by placing them inside special wrapper objects.

---

## Decorator Pattern (Wrapper)

**Type:** Structural

### Intent

Attach **additional responsibilities** to an object **dynamically**. Decorators provide a flexible alternative to subclassing for extending functionality.

### Problem

Sometimes you want to add behavior or state to individual objects at runtime, rather than affecting the entire class. Subclassing is one way to extend behavior, but it has drawbacks:

*   **Static:** Inheritance is fixed at compile time. You can't easily add or remove responsibilities from an object on the fly.
*   **Class Explosion:** If you need many different combinations of optional behaviors (e.g., adding logging, then compression, then encryption to a data stream), you might end up with a large number of subclasses (`LoggingStream`, `CompressedStream`, `LoggingCompressedStream`, `EncryptedLoggingCompressedStream`, etc.).
*   **Affects All Instances:** Subclassing affects all instances of the subclass. Decorator lets you modify single objects.

### Solution

The Decorator pattern involves creating a set of decorator classes that wrap the original component.

1.  **Component Interface:** Defines the common interface for both the objects being decorated (Wrappees) and the decorators themselves.
2.  **Concrete Component:** The original class whose behavior needs to be extended. It implements the Component interface.
3.  **Base Decorator (Optional but common):** An abstract class that also implements the Component interface. It holds a reference to a wrapped component object and delegates operations to it. This simplifies the creation of concrete decorators.
4.  **Concrete Decorators:** Subclasses of the Base Decorator (or directly implement the Component interface). They add their specific behavior *before* or *after* delegating the call to the wrapped component.

Decorators have the same interface as the objects they wrap, allowing for recursive composition (stacking decorators). The client code typically interacts with the outermost decorator through the common Component interface, unaware of the specific decorators applied.

### Python Implementation Example

Let's create a simple text component and decorate it with features like adding asterisks or exclamation marks around it.

```python
from abc import ABC, abstractmethod

# --- Component Interface ---
class TextComponent(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

# --- Concrete Component ---
class PlainText(TextComponent):
    def __init__(self, text: str):
        self._text = text

    def render(self) -> str:
        return self._text

# --- Base Decorator (Implements Component Interface) ---
class TextDecorator(TextComponent):
    def __init__(self, wrapped_component: TextComponent):
        self._wrapped_component = wrapped_component
        print(f"Wrapping with {self.__class__.__name__}")

    @abstractmethod
    def render(self) -> str:
        # Base decorator usually delegates, but subclasses override
        return self._wrapped_component.render()

# --- Concrete Decorators ---
class AsteriskDecorator(TextDecorator):
    def render(self) -> str:
        original_text = self._wrapped_component.render()
        print(f"AsteriskDecorator: Adding asterisks to '{original_text}'")
        return f"*** {original_text} ***"

class ExclamationDecorator(TextDecorator):
    def render(self) -> str:
        original_text = self._wrapped_component.render()
        print(f"ExclamationDecorator: Adding exclamation marks to '{original_text}'")
        return f"{original_text} !!!"

class UpperCaseDecorator(TextDecorator):
     def render(self) -> str:
        original_text = self._wrapped_component.render()
        print(f"UpperCaseDecorator: Uppercasing '{original_text}'")
        return original_text.upper()

# --- Client Code ---

# Start with a plain text component
plain = PlainText("Hello, World")
print(f"Original: {plain.render()}")

# Decorate it
print("\nApplying decorators...")
decorated1 = AsteriskDecorator(plain)
print(f"Decorated 1: {decorated1.render()}")

# Decorate it further (stacking)
decorated2 = ExclamationDecorator(decorated1)
print(f"\nDecorated 2: {decorated2.render()}")

# Another combination
decorated3 = UpperCaseDecorator(ExclamationDecorator(AsteriskDecorator(plain)))
print(f"\nDecorated 3: {decorated3.render()}")

# Output:
# Original: Hello, World
#
# Applying decorators...
# Wrapping with AsteriskDecorator
# AsteriskDecorator: Adding asterisks to 'Hello, World'
# Decorated 1: *** Hello, World ***
#
# Wrapping with ExclamationDecorator
# AsteriskDecorator: Adding asterisks to 'Hello, World'
# ExclamationDecorator: Adding exclamation marks to '*** Hello, World ***'
# Decorated 2: *** Hello, World *** !!!
#
# Wrapping with AsteriskDecorator
# Wrapping with ExclamationDecorator
# Wrapping with UpperCaseDecorator
# AsteriskDecorator: Adding asterisks to 'Hello, World'
# ExclamationDecorator: Adding exclamation marks to '*** Hello, World ***'
# UpperCaseDecorator: Uppercasing '*** Hello, World *** !!!'
# Decorated 3: *** HELLO, WORLD *** !!!

```
*Explanation:* `PlainText` is the concrete component. `TextDecorator` is the base decorator, holding a reference (`_wrapped_component`) to the component it wraps. `AsteriskDecorator`, `ExclamationDecorator`, and `UpperCaseDecorator` are concrete decorators. They call the `render` method of their wrapped component and then add their own modification. Notice how decorators can be stacked (`decorated3`). The client interacts with the outermost decorator via the `TextComponent` interface.

*Note:* Python's built-in `@decorator` syntax is related but distinct. It's syntactic sugar primarily for modifying functions or methods, often used for concerns like logging, access control, or memoization. The Decorator *design pattern* is a broader concept for adding responsibilities to *objects* dynamically using wrapper classes, as shown above.

### Pros

*   **Flexibility:** Add or remove responsibilities from objects dynamically at runtime.
*   **Avoids Feature-Laden Superclasses:** Functionality is composed via small decorator objects instead of inheriting everything from a complex base class.
*   **Composable:** Decorators can be combined and stacked in various ways.
*   **Single Responsibility Principle:** Each decorator focuses on a single added responsibility.
*   **Open/Closed Principle:** You can introduce new decorators without modifying existing component or decorator classes.

### Cons

*   **Many Small Objects:** Can result in a system with many small, similar-looking decorator objects.
*   **Debugging Complexity:** Tracing behavior through multiple layers of decorators can sometimes be challenging.
*   **Order Dependency:** The order in which decorators are applied can matter.

### When to Use

*   When you want to add responsibilities to individual objects dynamically and transparently (without affecting other objects).
*   When extension by subclassing is impractical due to the number of independent extensions or potential combinations.
*   When a class definition might be hidden or otherwise unavailable for subclassing.

---

**Next:** [Facade Pattern](./facade.html) *(Link TBD)*

Title: Bridge Pattern
Date: 2025-04-30 18:30
Modified: 2025-04-30
Category: Structural Patterns
Tags: bridge, structural pattern, design patterns, python, abstraction
Slug: structural/bridge
Authors: Alin Morosanu
Summary: Learn about the Bridge pattern, which decouples an abstraction from its implementation so that the two can vary independently.

---

## Bridge Pattern

**Type:** Structural

### Intent

Decouple an abstraction from its implementation so that the two can vary independently. The Bridge pattern is used to separate the abstraction (interface) from the implementation, allowing them to evolve independently.

### Problem

Imagine you are building a graphical application that supports multiple platforms (e.g., Windows, macOS, Linux) and multiple shapes (e.g., Circle, Rectangle). You want to:

*   Avoid a combinatorial explosion of classes (e.g., `WindowsCircle`, `MacRectangle`, etc.).
*   Allow adding new platforms or shapes without modifying existing code.

### Solution

The Bridge pattern splits the code into two hierarchies:

1.  **Abstraction:** Represents the high-level interface (e.g., `Shape`).
2.  **Implementation:** Represents the platform-specific implementation (e.g., `PlatformRenderer`).

The abstraction holds a reference to an implementation object and delegates work to it. This decouples the two hierarchies, allowing them to vary independently.

### Python Implementation Example

Let's model a graphical application with shapes and platform renderers.

```python
from abc import ABC, abstractmethod

# --- Implementation Hierarchy ---
class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius: float):
        pass

    @abstractmethod
    def render_rectangle(self, width: float, height: float):
        pass

class WindowsRenderer(Renderer):
    def render_circle(self, radius: float):
        print(f"Windows: Rendering circle with radius {radius}")

    def render_rectangle(self, width: float, height: float):
        print(f"Windows: Rendering rectangle {width}x{height}")

class MacRenderer(Renderer):
    def render_circle(self, radius: float):
        print(f"Mac: Rendering circle with radius {radius}")

    def render_rectangle(self, width: float, height: float):
        print(f"Mac: Rendering rectangle {width}x{height}")

# --- Abstraction Hierarchy ---
class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self._renderer = renderer

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: float):
        super().__init__(renderer)
        self._radius = radius

    def draw(self):
        self._renderer.render_circle(self._radius)

class Rectangle(Shape):
    def __init__(self, renderer: Renderer, width: float, height: float):
        super().__init__(renderer)
        self._width = width
        self._height = height

    def draw(self):
        self._renderer.render_rectangle(self._width, self._height)

# --- Client Code ---

# Create platform renderers
windows_renderer = WindowsRenderer()
mac_renderer = MacRenderer()

# Create shapes with different renderers
circle = Circle(windows_renderer, 5)
rectangle = Rectangle(mac_renderer, 10, 20)

# Draw shapes
circle.draw()
rectangle.draw()

# Output:
# Windows: Rendering circle with radius 5
# Mac: Rendering rectangle 10x20

```
*Explanation:* The `Renderer` interface defines platform-specific rendering methods. `WindowsRenderer` and `MacRenderer` implement these methods for their respective platforms. The `Shape` abstraction defines the high-level interface for shapes. `Circle` and `Rectangle` are concrete shapes that delegate rendering to the `Renderer` object. This decouples the shape hierarchy from the platform hierarchy.

### Pros

*   **Decouples Abstraction and Implementation:** Allows them to evolve independently.
*   **Reduces Class Explosion:** Avoids combinatorial explosion of classes.
*   **Improves Flexibility:** Makes it easy to add new abstractions or implementations.

### Cons

*   **Increases Complexity:** Adds indirection and complexity to the codebase.

### When to Use

*   When you want to decouple an abstraction from its implementation.
*   When you want to avoid a combinatorial explosion of classes.
*   When you want to improve flexibility and extensibility.

---

**Next:** [Flyweight Pattern](./flyweight.html) 

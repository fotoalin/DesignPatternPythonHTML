Title: Prototype Pattern
Date: 2025-04-30 17:00
Modified: 2025-04-30
Category: Creational Patterns
Tags: prototype, creational pattern, design patterns, python, cloning, copy
Slug: creational/prototype
Authors: Alin Morosanu
Summary: Learn about the Prototype pattern to create new objects by copying an existing object, known as the prototype.

---

## Prototype Pattern

**Type:** Creational

### Intent

Specify the kinds of objects to create using a **prototypical instance**, and create new objects by **copying** this prototype.

### Problem

Sometimes, creating an object directly using its constructor is inefficient or complex. This can happen when:

*   Object initialization is costly (e.g., involves database queries, network calls, heavy computation).
*   You have many similar objects that only differ slightly in their state.
*   You want to decouple the client from the concrete classes being instantiated, similar to Factory patterns, but the focus is on copying an existing instance.
*   The classes to instantiate are specified at runtime.

Instead of rebuilding an object from scratch every time, it might be more efficient to take an existing, fully initialized object (the prototype) and make a copy of it, modifying the copy as needed.

### Solution

The Prototype pattern relies on cloning. An object that supports cloning is designated as a prototype. This object can then be copied to produce new objects.

1.  **Prototype Interface/Abstract Class:** Declares a cloning method (e.g., `clone()`).
2.  **Concrete Prototypes:** Implement the cloning method. The complexity lies in creating a correct copy (shallow vs. deep).
3.  **Client:** Creates a new object by asking a prototype to clone itself.

In Python, cloning is often achieved using the `copy` module, specifically `copy.copy()` (shallow copy) and `copy.deepcopy()` (deep copy).

*   **Shallow Copy:** Creates a new object, but inserts references into it to the objects found in the original. Changes to nested objects will affect both the original and the copy.
*   **Deep Copy:** Creates a new object and recursively copies all objects found in the original. Changes to nested objects in the copy do *not* affect the original.

Often, deep copy is required for the Prototype pattern to ensure the new object is truly independent.

### Python Implementation Example

Let's model different shapes that can be cloned.

```python
import copy
from abc import ABC, abstractmethod

# --- Prototype Interface (Implicit via clone method) ---
class Shape(ABC):
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def clone(self): # The prototype method
        pass

    def __str__(self):
        return f"{self.__class__.__name__} at ({self.x}, {self.y}) with color {self.color}"

# --- Concrete Prototypes ---
class Rectangle(Shape):
    def __init__(self, x: int, y: int, color: str, width: int, height: int):
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def clone(self): # Using deepcopy for independence
        print(f"Cloning Rectangle (using deepcopy)...")
        return copy.deepcopy(self)

    def __str__(self):
        return f"{super().__str__()} [Width: {self.width}, Height: {self.height}]"

class Circle(Shape):
    def __init__(self, x: int, y: int, color: str, radius: int):
        super().__init__(x, y, color)
        self.radius = radius

    def clone(self): # Using deepcopy for independence
        print(f"Cloning Circle (using deepcopy)...")
        return copy.deepcopy(self)

    def __str__(self):
        return f"{super().__str__()} [Radius: {self.radius}]"

# --- Prototype Registry (Optional but common) ---
class ShapeRegistry:
    def __init__(self):
        self._shapes = {}

    def add_shape(self, name: str, shape: Shape):
        print(f"Registry: Adding prototype '{name}'")
        self._shapes[name] = shape

    def get_shape(self, name: str) -> Shape:
        print(f"Registry: Retrieving prototype '{name}'")
        prototype = self._shapes.get(name)
        if prototype:
            return prototype.clone()
        else:
            raise ValueError(f"Shape '{name}' not found in registry.")

# --- Client Code ---

# Create initial prototypes
prototype_rectangle = Rectangle(10, 20, "blue", 100, 50)
prototype_circle = Circle(30, 40, "red", 25)

# Populate registry
registry = ShapeRegistry()
registry.add_shape("BigBlueRectangle", prototype_rectangle)
registry.add_shape("SmallRedCircle", prototype_circle)

# Client clones shapes from the registry
print("\nClient: Requesting shapes from registry...")
shape1 = registry.get_shape("BigBlueRectangle")
shape2 = registry.get_shape("SmallRedCircle")
shape3 = registry.get_shape("BigBlueRectangle")

print("\nCreated Shapes:")
print(f"Shape 1: {shape1}")
print(f"Shape 2: {shape2}")
print(f"Shape 3: {shape3}")

# Verify independence
print(f"\nIs shape1 the same object as prototype_rectangle? {shape1 is prototype_rectangle}") # False
print(f"Is shape1 the same object as shape3? {shape1 is shape3}") # False

# Modify a clone
shape1.color = "green"
shape1.x = 100
print(f"\nModified Shape 1: {shape1}")
print(f"Original Prototype: {prototype_rectangle}") # Unchanged
print(f"Shape 3 (clone): {shape3}") # Unchanged

```
*Explanation:* We define `Shape` prototypes (`Rectangle`, `Circle`) with a `clone` method that uses `copy.deepcopy()`. An optional `ShapeRegistry` stores these prototypes. The client asks the registry for a shape by name; the registry finds the prototype and calls its `clone` method, returning a new, independent copy to the client.

### Pros

*   **Reduced Subclassing:** You can produce new objects without creating a parallel hierarchy of factory classes.
*   **Performance:** Cloning can be more efficient than creating complex objects from scratch, especially if initialization is expensive.
*   **Dynamic Configuration:** New objects can be added and removed at runtime by registering/unregistering prototypes.
*   **Simpler Creation:** Hides the complexity of object creation from the client.

### Cons

*   **Cloning Complexity:** Implementing `clone` correctly can be difficult, especially when dealing with complex objects containing circular references or non-clonable resources (like network sockets or file handles). Deep copy can be resource-intensive.
*   **Hidden Initialization:** The cloned object might need some state reset or re-initialized, which isn't always obvious.

### When to Use

*   When the classes to instantiate are specified at runtime (e.g., by dynamic loading).
*   When you want to avoid building a class hierarchy of factories that parallels the product class hierarchy.
*   When instances of a class can have one of only a few different combinations of state. It may be more convenient to install a corresponding number of prototypes and clone them rather than instantiating the class manually each time.
*   When object creation is significantly more expensive than cloning.

---

**Next:** [Adapter Pattern](../StructuralPatterns/adapter.html) *(Link TBD)*

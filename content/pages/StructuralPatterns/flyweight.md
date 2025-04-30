Title: Flyweight Pattern
Date: 2025-04-30 18:45
Modified: 2025-04-30
Category: Structural Patterns
Tags: flyweight, structural pattern, design patterns, python, memory optimization
Slug: structural/flyweight
Authors: Alin Morosanu
Summary: Learn about the Flyweight pattern, which reduces memory usage by sharing common parts of object state among multiple objects.

---

## Flyweight Pattern

**Type:** Structural

### Intent

Reduce memory usage by sharing common parts of object state among multiple objects. The Flyweight pattern is used to minimize memory usage and improve performance when working with a large number of similar objects.

### Problem

Imagine you are building a text editor that needs to display millions of characters on the screen. Each character has:

*   **Intrinsic State:** Shared state (e.g., font, size, color).
*   **Extrinsic State:** Unique state (e.g., position on the screen).

Creating a separate object for each character would consume a lot of memory. Instead, you can share the intrinsic state among characters and store only the extrinsic state separately.

### Solution

The Flyweight pattern splits the state of an object into:

1.  **Intrinsic State:** Shared state that is stored in a shared object (the flyweight).
2.  **Extrinsic State:** Unique state that is stored outside the flyweight and passed to it when needed.

### Python Implementation Example

Let's model a text editor that uses the Flyweight pattern to optimize memory usage for characters.

```python
class Character:
    def __init__(self, char: str, font: str):
        self.char = char
        self.font = font

    def display(self, position: tuple):
        print(f"Character: {self.char}, Font: {self.font}, Position: {position}")

class CharacterFactory:
    _characters = {}

    @classmethod
    def get_character(cls, char: str, font: str):
        key = (char, font)
        if key not in cls._characters:
            cls._characters[key] = Character(char, font)
        return cls._characters[key]

# --- Client Code ---

# Create a factory
factory = CharacterFactory()

# Create characters using the factory
char_a = factory.get_character("A", "Arial")
char_b = factory.get_character("B", "Arial")
char_a2 = factory.get_character("A", "Arial")

# Display characters with extrinsic state (position)
char_a.display((10, 20))
char_b.display((30, 40))
char_a2.display((50, 60))

# Output:
# Character: A, Font: Arial, Position: (10, 20)
# Character: B, Font: Arial, Position: (30, 40)
# Character: A, Font: Arial, Position: (50, 60)

# Verify that char_a and char_a2 are the same object
print(char_a is char_a2)  # True
```
*Explanation:* The `Character` class represents a character with intrinsic state (char and font). The `CharacterFactory` class ensures that only one instance of each unique character/font combination is created. The client code uses the factory to create characters and provides extrinsic state (position) when displaying them.

### Pros

*   **Reduces Memory Usage:** Shares common parts of object state among multiple objects.
*   **Improves Performance:** Reduces the overhead of creating and managing a large number of objects.

### Cons

*   **Complexity:** Adds complexity to the codebase by introducing shared state and a factory.
*   **Thread Safety:** Requires careful handling of shared state in multithreaded environments.

### When to Use

*   When you need to work with a large number of similar objects.
*   When the objects can share common parts of their state.
*   When memory usage is a concern.

---

**Next:** [Decorator Pattern](./decorator.html) 

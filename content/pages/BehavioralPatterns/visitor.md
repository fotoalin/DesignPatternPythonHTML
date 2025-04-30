Title: Visitor Pattern
Date: 2025-04-30 19:40
Modified: 2025-04-30
Category: Behavioral Patterns
Tags: visitor, behavioral pattern, design patterns, python
Slug: behavioral/visitor
Authors: Alin Morosanu
Summary: Learn about the Visitor pattern, which represents an operation to be performed on elements of an object structure without changing their classes.

---

## Visitor Pattern

**Type:** Behavioral

### Intent

Represent an operation to be performed on the elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates.

### Problem

You want to perform operations on objects of different classes in a class hierarchy without polluting their classes with unrelated behavior.

### Solution

Define a Visitor interface with a visit() operation for each concrete element. Each element class implements an accept(visitor) method that calls visitor.visitElement(this).

### Python Implementation Example

```python
from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_element_a(self, element):
        pass

    @abstractmethod
    def visit_element_b(self, element):
        pass

class ConcreteVisitor(Visitor):
    def visit_element_a(self, element):
        print(f"Visited ElementA: {element.value}")

    def visit_element_b(self, element):
        print(f"Visited ElementB: {element.value}")

class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ElementA(Element):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        visitor.visit_element_a(self)

class ElementB(Element):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        visitor.visit_element_b(self)

# Client code
elements = [ElementA(1), ElementB(2)]
visitor = ConcreteVisitor()
for elem in elements:
    elem.accept(visitor)
```

### Pros

* Adds operations without modifying element classes
* Simplifies adding new operations

### Cons

* Adding new element classes requires updating Visitor interface

### When to Use

* When you need many unrelated operations on objects in a structure
* When object structure is stable but operations change frequently

---

**Next:** [Iterator Pattern](./iterator.html) 
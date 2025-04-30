Title: Template Method Pattern
Date: 2025-04-30 19:20
Modified: 2025-04-30
Category: Behavioral Patterns
Tags: template method, behavioral pattern, design patterns, python
Slug: behavioral/template_method
Authors: Alin Morosanu
Summary: Learn about the Template Method pattern, which defines the skeleton of an algorithm in a method, deferring some steps to subclasses.

---

## Template Method Pattern

**Type:** Behavioral

### Intent

Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps without changing the algorithm's structure.

### Problem

You have an algorithm with fixed steps and some of these steps need to vary across subclasses.

### Solution

Implement a base class with a template method that calls abstract or hook methods. Subclasses override these methods for the variable steps.

### Python Implementation Example

```python
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self):
        self.step_one()
        self.step_two()
        self.hook()

    @abstractmethod
    def step_one(self):
        pass

    @abstractmethod
    def step_two(self):
        pass

    def hook(self):
        # optional override
        pass

class ConcreteClass(AbstractClass):
    def step_one(self):
        print("Concrete step one")

    def step_two(self):
        print("Concrete step two")
```

### Pros

* Promotes code reuse in the invariant parts of an algorithm
* Enforces consistent algorithm structure

### Cons

* Can limit subclass flexibility

### When to Use

* When you have clear invariant and variant parts in an algorithm
* When you want to avoid code duplication across subclasses

---

**Next:** [Chain of Responsibility Pattern](./chain_of_responsibility.html) 
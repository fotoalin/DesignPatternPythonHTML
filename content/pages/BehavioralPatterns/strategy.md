Title: Strategy Pattern
Date: 2025-04-30 19:05
Modified: 2025-04-30
Category: Behavioral Patterns
Tags: strategy, behavioral pattern, design patterns, python
Slug: behavioral/strategy
Authors: Alin Morosanu
Summary: Learn about the Strategy pattern, which defines a family of algorithms, encapsulates each one, and makes them interchangeable.

---

## Strategy Pattern

**Type:** Behavioral

### Intent

Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

### Problem

You need to implement multiple algorithms for the same task and want to switch between them at runtime without cluttering client code.

### Solution

Define a Strategy interface and implement concrete strategies for each algorithm. The Context holds a reference to a Strategy and delegates executing the algorithm.

### Python Implementation Example

```python
# Example implementation of Strategy pattern
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, data):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self, data):
        pass
```

### Pros

* Simplifies swapping algorithms
* Adheres to open/closed principle

### Cons

* Increases number of classes

### When to Use

* When you have multiple related algorithms
* When you want to switch algorithms at runtime

---

**Next:** [Command Pattern](./command.html) 
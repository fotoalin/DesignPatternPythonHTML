Title: Observer Pattern
Date: 2025-04-30 19:00
Modified: 2025-04-30
Category: Behavioral Patterns
Tags: observer, behavioral pattern, design patterns, python
Slug: behavioral/observer
Authors: Alin Morosanu
Summary: Learn about the Observer pattern, which defines a one-to-many dependency between objects so that when one object changes state, all dependents are notified.

---

## Observer Pattern

**Type:** Behavioral

### Intent

Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

### Problem

You have objects (observers) that need to be notified when another object (subject) changes state, and you want to decouple them.

### Solution

The Subject maintains a list of observers and notifies them on state changes. Observers implement an update() method and register/unregister with the Subject.

### Python Implementation Example

```python
# Example implementation of Observer pattern
from abc import ABC, abstractmethod

class Subject:
    # ...subject code...
    pass

class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass
```

### Pros

* Promotes loose coupling
* Supports dynamic subscription

### Cons

* Can lead to memory leaks if observers are not properly detached
* Notification overhead

### When to Use

* When an object's change needs to be propagated to other objects
* When a clean separation between subject and observers is desired

---

**Next:** [Strategy Pattern](./strategy.html) 
Title: Memento Pattern
Date: 2025-04-30 19:35
Modified: 2025-04-30
Category: Behavioral Patterns
Tags: memento, behavioral pattern, design patterns, python
Slug: behavioral/memento
Authors: Alin Morosanu
Summary: Learn about the Memento pattern, which captures and externalizes an object's internal state so it can be restored later.

---

## Memento Pattern

**Type:** Behavioral

### Intent

Capture and externalize an object's internal state without violating encapsulation, so the object can be restored to this state later.

### Problem

You need to implement undo/rollback functionality but want to avoid exposing the internal details of the object.

### Solution

Define a Memento class to hold the state. The Originator creates a Memento with its current state and can restore its state from a Memento. The Caretaker keeps track of Mementos.

### Python Implementation Example

```python
class Memento:
    def __init__(self, state):
        self._state = state

    @property
    def state(self):
        return self._state

class Originator:
    def __init__(self, state):
        self._state = state

    def save(self):
        return Memento(self._state)

    def restore(self, memento: Memento):
        self._state = memento.state

class Caretaker:
    def __init__(self):
        self._history = []

    def backup(self, originator: Originator):
        self._history.append(originator.save())

    def undo(self, originator: Originator):
        if self._history:
            m = self._history.pop()
            originator.restore(m)
```

### Pros

* Restores state without violating encapsulation
* Supports rollback

### Cons

* Can consume memory if state is large

### When to Use

* When you need undo/redo functionality
* When you want to snapshot and restore object state

---

**Next:** [Visitor Pattern](./visitor.html) 
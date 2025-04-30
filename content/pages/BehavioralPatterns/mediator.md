Title: Mediator Pattern
Date: 2025-04-30 19:30
Modified: 2025-04-30
Category: Behavioral Patterns
Tags: mediator, behavioral pattern, design patterns, python
Slug: behavioral/mediator
Authors: Alin Morosanu
Summary: Learn about the Mediator pattern, which defines an object that encapsulates how a set of objects interact.

---

## Mediator Pattern

**Type:** Behavioral

### Intent

Define an object that encapsulates how a set of objects interact, promoting loose coupling by preventing objects from referring to each other explicitly.

### Problem

A set of objects communicate in complex ways, leading to tangled dependencies and making the system hard to maintain.

### Solution

Introduce a Mediator object that handles communication between colleague objects. Colleagues send requests to the Mediator, which coordinates and forwards requests.

### Python Implementation Example

```python
from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass

class ConcreteMediator(Mediator):
    def __init__(self, comp_a, comp_b):
        self._comp_a = comp_a
        self._comp_a.mediator = self
        self._comp_b = comp_b
        self._comp_b.mediator = self

    def notify(self, sender, event):
        if event == 'A':
            print("Mediator reacts to A and triggers B")
            self._comp_b.action_b()

class BaseComponent:
    def __init__(self):
        self.mediator = None

class ComponentA(BaseComponent):
    def action_a(self):
        print("Component A does A.")
        self.mediator.notify(self, 'A')

class ComponentB(BaseComponent):
    def action_b(self):
        print("Component B does B.")

# Client setup
comp_a = ComponentA()
comp_b = ComponentB()
mediator = ConcreteMediator(comp_a, comp_b)
comp_a.action_a()
``` 

### Pros

* Promotes loose coupling
* Localizes control logic in a single place

### Cons

* Can become a monolithic class

### When to Use

* When object communication is complex
* When you want to centralize control of interactions

---

**Next:** [Memento Pattern](./memento.html) *(Link TBD)*
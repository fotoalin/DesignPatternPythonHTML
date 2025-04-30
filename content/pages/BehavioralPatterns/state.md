Title: State Pattern
Date: 2025-04-30 19:15
Modified: 2025-04-30
Category: Behavioral Patterns
Tags: state, behavioral pattern, design patterns, python
Slug: behavioral/state
Authors: Alin Morosanu
Summary: Learn about the State pattern, which allows an object to alter its behavior when its internal state changes.

---

## State Pattern

**Type:** Behavioral

### Intent

Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.

### Problem

Often an object's behavior depends on its state, leading to large conditional statements or scattered state logic.

### Solution

Define state-specific classes implementing a common State interface. The Context holds a reference to its current state and delegates requests to it.

### Python Implementation Example

```python
from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass

class ConcreteStateA(State):
    def handle(self, context):
        # handle state A
        print("Handling State A")
        context.state = ConcreteStateB()

class ConcreteStateB(State):
    def handle(self, context):
        # handle state B
        print("Handling State B")
        context.state = ConcreteStateA()

class Context:
    def __init__(self, state: State):
        self.state = state

    def request(self):
        self.state.handle(self)
```

### Pros

* Simplifies state-specific behavior
* Eliminates complex conditionals

### Cons

* Increases number of classes

### When to Use

* When an object's behavior depends on its state
* When you want to organize state transitions cleanly

---

**Next:** [Template Method Pattern](./template_method.html) *(Link TBD)*
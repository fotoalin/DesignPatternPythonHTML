Title: Command Pattern
Date: 2025-04-30 19:10
Modified: 2025-04-30
Category: Behavioral Patterns
Tags: command, behavioral pattern, design patterns, python
Slug: behavioral/command
Authors: Alin Morosanu
Summary: Learn about the Command pattern, which encapsulates a request as an object to parameterize clients with different requests and support undo operations.

---

## Command Pattern

**Type:** Behavioral

### Intent

Encapsulate a request as an object, thereby allowing you to parameterize clients with different requests, queue or log requests, and support undoable operations.

### Problem

You want to decouple the object that invokes the operation from the one that knows how to perform it, and support features like undo.

### Solution

Define a Command interface with an execute() method. Create concrete command classes that implement this interface and call the corresponding action on a Receiver. The Invoker holds commands and triggers them.

### Python Implementation Example

```python
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Receiver:
    def action(self):
        print("Receiver: Action performed")

class ConcreteCommand(Command):
    def __init__(self, receiver: Receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.action()

class Invoker:
    def __init__(self):
        self._history = []

    def store_and_execute(self, cmd: Command):
        self._history.append(cmd)
        cmd.execute()
```

### Pros

* Decouples sender and receiver
* Supports undo/redo and queuing

### Cons

* Can result in many command classes

### When to Use

* When you need to parameterize objects with operations
* When you want to support undo/redo and logging

---

**Next:** [State Pattern](./state.html) *(Link TBD)*
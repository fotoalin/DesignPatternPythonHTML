Title: Chain of Responsibility Pattern
Date: 2025-04-30 19:25
Modified: 2025-04-30
Category: Behavioral Patterns
Tags: chain of responsibility, behavioral pattern, design patterns, python
Slug: behavioral/chain_of_responsibility
Authors: Alin Morosanu
Summary: Learn about the Chain of Responsibility pattern, which passes a request along a chain of handlers until one handles it.

---

## Chain of Responsibility Pattern

**Type:** Behavioral

### Intent

Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along until an object handles it.

### Problem

You have multiple handlers that can process a request, but you don't know which one should handle it, and you want to decouple sender and receiver.

### Solution

Define a Handler interface with a method to handle requests and an optional link to the next handler. Concrete handlers either process the request or pass it to the next handler in the chain.

### Python Implementation Example

```python
from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def handle(self, request):
        pass

class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == 'A':
            print("Handled by A")
        elif self._successor:
            self._successor.handle(request)

class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == 'B':
            print("Handled by B")
        elif self._successor:
            self._successor.handle(request)

# Client setup
handler_chain = ConcreteHandlerA(ConcreteHandlerB())
for req in ['A', 'B', 'C']:
    handler_chain.handle(req)
``` 

### Pros

* Promotes loose coupling
* Simplifies object interconnections

### Cons

* Requests may go unhandled
* Hard to debug chain of handlers

### When to Use

* When multiple objects can handle a request
* When you want to issue a request to a dynamic set of handlers

---

**Next:** [Mediator Pattern](./mediator.html) *(Link TBD)*
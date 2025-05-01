Title: Order Processing Workflow
Date: 2025-04-30 20:40
Modified: 2025-04-30
Category: Projects
Tags: order processing, workflow, django, python, chain of responsibility, state, template method
Slug: projects/OrderProcessingWorkflow
Authors: Alin Morosanu
Summary: Build a multi-step order processing pipeline in Django, using Template Method, Chain of Responsibility, and State patterns.

---

**Goal:** Implement a scalable order processing pipeline in Django that handles validation, payment, inventory, and shipping in distinct steps with clear extensibility.

## 📚 Patterns Used

- **Template Method Pattern:** Define the skeleton of the order workflow, delegating steps to subclasses or handlers.
- **Chain of Responsibility Pattern:** Pass the order through a chain of handlers (e.g., validation, payment, inventory, shipping) until all steps are completed.
- **State Pattern:** Manage order statuses (Pending, Paid, Shipped) and transition behavior.
- **Strategy Pattern:** Switch between different processing algorithms for each step (e.g., various validation or shipping strategies) at runtime.

## 🔧 Setup

1. Create a Django app: `python manage.py startapp orders`
2. Add `orders` to `INSTALLED_APPS`.
3. Define order models and status field.

## 🛠️ Implementation Steps

1. **Define Workflow Base** (`orders/workflow.py`):
```python
from abc import ABC, abstractmethod

class OrderWorkflow(ABC):
    def process(self, order):
        self.validate(order)
        self.process_payment(order)
        self.check_inventory(order)
        self.ship_order(order)

    @abstractmethod
    def validate(self, order): pass
    @abstractmethod
    def process_payment(self, order): pass
    @abstractmethod
    def check_inventory(self, order): pass
    @abstractmethod
    def ship_order(self, order): pass
```

2. **Chain Handlers** (`orders/handlers.py`):
```python
class Handler:
    def __init__(self, successor=None):
        self._successor = successor
    def handle(self, order):
        if self._successor:
            self._successor.handle(order)

class ValidationHandler(Handler):
    def handle(self, order):
        # validate order data
        super().handle(order)
# ... PaymentHandler, InventoryHandler, ShippingHandler
```

3. **Order States** (`orders/state.py`):
```python
class State(ABC):
    @abstractmethod
    def next(self, context): pass

class Pending(State):
    def next(self, context): context.state = Paid()
# ... Paid, Shipped states
```

4. **Putting It Together** (`orders/services.py`):
```python
# Using Template Method:
class BasicOrderWorkflow(OrderWorkflow):
    def validate(self, order): ...
    def process_payment(self, order): ...
    def check_inventory(self, order): ...
    def ship_order(self, order): ...

# Or using Handlers:
handler_chain = ValidationHandler(PaymentHandler(InventoryHandler(ShippingHandler())))
handler_chain.handle(order)

# State transitions:
order.state = Pending()
order.state.next(order)
```

## 📁 Recommended File Structure

```
orders/
├── __init__.py
├── models.py        # Order model with status field
├── workflow.py      # Template Method classes
├── handlers.py      # Chain of Responsibility handlers
├── state.py         # Order state classes
└── services.py      # Entry points for processing
```

## ✅ Testing

- Write unit tests for each workflow step and state transition.
- Test handler chain order and failure handling.
- Simulate full workflow in integration tests.

---

*Previous:* [Background Task Queue](BackgroundTaskQueue.html)

*Next:* [User Authentication System Project](UserAuthenticationSystem.html)

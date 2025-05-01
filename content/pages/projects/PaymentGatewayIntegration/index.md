Title: Payment Gateway Integration
Date: 2025-04-30 20:00
Modified: 2025-04-30
Category: Projects
Tags: payment gateway, factory pattern, strategy pattern, django, python
Slug: projects/PaymentGatewayIntegration
Authors: Alin Morosanu
Summary: Build a payment system supporting multiple providers (Stripe, PayPal) using Factory and Strategy patterns in Django.

---

**Goal:** Create a Django-based system capable of processing payments through different providers (e.g., Stripe, PayPal) with a clean, extensible architecture.

## 📚 Patterns Used

- **Factory Pattern:** Instantiate the correct payment provider client based on configuration.
- **Strategy Pattern:** Encapsulate payment algorithms for each provider and switch between them at runtime.

## 🔧 Setup

1. Create a Django app, e.g.: `python manage.py startapp payments`
2. Define a `PaymentProcessor` interface in `payments/processors.py`.
3. Install provider SDKs: `pip install stripe paypalrestsdk`

## 🛠️ Implementation Steps

1. **Define Processor Interface** (`payments/processors.py`):
```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def charge(self, amount: float, currency: str, source: str) -> dict:
        pass
```

2. **Implement Concrete Strategies**:
```python
    class StripeProcessor(PaymentProcessor):
        def charge(self, amount: float, currency: str, source: str) -> dict:
            # Stripe SDK logic here
            pass

class PayPalProcessor(PaymentProcessor):
    def charge(self, amount: float, currency: str, source: str) -> dict:
        # PayPal SDK logic here
        pass
```

3. **Factory** (`payments/factory.py`):
```python
def get_processor(provider: str) -> PaymentProcessor:
    if provider == 'stripe':
        return StripeProcessor()
    if provider == 'paypal':
        return PayPalProcessor()
    raise ValueError(f"Unknown provider {provider}")
```

4. **Usage in Views**:
```python
from payments.factory import get_processor

def checkout(request):
    provider = settings.PAYMENT_PROVIDER  # 'stripe' or 'paypal'
    processor = get_processor(provider)
    result = processor.charge(100.0, 'GBP', request.POST['token'])
    return JsonResponse(result)
```

## 📁 Recommended File Structure

```
payments/
├── __init__.py
├── processors.py      # interface + concrete classes
├── factory.py         # Factory function
├── views.py           # Checkout logic
└── tests.py           # Unit tests for each processor and factory
```

## ✅ Testing

- Write unit tests for each processor using mocks for external SDK calls.
- Test the factory returns the correct processor instance.


---

*Next:* [Notification System Project](NotificationSystem.html)

Title: Custom Django Middleware
Date: 2025-04-30 20:20
Modified: 2025-04-30
Category: Projects
Tags: django, middleware, decorator pattern, python
Slug: projects/CustomDjangoMiddleware
Authors: Alin Morosanu
Summary: Develop Django middleware using the Decorator pattern to add behaviors (e.g., logging, header injection) to request/response processing.

---

**Goal:** Implement a flexible middleware system in Django to wrap request/response handling and compose behaviors dynamically.

## 📚 Patterns Used

- **Decorator Pattern:** Wrap the base Middleware class to add cross-cutting concerns like logging, authentication, or response modification.

## 🔧 Setup

1. In your Django project, create an app, e.g.: `python manage.py startapp core`
2. Inside `core/middleware.py`, define base and decorator classes.
3. Add middleware to `MIDDLEWARE` in `settings.py`.

## 🛠️ Implementation Steps

1. **Base Middleware** (`core/middleware.py`):
   
```python
class BaseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)
```

2. **Decorator Base**:
```python
class MiddlewareDecorator(BaseMiddleware):
    def __init__(self, get_response):
        super().__init__(get_response)
        self._wrapped = BaseMiddleware(get_response)
    
    def __call__(self, request):
        return self._wrapped(request)
```

3. **Concrete Decorators**:
   - **LoggingMiddleware** logs requests/responses.
   - **HeaderMiddleware** injects custom headers.
```python
class LoggingMiddleware(MiddlewareDecorator):
    def __call__(self, request):
        print(f"Request Path: {request.path}")
        response = super().__call__(request)
        print(f"Status Code: {response.status_code}")
        return response
```

4. **Register Middleware** in `settings.py`:
```python
MIDDLEWARE = [
    'core.middleware.LoggingMiddleware',
    'core.middleware.HeaderMiddleware',
    # other Django middleware
]
```

## 📁 Recommended File Structure

```
core/
├── __init__.py
├── middleware.py    # base, decorator, concrete classes
└── tests.py         # unit tests for middleware
```

## ✅ Testing

- Use Django's `RequestFactory` to simulate requests and assert middleware behavior.
- Test composition order by stacking multiple decorators.

---

*Precvious:* [Notification System Project](NotificationSystem.html)

*Next:* [Background Task Queue](BackgroundTaskQueue.html)

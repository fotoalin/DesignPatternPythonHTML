Title: Notification System
Date: 2025-04-30 20:30
Modified: 2025-04-30
Category: Projects
Tags: notifications, observer pattern, django, python, websocket
Slug: projects/NotificationSystem
Authors: Alin Morosanu
Summary: Build a real-time notification system in Django, using Observer and Strategy patterns to support multiple channels (WebSocket, email).

---

**Goal:** Implement a real-time notification infrastructure for Django that can broadcast alerts to users via different channels (WebSocket, email, SMS).

## 📚 Patterns Used

- **Observer Pattern:** Register subscribers for notification events and notify them on state changes.
- **Strategy Pattern:** Define multiple delivery strategies (WebSocket, email, SMS) and switch based on user preference.

## 🔧 Setup

1. Install Django Channels: `pip install channels`
2. Configure `ASGI_APPLICATION` and channel layers (e.g., Redis).
3. Create a `notifications` app.

## 🛠️ Implementation Steps

1. **Define Notification Event** (`notifications/events.py`):
```python
class NotificationEvent:
    def __init__(self, user, message):
        self.user = user
        self.message = message
```

2. **Observer Manager** (`notifications/manager.py`):
```python
class NotificationManager:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def notify(self, event):
        for sub in self._subscribers:
            sub.update(event)
```

3. **Delivery Strategies** (`notifications/strategies.py`):
```python
class WebSocketStrategy:
    def update(self, event):
        # send via Channels group_send
        pass

class EmailStrategy:
    def update(self, event):
        # send email
        pass
```

4. **Usage Example** (`notifications/services.py`):
```python
manager = NotificationManager()
manager.subscribe(WebSocketStrategy())
manager.subscribe(EmailStrategy())

# On some action:
event = NotificationEvent(user, 'You have a new message')
manager.notify(event)
```

## 📁 Recommended File Structure

```
notifications/
├── __init__.py
├── events.py         # notification event definitions
├── manager.py        # observer manager
├── strategies.py     # delivery strategies
└── services.py       # high-level API to trigger notifications
```

## ✅ Testing

- Use Django test client and Channels `Communicator` to simulate WebSocket.
- Mock email backend to verify email sends.
- Test manager.notify calls subscriber.update correctly.

---

*Previous:* [Payment Gateway Integration](PaymentGatewayIntegration.html)

*Next:* [Custom Django Middleware (Decorator)](CustomDjangoMiddleware.html)

Title: Background Task Queue
Date: 2025-04-30 20:10
Modified: 2025-04-30
Category: Projects
Tags: celery, background tasks, queue, django, python
Slug: projects/BackgroundTaskQueue
Authors: Alin Morosanu
Summary: Build a Django-based background task processing system using Celery and message queues, applying Command and Observer patterns.

---

**Goal:** Implement a robust background processing system for Django to handle asynchronous tasks like sending emails, reports, or long-running jobs.

## 📚 Patterns Used

- **Command Pattern:** Encapsulate tasks as command objects for execution and retry.
- **Observer Pattern:** Notify subscribers on task events (success, failure).
- **Strategy Pattern:** Switch between different broker backends (Redis, RabbitMQ) at runtime.

## 🔧 Setup

1. Install Celery and a message broker, e.g.: `pip install celery redis`
2. Configure `CELERY_BROKER_URL` and `CELERY_RESULT_BACKEND` in Django `settings.py`.
3. Create a `tasks.py` module in your Django app.

## 🛠️ Implementation Steps

1. **Define Task Base** (`app/tasks.py`):
```python
from celery import shared_task

@shared_task(bind=True)
def process_report(self, user_id):
    # task logic...
    return result
```

2. **Command Wrapper**:
```python
class TaskCommand:
    def __init__(self, task, *args, **kwargs):
        self.task = task
        self.args = args
        self.kwargs = kwargs

    def execute(self):
        return self.task.delay(*self.args, **self.kwargs)
```

3. **Event Observer** (`app/events.py`):
```python
class TaskObserver:
    def on_success(self, result):
        pass

    def on_failure(self, exc):
        pass
```

4. **Runner Service** (`app/services.py`):
```python
from tasks import process_report
from .commands import TaskCommand

def run_report(user_id):
    cmd = TaskCommand(process_report, user_id)
    result = cmd.execute()
    result.then(on_success=observer.on_success, on_failure=observer.on_failure)
```

## 📁 Recommended File Structure

```
app/
├── tasks.py         # Celery task definitions
├── commands.py      # TaskCommand and related classes
├── events.py        # Observer interfaces and implementations
└── services.py      # Runner that ties commands and observers
```

## ✅ Testing

- Unit test Celery tasks with `celery.app.Task.run()` for sync execution.
- Mock broker calls to verify task dispatch.
- Test observer callbacks for success/failure events.

---

*Previous:* [Custom Django Middleware (Decorator)](CustomDjangoMiddleware.html)

*Next:* [Order Processing Workflow](OrderProcessingWorkflow.html)

Title: Iterator Pattern
Date: 2025-04-30 19:45
Modified: 2025-04-30
Category: Behavioral Patterns
Tags: iterator, behavioral pattern, design patterns, python
Slug: behavioral/iterator
Authors: Alin Morosanu
Summary: Learn about the Iterator pattern, which provides a way to access elements of an aggregate object sequentially without exposing its underlying representation.

---

## Iterator Pattern

**Type:** Behavioral

### Intent

Provide a way to access elements of an aggregate object sequentially without exposing its underlying representation.

### Problem

You have a collection of objects and want to traverse them without exposing the internals of the collection.

### Solution

Define an Iterator interface with methods like __iter__() and __next__(). The aggregate returns an iterator object that implements these methods.

### Python Implementation Example

```python
class Iterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            value = self._collection[self._index]
        except IndexError:
            raise StopIteration
        self._index += 1
        return value

# Client code
data = [1, 2, 3]
for item in Iterator(data):
    print(item)
```

### Pros

* Simplifies traversal of complex data structures
* Decouples collection from traversal logic

### Cons

* Additional classes or methods for simple collections

### When to Use

* When you need uniform traversal of different aggregate structures
* When you want to support multiple traversal algorithms

---

**Next:** [Interpreter Pattern](./interpreter.html) 
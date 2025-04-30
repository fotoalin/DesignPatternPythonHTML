Title: Interpreter Pattern
Date: 2025-04-30 19:50
Modified: 2025-04-30
Category: Behavioral Patterns
Tags: interpreter, behavioral pattern, design patterns, python
Slug: behavioral/interpreter
Authors: Alin Morosanu
Summary: Learn about the Interpreter pattern, which defines a representation for a language's grammar and an interpreter to evaluate sentences in the language.

---

## Interpreter Pattern

**Type:** Behavioral

### Intent

Define a representation for a grammar of a language, and an interpreter that uses this representation to interpret sentences in the language.

### Problem

You need to parse or evaluate sentences in a language, and you want a flexible way to represent grammar rules and evaluation logic.

### Solution

Define an AbstractExpression interface with an interpret(context) method. Implement terminal and non-terminal expressions for grammar rules. Build a syntax tree and interpret it by calling interpret on the root.

### Python Implementation Example

```python
from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value

class Add(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)

# Client code
context = {}
expression = Add(Number(2), Add(Number(3), Number(4)))
print(expression.interpret(context))  # Output: 9
```

### Pros

* Simplifies design of interpreters for simple languages
* Easy to extend grammar by adding new expression classes

### Cons

* Can lead to many classes for complex grammars
* Parsing and syntax tree construction may require extra code

### When to Use

* When you need to implement a simple grammar or DSL
* When grammar rules change frequently

---

**Next:** (end of series)
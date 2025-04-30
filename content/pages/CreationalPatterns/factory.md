Title: Factory Pattern (Factory Method & Simple Factory)
Date: 2025-04-30 16:15
Modified: 2025-04-30
Category: Creational Patterns
Tags: factory method, simple factory, creational pattern, design patterns, python
Slug: creational/factory
Authors: Alin Morosanu
Summary: Learn about the Factory Method and Simple Factory patterns for creating objects without specifying the exact class.

---

## Factory Pattern (Factory Method & Simple Factory)

**Type:** Creational

Often, "Factory Pattern" can refer to two related but distinct patterns: **Simple Factory** (which isn't one of the original GoF patterns but is very common) and **Factory Method** (which is a GoF pattern).

### Intent

*   **Simple Factory:** Encapsulate object creation logic in one place, simplifying the client code.
*   **Factory Method:** Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.

### Problem

Imagine you have code that needs to create different types of objects based on some condition (e.g., user input, configuration). Directly using constructors (`MyClass(...)`) throughout your client code can lead to problems:

*   **Tight Coupling:** The client code becomes tightly coupled to the concrete classes it instantiates. If you add a new class or change an existing one, you have to find and modify all the places where it's created.
*   **Violates Open/Closed Principle:** Adding new types of objects requires modifying the client code's creation logic.
*   **Complex Client Code:** The client code gets cluttered with `if/elif/else` or `switch` statements for object creation.

### Solution

#### 1. Simple Factory

A Simple Factory is often just a class or function that encapsulates the logic for selecting and creating objects of different types based on input parameters. It centralizes the creation logic.

```python
from abc import ABC, abstractmethod

# Product Interface (Optional but good practice)
class Document(ABC):
    @abstractmethod
    def display(self):
        pass

# Concrete Products
class TextDocument(Document):
    def display(self):
        print("Displaying text document...")

class PdfDocument(Document):
    def display(self):
        print("Displaying PDF document...")

class SpreadsheetDocument(Document):
    def display(self):
        print("Displaying spreadsheet document...")

# Simple Factory
class DocumentFactory:
    @staticmethod
    def create_document(doc_type: str) -> Document:
        """Creates a document object based on the type."""
        if doc_type == 'text':
            return TextDocument()
        elif doc_type == 'pdf':
            return PdfDocument()
        elif doc_type == 'spreadsheet':
            return SpreadsheetDocument()
        else:
            raise ValueError(f"Unknown document type: {doc_type}")

# Client Code
doc_type = "pdf" # Could come from config, user input, etc.
document = DocumentFactory.create_document(doc_type)
document.display() # Output: Displaying PDF document...

doc_type = "text"
document = DocumentFactory.create_document(doc_type)
document.display() # Output: Displaying text document...
```
*Explanation:* The client code (`DocumentFactory.create_document(...)`) doesn't need to know about `TextDocument` or `PdfDocument`. It just asks the factory for a document of a certain type. All the creation logic is hidden inside the factory.

#### 2. Factory Method

The Factory Method pattern uses inheritance. A base class (Creator) declares an abstract `factory_method` that subclasses must implement to create specific product objects. The Creator class often has methods that work with the product created by the factory method, unaware of the concrete product type.

```python
from abc import ABC, abstractmethod

# --- Product Interface and Concrete Products (same as Simple Factory example) ---
class Document(ABC):
    @abstractmethod
    def display(self):
        pass

class TextDocument(Document):
    def display(self):
        print("Displaying text document...")

class PdfDocument(Document):
    def display(self):
        print("Displaying PDF document...")

# --- Creator Abstract Class ---
class Application(ABC):
    """The Creator class declares the factory method."""

    @abstractmethod
    def factory_method(self) -> Document:
        """Subclasses will override this to create specific documents."""
        pass

    def open_document(self):
        """Core logic that uses the product created by the factory method."""
        doc = self.factory_method()
        print("Application: Using the created document.")
        doc.display()

# --- Concrete Creators ---
class TextApplication(Application):
    """Concrete Creator for text documents."""
    def factory_method(self) -> Document:
        print("TextApplication: Creating a TextDocument.")
        return TextDocument()

class PdfApplication(Application):
    """Concrete Creator for PDF documents."""
    def factory_method(self) -> Document:
        print("PdfApplication: Creating a PdfDocument.")
        return PdfDocument()

# Client Code
def client_code(creator: Application):
    """The client code works with an instance of a concrete creator,
       albeit through its base interface. As long as the client keeps
       working with the creator via the base interface, you can pass it
       any creator's subclass."""
    print("Client: I'm not aware of the creator's concrete class, but it works.")
    creator.open_document()

print("App: Launched with the TextApplication.")
client_code(TextApplication())
# Output:
# App: Launched with the TextApplication.
# Client: I'm not aware of the creator's concrete class, but it works.
# TextApplication: Creating a TextDocument.
# Application: Using the created document.
# Displaying text document...

print("\nApp: Launched with the PdfApplication.")
client_code(PdfApplication())
# Output:
# App: Launched with the PdfApplication.
# Client: I'm not aware of the creator's concrete class, but it works.
# PdfApplication: Creating a PdfDocument.
# Application: Using the created document.
# Displaying PDF document...
```
*Explanation:* The `Application` class defines the structure (`open_document`) but delegates the actual object creation to its subclasses (`TextApplication`, `PdfApplication`) via the `factory_method`. The client code interacts with the `Application` interface, decoupling it from the concrete document types.

### Pros

*   **Decoupling:** Reduces coupling between client code and concrete product classes.
*   **Single Responsibility Principle:** Moves creation logic out of the client code (Simple Factory) or into dedicated subclasses (Factory Method).
*   **Open/Closed Principle:** Allows introducing new product types without modifying client code (Simple Factory requires modifying the factory; Factory Method requires adding a new Creator subclass).
*   **Flexibility (Factory Method):** Gives subclasses control over object creation.

### Cons

*   **Increased Complexity:** Introduces more classes/functions (factories or creator hierarchies).
*   **Simple Factory Limitation:** If adding new product types, the factory itself needs modification (violating OCP for the factory).
*   **Factory Method Hierarchy:** Can lead to a parallel hierarchy of Creator classes alongside Product classes.

### When to Use

*   **Simple Factory:** When you have a relatively simple creation process with a limited number of types, and you want to centralize creation logic away from the client.
*   **Factory Method:**
    *   When a class can't anticipate the class of objects it must create.
    *   When a class wants its subclasses to specify the objects it creates.
    *   When you want to localize the knowledge of which helper subclass is the delegate.

---

**Next:** [Abstract Factory Pattern](link-to-abstract-factory.html) 

Title: Builder Pattern
Date: 2025-04-30 16:45
Modified: 2025-04-30
Category: Creational Patterns
Tags: builder, creational pattern, design patterns, python
Slug: creational/builder
Authors: Alin Morosanu
Summary: Learn about the Builder pattern to construct complex objects step by step, allowing different representations.

---

## Builder Pattern

**Type:** Creational

### Intent

Separate the construction of a **complex object** from its representation so that the same construction process can create **different representations**.

### Problem

Imagine an object that requires many configuration steps or has numerous optional parameters in its constructor. Examples include:

*   Creating a complex query object (SQL, NoSQL).
*   Building a configuration object with many settings.
*   Constructing a document with various sections (header, body, footer, formatting).
*   Creating a user profile with optional fields (address, phone, preferences).

Using a single constructor with many parameters becomes unwieldy and error-prone:

*   **Telescoping Constructor:** You might create multiple constructors with different subsets of parameters. This leads to code duplication and confusion.
*   **Many Optional Parameters:** A single constructor with many `None` defaults makes it hard to know which parameters are required and easy to mix up the order.
*   **Inconsistent State:** If the object requires multiple steps to be fully configured, it might be in an inconsistent state partway through the process if created directly.

### Solution

The Builder pattern extracts the object construction logic into a separate class called a **Builder**. It involves:

1.  **Builder Interface:** Defines abstract steps for constructing parts of the product (e.g., `build_part_a()`, `build_part_b()`). It also usually includes a method to retrieve the final product (e.g., `get_result()`).
2.  **Concrete Builders:** Implement the Builder interface, providing specific implementations for the building steps. Each Concrete Builder might produce a different representation of the product. They often keep track of the product being built internally.
3.  **Product:** The complex object being constructed. Its constructor might be simple or even private, as the Builder handles the assembly.
4.  **Director (Optional):** A class that orchestrates the construction process using a Builder object. It defines the order in which to call the building steps. The client interacts with the Director (or directly with a Builder).

This allows the client code to:
*   Instantiate a specific Builder.
*   Optionally, pass the Builder to a Director, which calls the building steps in a predefined sequence.
*   Or, call the building steps on the Builder directly.
*   Finally, retrieve the fully constructed object from the Builder.

### Python Implementation Example

Let's build different representations of a computer.

```python
from abc import ABC, abstractmethod
from typing import List

# --- Product ---
class Computer:
    """The complex object being built."""
    def __init__(self):
        self.parts: List[str] = []

    def add_part(self, part: str):
        self.parts.append(part)

    def __str__(self):
        return f"Computer parts: {', '.join(self.parts)}"

# --- Builder Interface ---
class ComputerBuilder(ABC):
    @abstractmethod
    def build_cpu(self):
        pass

    @abstractmethod
    def build_ram(self):
        pass

    @abstractmethod
    def build_storage(self):
        pass

    @abstractmethod
    def get_computer(self) -> Computer:
        pass

# --- Concrete Builders ---
class GamingComputerBuilder(ComputerBuilder):
    """Builds a high-end gaming computer."""
    def __init__(self):
        self._computer = Computer()

    def build_cpu(self):
        self._computer.add_part("High-performance CPU")

    def build_ram(self):
        self._computer.add_part("32GB RAM")

    def build_storage(self):
        self._computer.add_part("1TB NVMe SSD")
        self._computer.add_part("Dedicated Graphics Card") # Specific to gaming

    def get_computer(self) -> Computer:
        return self._computer

class OfficeComputerBuilder(ComputerBuilder):
    """Builds a standard office computer."""
    def __init__(self):
        self._computer = Computer()

    def build_cpu(self):
        self._computer.add_part("Standard CPU")

    def build_ram(self):
        self._computer.add_part("16GB RAM")

    def build_storage(self):
        self._computer.add_part("512GB SATA SSD")

    def get_computer(self) -> Computer:
        return self._computer

# --- Director (Optional) ---
class Director:
    """Orchestrates the building process."""
    def __init__(self, builder: ComputerBuilder):
        self._builder = builder

    def construct_computer(self):
        print("Director: Starting construction.")
        self._builder.build_cpu()
        self._builder.build_ram()
        self._builder.build_storage()
        print("Director: Construction finished.")

    def set_builder(self, builder: ComputerBuilder):
        self._builder = builder

# --- Client Code ---

# Using the Director
print("--- Building with Director ---")
gaming_builder = GamingComputerBuilder()
director = Director(gaming_builder)
director.construct_computer()
gaming_pc = gaming_builder.get_computer()
print(gaming_pc)
# Output:
# --- Building with Director ---
# Director: Starting construction.
# Director: Construction finished.
# Computer parts: High-performance CPU, 32GB RAM, 1TB NVMe SSD, Dedicated Graphics Card

office_builder = OfficeComputerBuilder()
director.set_builder(office_builder) # Change the builder
director.construct_computer()
office_pc = office_builder.get_computer()
print(office_pc)
# Output:
# Director: Starting construction.
# Director: Construction finished.
# Computer parts: Standard CPU, 16GB RAM, 512GB SATA SSD

# Using the Builder directly (Fluent Interface style)
print("\n--- Building directly with Builder (Fluent) ---")
class FluentComputerBuilder:
    def __init__(self):
        self._computer = Computer()

    def add_cpu(self, spec: str):
        self._computer.add_part(f"CPU: {spec}")
        return self # Return self for chaining

    def add_ram(self, spec: str):
        self._computer.add_part(f"RAM: {spec}")
        return self

    def add_storage(self, spec: str):
        self._computer.add_part(f"Storage: {spec}")
        return self

    def add_gpu(self, spec: str):
        self._computer.add_part(f"GPU: {spec}")
        return self

    def get_computer(self) -> Computer:
        return self._computer

custom_pc = (FluentComputerBuilder()
             .add_cpu("AMD Ryzen 9")
             .add_ram("64GB DDR5")
             .add_storage("2TB NVMe Gen4 SSD")
             .add_gpu("NVIDIA RTX 4090")
             .get_computer())
print(custom_pc)
# Output:
# --- Building directly with Builder (Fluent) ---
# Computer parts: CPU: AMD Ryzen 9, RAM: 64GB DDR5, Storage: 2TB NVMe Gen4 SSD, GPU: NVIDIA RTX 4090

```
*Explanation:* We define a `Computer` product, a `ComputerBuilder` interface, and two concrete builders (`GamingComputerBuilder`, `OfficeComputerBuilder`). The optional `Director` shows how to encapsulate a standard construction sequence. The client can use the Director or interact with a builder directly. The fluent interface example shows a common variation where builder methods return `self` to allow chaining.

### Pros

*   **Step-by-Step Construction:** Allows you to construct objects step by step, under your control.
*   **Different Representations:** The same construction process can create different product variations (using different Concrete Builders).
*   **Isolates Complex Construction Code:** Moves complex construction logic out of the business logic of the product and client.
*   **Improved Readability:** Client code for object creation becomes more readable, especially compared to constructors with many parameters.

### Cons

*   **Increased Complexity:** Requires creating multiple new classes (Builder interface, Concrete Builders, potentially a Director).
*   **Mutability:** The product is often mutable during the building process (though the final product returned can be made immutable).

### When to Use

*   When the algorithm for creating a complex object should be independent of the parts that make up the object and how they're assembled.
*   When the construction process must allow different representations for the object that's constructed.
*   When you want to avoid a constructor with a large number of parameters (telescoping constructor or many optional arguments).
*   When you need more control over the construction process than a Factory pattern typically provides.

---

**Next:** [Prototype Pattern](link-to-prototype-pattern.html) 

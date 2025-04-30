Title: Composite Pattern
Date: 2025-04-30 18:00
Modified: 2025-04-30
Category: Structural Patterns
Tags: composite, structural pattern, design patterns, python, tree structure
Slug: structural/composite
Authors: Alin Morosanu
Summary: Learn about the Composite pattern, which allows you to compose objects into tree structures to represent part-whole hierarchies.

---

## Composite Pattern

**Type:** Structural

### Intent

Compose objects into **tree structures** to represent **part-whole hierarchies**. Composite lets clients treat individual objects and compositions of objects **uniformly**.

### Problem

Imagine you are building a file system explorer. A file system consists of files and directories. Directories can contain files or other directories, forming a tree structure. You want to:

*   Represent both files and directories in a uniform way.
*   Allow clients to interact with individual files and directories in the same manner (e.g., `get_size()` or `display()`).
*   Avoid duplicating code for handling files and directories.

### Solution

The Composite pattern models the tree structure with **components**:

1.  **Component Interface:** Declares common operations for both simple (leaf) and complex (composite) objects.
2.  **Leaf:** Represents simple objects (e.g., files). Implements the Component interface.
3.  **Composite:** Represents complex objects (e.g., directories). Implements the Component interface and stores child components (both leaves and composites).
4.  **Client:** Interacts with components through the Component interface, treating leaves and composites uniformly.

### Python Implementation Example

Let's model a file system with files and directories.

```python
from abc import ABC, abstractmethod
from typing import List

# --- Component Interface ---
class FileSystemComponent(ABC):
    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def display(self, indent: int = 0):
        pass

# --- Leaf ---
class File(FileSystemComponent):
    def __init__(self, name: str, size: int):
        self._name = name
        self._size = size

    def get_size(self) -> int:
        return self._size

    def display(self, indent: int = 0):
        print(" " * indent + f"File: {self._name} ({self._size} KB)")

# --- Composite ---
class Directory(FileSystemComponent):
    def __init__(self, name: str):
        self._name = name
        self._children: List[FileSystemComponent] = []

    def add(self, component: FileSystemComponent):
        self._children.append(component)

    def remove(self, component: FileSystemComponent):
        self._children.remove(component)

    def get_size(self) -> int:
        return sum(child.get_size() for child in self._children)

    def display(self, indent: int = 0):
        print(" " * indent + f"Directory: {self._name}")
        for child in self._children:
            child.display(indent + 2)

# --- Client Code ---

# Create files
file1 = File("file1.txt", 10)
file2 = File("file2.txt", 20)
file3 = File("file3.txt", 30)

# Create directories
root = Directory("root")
sub_dir1 = Directory("sub_dir1")
sub_dir2 = Directory("sub_dir2")

# Build the tree structure
root.add(file1)
root.add(sub_dir1)
sub_dir1.add(file2)
sub_dir1.add(sub_dir2)
sub_dir2.add(file3)

# Client interacts with the tree
print("File System Structure:")
root.display()

print("\nTotal Size:", root.get_size(), "KB")

# Output:
# File System Structure:
# Directory: root
#   File: file1.txt (10 KB)
#   Directory: sub_dir1
#     File: file2.txt (20 KB)
#     Directory: sub_dir2
#       File: file3.txt (30 KB)
#
# Total Size: 60 KB

```
*Explanation:* The `FileSystemComponent` interface declares `get_size()` and `display()` methods. `File` is a leaf that implements these methods directly. `Directory` is a composite that stores child components (both files and directories) and delegates operations to them. The client interacts with the `root` directory, treating it as a single object, even though it contains a tree of files and directories.

### Pros

*   **Uniformity:** Treat individual objects and compositions uniformly.
*   **Extensibility:** New types of components (e.g., symbolic links) can be added without changing existing code.
*   **Simplifies Client Code:** The client doesn't need to distinguish between simple and complex components.

### Cons

*   **Overhead:** Managing the tree structure can add complexity and overhead, especially for large hierarchies.
*   **Inappropriate for Flat Structures:** If the structure is flat (e.g., no nesting), the Composite pattern might be overkill.

### When to Use

*   When you need to represent part-whole hierarchies of objects.
*   When you want clients to treat individual objects and compositions uniformly.
*   When you want to simplify client code by hiding the complexity of the tree structure.

---

**Next:** [Proxy Pattern](./proxy.html)

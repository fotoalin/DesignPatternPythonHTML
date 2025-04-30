Title: Proxy Pattern
Date: 2025-04-30 18:15
Modified: 2025-04-30
Category: Structural Patterns
Tags: proxy, structural pattern, design patterns, python, access control
Slug: structural/proxy
Authors: Alin Morosanu
Summary: Learn about the Proxy pattern, which provides a surrogate or placeholder for another object to control access to it.

---

## Proxy Pattern

**Type:** Structural

### Intent

Provide a **surrogate** or **placeholder** for another object to control access to it. Proxies are used to add an additional level of indirection to support controlled access, lazy initialization, logging, or other features.

### Problem

Sometimes, you want to control access to an object or add extra behavior without modifying the object itself. For example:

*   **Expensive Objects:** You want to delay the creation of a resource-intensive object until it's actually needed (e.g., loading a large image).
*   **Access Control:** You want to restrict access to certain objects based on user permissions.
*   **Remote Access:** You want to interact with an object located in a different address space (e.g., a remote server).
*   **Logging/Monitoring:** You want to log or monitor interactions with an object.

### Solution

The Proxy pattern introduces a **proxy object** that implements the same interface as the real object. The proxy holds a reference to the real object and delegates requests to it. The proxy can add its own behavior **before** or **after** delegating the request.

### Types of Proxies

1.  **Virtual Proxy:** Delays the creation and initialization of an expensive object until it's needed.
2.  **Protection Proxy:** Controls access to the real object based on permissions.
3.  **Remote Proxy:** Represents an object in a different address space (e.g., a remote server).
4.  **Logging Proxy:** Logs requests to the real object.

### Python Implementation Example

Let's create a virtual proxy for a resource-intensive object (e.g., a large image).

```python
from abc import ABC, abstractmethod

# --- Subject Interface ---
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# --- Real Subject ---
class RealImage(Image):
    def __init__(self, filename: str):
        self._filename = filename
        self._load_image_from_disk()

    def _load_image_from_disk(self):
        print(f"Loading image from disk: {self._filename}")

    def display(self):
        print(f"Displaying image: {self._filename}")

# --- Proxy ---
class ProxyImage(Image):
    def __init__(self, filename: str):
        self._filename = filename
        self._real_image = None

    def display(self):
        if self._real_image is None:
            print(f"Proxy: Loading real image for the first time.")
            self._real_image = RealImage(self._filename)
        self._real_image.display()

# --- Client Code ---

# Client interacts with the proxy instead of the real object
image1 = ProxyImage("photo1.jpg")
image2 = ProxyImage("photo2.jpg")

# Image is loaded only when display is called
print("First display call for image1:")
image1.display()

print("\nSecond display call for image1:")
image1.display()

print("\nFirst display call for image2:")
image2.display()

# Output:
# First display call for image1:
# Proxy: Loading real image for the first time.
# Loading image from disk: photo1.jpg
# Displaying image: photo1.jpg
#
# Second display call for image1:
# Displaying image: photo1.jpg
#
# First display call for image2:
# Proxy: Loading real image for the first time.
# Loading image from disk: photo2.jpg
# Displaying image: photo2.jpg

```
*Explanation:* The `Image` interface defines the `display()` method. `RealImage` is the real subject that loads and displays the image. `ProxyImage` is the proxy that delays the creation of `RealImage` until `display()` is called. The client interacts with `ProxyImage`, unaware of whether it's dealing with the proxy or the real object.

### Pros

*   **Lazy Initialization:** Delays the creation of resource-intensive objects until they're needed.
*   **Access Control:** Adds security by controlling access to the real object.
*   **Logging/Monitoring:** Adds logging or monitoring functionality without modifying the real object.
*   **Decouples Client and Real Object:** The client interacts with the proxy, not the real object.

### Cons

*   **Overhead:** Adds an extra layer of indirection, which can introduce performance overhead.
*   **Complexity:** Increases the complexity of the codebase.

### When to Use

*   When you need to control access to an object.
*   When you want to add extra behavior (e.g., logging) without modifying the real object.
*   When you want to delay the creation of a resource-intensive object until it's needed.
*   When you need to interact with a remote object as if it were local.

---

**Next:** [Bridge Pattern](./bridge.html) *(Link TBD)*

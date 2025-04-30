Title: Facade Pattern
Date: 2025-04-30 17:45
Modified: 2025-04-30
Category: Structural Patterns
Tags: facade, structural pattern, design patterns, python, simplification
Slug: structural/facade
Authors: Alin Morosanu
Summary: Learn about the Facade pattern, which provides a simplified interface to a complex subsystem.

---

## Facade Pattern

**Type:** Structural

### Intent

Provide a **unified interface** to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem **easier to use**.

### Problem

Imagine a complex system with many interacting classes and objects (e.g., a video conversion library, a complex set of APIs for an online store, a home automation system). To perform a common task, a client might need to interact with multiple objects within the subsystem, understand their relationships, and manage their lifecycles.

This leads to:
*   **High Coupling:** The client code becomes tightly coupled to the internal structure of the subsystem.
*   **Complexity:** The client has to manage the intricate details of the subsystem's interactions.
*   **Difficult Maintenance:** Changes within the subsystem can easily break the client code.

Clients often don't need the full flexibility of the subsystem; they just want a simple way to perform common tasks.

### Solution

The Facade pattern introduces a single `Facade` class that:

1.  **Knows the Subsystem:** It holds references to the necessary objects within the complex subsystem.
2.  **Provides Simplified Methods:** It offers a limited number of high-level methods that correspond to common client tasks.
3.  **Delegates Requests:** When a client calls a facade method, the facade orchestrates the necessary interactions among the subsystem objects to fulfill the request.

The client interacts only with the Facade, decoupling it from the complexities of the subsystem.

### Python Implementation Example

Let's model a simplified home theater system with multiple components (DVD Player, Projector, Amplifier, Screen) and create a facade to simplify common actions like "Watch Movie" and "End Movie".

```python
# --- Subsystem Components ---
class DvdPlayer:
    def on(self): print("DVD Player: On")
    def off(self): print("DVD Player: Off")
    def play(self, movie: str): print(f"DVD Player: Playing '{movie}'")
    def stop(self): print("DVD Player: Stopped")

class Projector:
    def on(self): print("Projector: On")
    def off(self): print("Projector: Off")
    def wide_screen_mode(self): print("Projector: Wide Screen Mode")

class Amplifier:
    def on(self): print("Amplifier: On")
    def off(self): print("Amplifier: Off")
    def set_dvd(self, dvd_player: DvdPlayer): print("Amplifier: Setting DVD player")
    def set_surround_sound(self): print("Amplifier: Surround Sound On")
    def set_volume(self, level: int): print(f"Amplifier: Setting Volume to {level}")

class Screen:
    def up(self): print("Screen: Going Up")
    def down(self): print("Screen: Going Down")

# --- Facade Class ---
class HomeTheaterFacade:
    """Provides a simplified interface to the home theater subsystem."""
    def __init__(self, amp: Amplifier, dvd: DvdPlayer, proj: Projector, screen: Screen):
        print("HomeTheaterFacade: Initializing subsystem components.")
        self._amplifier = amp
        self._dvd_player = dvd
        self._projector = proj
        self._screen = screen

    def watch_movie(self, movie: str):
        """Handles all steps to start watching a movie."""
        print("\nFacade: Get ready to watch a movie...")
        self._screen.down()
        self._projector.on()
        self._projector.wide_screen_mode()
        self._amplifier.on()
        self._amplifier.set_dvd(self._dvd_player)
        self._amplifier.set_surround_sound()
        self._amplifier.set_volume(5)
        self._dvd_player.on()
        self._dvd_player.play(movie)

    def end_movie(self):
        """Handles all steps to shut down the theater."""
        print("\nFacade: Shutting movie theater down...")
        self._dvd_player.stop()
        self._dvd_player.off()
        self._amplifier.off()
        self._projector.off()
        self._screen.up()

# --- Client Code ---

# Create subsystem components
amp = Amplifier()
dvd = DvdPlayer()
proj = Projector()
screen = Screen()

# Create the Facade
facade = HomeTheaterFacade(amp, dvd, proj, screen)

# Client uses the simple interface
facade.watch_movie("Raiders of the Lost Ark")
facade.end_movie()

# Output:
# HomeTheaterFacade: Initializing subsystem components.
#
# Facade: Get ready to watch a movie...
# Screen: Going Down
# Projector: On
# Projector: Wide Screen Mode
# Amplifier: On
# Amplifier: Setting DVD player
# Amplifier: Surround Sound On
# Amplifier: Setting Volume to 5
# DVD Player: On
# DVD Player: Playing 'Raiders of the Lost Ark'
#
# Facade: Shutting movie theater down...
# DVD Player: Stopped
# DVD Player: Off
# Amplifier: Off
# Projector: Off
# Screen: Going Up

```
*Explanation:* The `HomeTheaterFacade` wraps the `Amplifier`, `DvdPlayer`, `Projector`, and `Screen` objects. The client code only needs to interact with the `facade` object and call simple methods like `watch_movie()` and `end_movie()`. The facade handles the complex sequence of calls to the underlying subsystem components.

### Pros

*   **Simplifies Client Code:** Provides a simpler, higher-level interface for common tasks.
*   **Decouples Client from Subsystem:** Reduces the dependencies between the client and the internal workings of the subsystem. Changes within the subsystem are less likely to affect the client as long as the facade interface remains stable.
*   **Organizes Subsystem:** Can help structure a complex subsystem by introducing a clear entry point.

### Cons

*   **Can Become a God Object:** The facade itself can become overly complex if it tries to expose too much functionality from the subsystem.
*   **Hides Features (Potentially):** While simplifying, it might hide useful lower-level features of the subsystem from clients who need more control (though clients can often still access subsystem objects directly if needed).
*   **Doesn't Prevent Direct Access:** Clients can often still bypass the facade and interact with the subsystem directly if necessary (which can be good or bad depending on the design goals).

### When to Use

*   When you want to provide a simple interface to a complex subsystem.
*   When you want to decouple clients from the implementation details of a subsystem, making the subsystem easier to evolve.
*   When you want to layer your subsystems, using facades to define entry points to each level.

---

**Next:** [Composite Pattern](./composite.html) 

from elevator import Elevator
from request import Request


class ElevatorSystem:
    """Manages multiple elevators and assigns requests to the best elevator."""

    def __init__(self, num_elevators=2, num_floors=10):
        self.elevators = [Elevator(id=i, max_floor=num_floors) for i in range(num_elevators)]
        self.num_floors = num_floors
        self.callbacks = []  # Stores GUI update functions

    def request_elevator(self, floor):
        """Finds the best elevator and assigns the request."""
        best_elevator = min(self.elevators, key=lambda e: abs(e.current_floor - floor))
        best_elevator.add_request(Request(floor))
        self._update_gui()

    def step(self):
        """Moves all elevators one step towards their target floors."""
        for elevator in self.elevators:
            elevator.move()
        self._update_gui()

    def _update_gui(self):
        """Updates the GUI if callback functions are registered."""
        for callback in self.callbacks:
            callback()

    def register_callback(self, callback):
        """Registers a GUI update function."""
        self.callbacks.append(callback)

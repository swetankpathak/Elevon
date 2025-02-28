class Elevator:
    """Represents an individual elevator and manages its movement."""

    def __init__(self, id, min_floor=0, max_floor=10):
        self.id = id  # Elevator ID
        self.current_floor = 0  # Start from ground floor
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.target_floors = []  # Stores requested floors
        self.direction = None  # "UP", "DOWN", or None

    def move(self):
        """Moves the elevator one step towards the next target floor."""
        if not self.target_floors:
            self.direction = None
            return

        next_floor = self.target_floors[0]

        if self.current_floor < next_floor:
            self.current_floor += 1
            self.direction = "UP"
        elif self.current_floor > next_floor:
            self.current_floor -= 1
            self.direction = "DOWN"

        # Remove the floor from the list if reached
        if self.current_floor == next_floor:
            self.target_floors.pop(0)

        print(f"Elevator {self.id} at floor {self.current_floor}, moving {self.direction}")

    def add_request(self, request):
        """Adds a floor request to the elevator's queue."""
        if request.floor not in self.target_floors:
            self.target_floors.append(request.floor)
            self.target_floors.sort(reverse=(self.direction == "DOWN"))  # Sort for efficient movement

        print(f"Request added: Elevator {self.id} now targeting floors: {self.target_floors}")

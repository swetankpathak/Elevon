import tkinter as tk
from elevator_system import ElevatorSystem


class ElevatorGUI:
    """Handles the graphical user interface for the elevator system."""

    def __init__(self, root, num_floors=10, num_elevators=2):
        self.root = root
        self.root.title("Elevator System")
        self.num_floors = num_floors
        self.num_elevators = num_elevators
        self.system = ElevatorSystem(num_elevators, num_floors)
        self.system.register_callback(self.update_gui)

        # Create UI Elements
        self.canvas = tk.Canvas(root, width=400, height=500, bg="black")
        self.canvas.pack()

        self.floor_buttons = []
        for floor in range(self.num_floors):
            button = tk.Button(root, text=f"Request Floor {floor}", command=lambda f=floor: self.request_elevator(f))
            button.pack()
            self.floor_buttons.append(button)

        self.elevator_positions = [
            self.canvas.create_rectangle(50 + (i * 150), 450, 100 + (i * 150), 500, fill="blue")
            for i in range(num_elevators)
        ]

        self.update_gui()

    def request_elevator(self, floor):
        """Handles elevator request from UI."""
        self.system.request_elevator(floor)

    def update_gui(self):
        """Updates elevator positions in the GUI."""
        for i, elevator in enumerate(self.system.elevators):
            y_position = 450 - (elevator.current_floor * 50)  # Convert floor to Y-coordinates
            self.canvas.coords(self.elevator_positions[i], 50 + (i * 150), y_position, 100 + (i * 150), y_position + 50)

    def run(self):
        """Starts the automatic movement of elevators."""

        def move_elevators():
            self.system.step()
            self.root.after(1000, move_elevators)

        move_elevators()
        self.root.mainloop()


# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    gui = ElevatorGUI(root)
    gui.run()

# Elevon
Elevon is a Python-based OOP-driven elevator system with an intuitive GUI, designed to simulate real-world elevator operations efficiently. It provides a structured, scalable, and interactive way to understand elevator mechanics while demonstrating Object-Oriented Programming principles like encapsulation, inheritance, and polymorphism.

---

## 🏗️ **Features**
✅ **Multiple Elevators** - Handles multiple elevators dynamically.
✅ **Optimized Request Handling** - Assigns the nearest elevator to requests.
✅ **Smooth Elevator Movement** - Moves step-by-step until reaching target floors.
✅ **GUI Interface** - Uses Tkinter to display elevator movement.
✅ **Button-Based Requests** - Users can request elevators by clicking buttons.

---

## 📂 **Project Structure**
```
elevator_system/
│── main.py              # Entry point (Runs the GUI)
│── elevator.py          # Elevator class (Handles movement)
│── elevator_system.py   # System class (Manages multiple elevators)
│── request.py           # Request class (Handles user requests)
│── gui.py               # GUI Interface (Tkinter for visualization)
│── README.md            # Project Documentation
```

---

## 🏗 **Installation & Setup**
### **1️⃣ Install Dependencies**
```bash
pip install tk
```

### **2️⃣ Run the Application**
```bash
python gui.py
```

---

## 🎮 **How to Use**
1. **Launch the GUI** - `python gui.py`
2. **Click on Floor Request Buttons** - Calls the nearest elevator.
3. **Watch Elevators Move** - They move step by step.

---

## 🛠 **Code Overview**
### **1️⃣ Request Class (Handles User Requests)**
```python
class Request:
    def __init__(self, floor):
        self.floor = floor  # Floor number
```
✅ **Stores requested floor numbers.**

### **2️⃣ Elevator Class (Handles Movement)**
```python
class Elevator:
    def __init__(self, id, max_floor=10):
        self.id = id
        self.current_floor = 0
        self.target_floors = []
    
    def move(self):
        # Moves elevator step-by-step
```
✅ **Moves the elevator up/down efficiently.**

### **3️⃣ Elevator System (Manages All Elevators)**
```python
class ElevatorSystem:
    def __init__(self, num_elevators=2, num_floors=10):
        self.elevators = [Elevator(i, num_floors) for i in range(num_elevators)]
    
    def request_elevator(self, floor):
        # Assigns nearest elevator
```
✅ **Optimizes elevator assignments.**

### **4️⃣ GUI (Tkinter for Visualization)**
```python
class ElevatorGUI:
    def __init__(self, root, num_floors=10, num_elevators=2):
        self.root = root
        self.canvas = tk.Canvas(root, width=400, height=500, bg="white")
    
    def run(self):
        self.root.mainloop()
```
✅ **Provides an interactive user interface.**

---

## 📌 **System Design**
### **High-Level Design (HLD)**
```
+-------------------------+
|   User Interface (GUI)  |
+-------------------------+
           |
           v
+-------------------------+
|   Elevator System       |
+-------------------------+
           |
           v
+-------------------------+
|   Elevator Instances    |
+-------------------------+
```

### **Low-Level Design (LLD)**
```
+-----------------------+
|      ElevatorSystem   |
+-----------------------+
       |
       v
+-----------------------+
|      Elevator         |
+-----------------------+
       |
       v
+-----------------------+
|      Request         |
+-----------------------+
```
---

## 🎯 **Final Summary**
| Feature | Implemented? |
|---------|-------------|
| Multiple Elevators ✅ | Yes |
| Elevator Movement ✅ | Yes |
| Nearest Elevator Assignment ✅ | Yes |
| GUI Interface ✅ | Yes |
| Button-Based Requests ✅ | Yes |
| Real-Time Animation ✅ | Yes |

---



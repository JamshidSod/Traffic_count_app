import csv
import tkinter as tk
from datetime import datetime

def count_vehicle(vehicle_type, direction):
    count = int(count_labels[vehicle_type][direction]["text"])
    count += 1
    count_labels[vehicle_type][direction]["text"] = str(count)
    save_data(vehicle_type, direction, count)

def reset_counts():
    for vehicle_type in count_labels:
        for direction in count_labels[vehicle_type]:
            count_labels[vehicle_type][direction]["text"] = "0"

def save_data(vehicle_type, direction, count):
    timestamp = datetime.now()
    date = timestamp.date()
    time = timestamp.strftime("%H:%M")

    with open('traffic_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([vehicle_type, direction, count, date, time])

# Create the main window
window = tk.Tk()
window.title("Traffic Count Survey")

# Add labels for Direction A and Direction B
direction_a_label = tk.Label(window, text="Direction A", font=("Arial", 24, "bold"))
direction_a_label.grid(row=0, column=1, pady=10)

direction_b_label = tk.Label(window, text="Direction B", font=("Arial", 24, "bold"))
direction_b_label.grid(row=0, column=3, pady=10)

# Create a dictionary to store the count labels
count_labels = {}

# Define the vehicle types and directions
vehicle_types = [
    "Cars",
    "Minibuses",
    "Buses",
    "Trucks up to 3.5 t",
    "Trucks up to 3.5–12 t",
    "Trucks above 12 t",
    "Road trains",
    "Other"
]

directions = ["Direction A", "Direction B"]

# Create the count labels and buttons for each vehicle type and direction
for i, vehicle_type in enumerate(vehicle_types):
    # Create a nested dictionary to store the count labels for each direction
    count_labels[vehicle_type] = {}
    
    for j, direction in enumerate(directions):
        # Create the count label
        count_label = tk.Label(window, text="0", font=("Arial", 24))
        count_label.grid(row=i+1, column=j*2, padx=30, pady=30, sticky=tk.E+tk.W)  # Align center horizontally
        count_labels[vehicle_type][direction] = count_label

        # Create the count button
        count_button = tk.Button(window, text=vehicle_type, command=lambda vt=vehicle_type, d=direction: count_vehicle(vt, d), font=("Arial", 24))
        count_button.grid(row=i+1, column=j*2 + 1, padx=10, pady=10, sticky=tk.E+tk.W)  # Align center horizontally

# Create the reset button
reset_button = tk.Button(window, text="Reset Counts", command=reset_counts, font=("Arial", 16))
reset_button.grid(row=len(vehicle_types)+1, columnspan=len(directions), pady=10, sticky=tk.E+tk.W)  # Align center horizontally

# Start the Tkinter event loop
window.mainloop()

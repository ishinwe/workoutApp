import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Function to calculate protein intake
def calculate_protein(weight, goal):
    if goal == 'Building Muscle':
        return round(weight * 2.0, 2)  # 2 grams per kg for building muscle
    elif goal == 'Losing Weight':
        return round(weight * 1.5, 2)  # 1.5 grams per kg for losing weight
    elif goal == 'Both':
        return round(weight * 1.8, 2)  # 1.8 grams per kg for both goals

# Function to generate workout split plan
def generate_workout_plan(goal):
    if goal == 'Building Muscle':
        return [
            'Day 1: Upper Body (Push: Chest, Shoulders, Triceps)',
            'Day 2: Lower Body (Legs)',
            'Day 3: Rest',
            'Day 4: Upper Body (Pull: Back, Biceps)',
            'Day 5: Lower Body (Legs)',
            'Day 6: Rest',
            'Day 7: Rest or Light Cardio'
        ]
    elif goal == 'Losing Weight':
        return [
            'Day 1: Cardio + Full Body Strength',
            'Day 2: HIIT Workout',
            'Day 3: Rest or Active Recovery',
            'Day 4: Cardio + Full Body Strength',
            'Day 5: Rest',
            'Day 6: HIIT Workout',
            'Day 7: Rest'
        ]
    elif goal == 'Both':
        return [
            'Day 1: Upper Body Strength + Cardio',
            'Day 2: Lower Body Strength + Cardio',
            'Day 3: HIIT Workout',
            'Day 4: Upper Body Strength + Cardio',
            'Day 5: Lower Body Strength + Cardio',
            'Day 6: Rest',
            'Day 7: Rest or Light Cardio'
        ]

# Function to track weight and show a chart
def track_weight(weights):
    days = list(range(1, len(weights) + 1))
    plt.plot(days, weights, marker='o', color='blue')
    plt.title('Weight Progress Over Time')
    plt.xlabel('Day')
    plt.ylabel('Weight (kg)')
    plt.grid(True)
    plt.show()

# Function to display workout plan and protein intake
def show_plan():
    weight = float(entry_weight.get())
    goal = goal_var.get()

    # Generate workout plan and calculate protein intake
    workout_plan = generate_workout_plan(goal)
    protein_intake = calculate_protein(weight, goal)

    # Display workout plan in a message box
    workout_plan_str = "\n".join(workout_plan)
    messagebox.showinfo("Workout Plan", workout_plan_str)
    
    # Display protein intake
    label_protein.config(text=f"Recommended Protein: {protein_intake}g per day")

# Function to start weight tracking
def start_weight_tracking():
    weights = []
    try:
        for day in range(1, int(entry_days.get()) + 1):
            weight = float(entry_weight_tracking.get())
            weights.append(weight)
        track_weight(weights)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid weight values.")

# Main App
root = tk.Tk()
root.title("Fitness Planner")

# Weight input
label_weight = tk.Label(root, text="Enter your weight (kg):")
label_weight.pack()
entry_weight = tk.Entry(root)
entry_weight.pack()

# Goal selection
label_goal = tk.Label(root, text="Select your fitness goal:")
label_goal.pack()

goal_var = tk.StringVar(value="Building Muscle")
goal_options = ["Building Muscle", "Losing Weight", "Both"]
goal_menu = tk.OptionMenu(root, goal_var, *goal_options)
goal_menu.pack()

# Show Workout Plan and Protein Intake Button
button_show_plan = tk.Button(root, text="Show Plan", command=show_plan)
button_show_plan.pack()

# Protein intake label
label_protein = tk.Label(root, text="Recommended Protein: ")
label_protein.pack()

# Weight tracking
label_days = tk.Label(root, text="Enter number of days to track weight:")
label_days.pack()
entry_days = tk.Entry(root)
entry_days.pack()

label_weight_tracking = tk.Label(root, text="Enter today's weight (kg):")
label_weight_tracking.pack()
entry_weight_tracking = tk.Entry(root)
entry_weight_tracking.pack()

button_track_weight = tk.Button(root, text="Track Weight", command=start_weight_tracking)
button_track_weight.pack()

root.mainloop()



#Program to create a GUI  using Tkinter (Calculator)
import tkinter as tk

# Function to perform calculations
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result.set(num1 + num2)
    except ValueError:
        result.set("Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields
label_num1 = tk.Label(root, text="Enter number 1:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter number 2:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Create a button to perform the calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Create a label to display the result
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()

# Start the Tkinter main loop
root.mainloop()

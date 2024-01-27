import tkinter as tk
import networkx as nx





window = tk.Tk()
window.title("Academic Program Analyzer")

course_label = tk.Label(window, text="Course:")
course_label.pack()

#course_entry = tk.Entry(window)
#course_entry.pack()

prerequisite_label = tk.Label(window, text="Prerequisites (comma-separated):")
prerequisite_label.pack()

prerequisite_entry = tk.Entry(window)
prerequisite_entry.pack()

add_button = tk.Button(window, text="Add Course")
add_button.pack()

canvas = tk.Canvas(window, width=300, height=10)
canvas.pack()

# Draw a line directly without clicking a button
canvas.create_line(1, 5, 299, 5, width=2, fill="red")

checkbox = tk.Checkbutton(window, text="Check me!")
checkbox.pack()

# Add radio buttons
radio_var = tk.StringVar()
radio_var.set("Option 1")  # Set initial value to "Option 1"
radio_button1 = tk.Radiobutton(window, text="Option 1", variable=radio_var, value="Option 1")
radio_button2 = tk.Radiobutton(window, text="Option 2", variable=radio_var, value="Option 2")
radio_button1.pack()
radio_button2.pack()

result_label = tk.Label(window)
result_label.pack()

window.mainloop()
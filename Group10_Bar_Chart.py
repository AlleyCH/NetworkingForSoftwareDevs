import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def update_chart():
    value = float(value_entry.get())
    axis_name = axis_name_entry.get()
    bar_color = color_entry.get()
    
    ax.cla()
    ax.bar(axis_name, value, color = bar_color)
    ax.set_xlabel('Player Name')
    ax.set_ylabel('Player Score')
    canvas.draw()

app = tk.Tk()
app.title('Lab08 Group #10 Game Score Bar Chart')

frame = ttk.Frame(app)
frame.pack(padx=10, pady=10)

# Labels and Names for Player Score
value_label = ttk.Label(frame, text='Player Score: ')
value_label.grid(row=0, column=0)
value_entry = ttk.Entry(frame)
value_entry.grid(row=0, column=1)

# Labels and Names for Player Name
axis_name_label = ttk.Label(frame, text='Player Name: ')
axis_name_label.grid(row=1, column=0)
axis_name_entry = ttk.Entry(frame)
axis_name_entry.grid(row=1, column=1)

# Label and color entry for the bar color
color_label = ttk.Label(frame, text = 'Bar Color: ')
color_label.grid(row=2, column=0)
color_entry = ttk.Entry(frame)
color_entry.grid(row=2, column=1)

# Button that updates the chart with entered information
update_button = ttk.Button(frame, text='Update Chart', command=update_chart)
update_button.grid(row=3, columnspan=2)

# Creates the default bar chart without entering any info
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=app)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

# Default Values just to get the chart created
value_entry.insert(0, '5.0')
axis_name_entry.insert(0, 'X')
color_entry.insert(0, "blue") 

# Updates the chart with the default values
update_chart()

app.mainloop()

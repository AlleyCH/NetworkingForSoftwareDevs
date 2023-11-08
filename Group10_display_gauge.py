import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msgbox

def update_gauge_and_name():
    # Handle the error if the user tries to enter a score above 5000
    try:
        score = float(score_entry.get())
        if score < 0 or score > 5000:
            raise ValueError('Score must be between 0 and 5000')
        
        percentage = score / 5000  # I arbitrarily set the max value to 5000 
        gauge.set(percentage)
        draw_gauge(percentage)
    
        player_name = player_name_entry.get()
        player_name_label.config(text='Player: ' + player_name)
        
    except ValueError as e:
        msgbox.showerror('Invalid Value', str(e))

app = tk.Tk()
app.title('Group 10 Circular Gauge')

frame = ttk.Frame(app)
frame.pack(padx=10, pady=10)

# Label and text field for Player Name
player_name_label = ttk.Label(frame, text='Player Name: ')
player_name_label.grid(row=0, column=0, columnspan=2)
player_name_entry = ttk.Entry(frame)
player_name_entry.grid(row=1, column=0, columnspan=2)

# # Label and display for Score 
score_display_label = ttk.Label(frame, text='Player Score: ')
score_display_label.grid(row=3, column=0, columnspan=2)

# Label and text field for Score
score_label = ttk.Label(frame, text='Player Score: ')
score_label.grid(row=2, column=0, columnspan=2)
score_entry = ttk.Entry(frame)
score_entry.grid(row=4, column=0, columnspan=2)

# Create the gauge itself
canvas = tk.Canvas(frame, width=200, height=200)
canvas.grid(row=6, columnspan=2)

def draw_gauge(percentage):
    canvas.delete('gauge')  # Clear the previous gauge 
    size = 180
    start_angle = -90  # Start the gauge at the top
    
    # if I make the extent a full 360 it vanishes
    extent = 359.99 * percentage
    
    # Draw the magenta circle (maximum value) first so we can display the maximum potential
    # of the gauge, kind of like an outline
    canvas.create_oval(10, 10, size, size, outline='magenta', width=15, tags='gauge_max')
    
    # The actual gauge that will display the value
    canvas.create_arc(10, 10, size, size, start=start_angle, extent=extent, style=tk.ARC, outline='blue', width=10, tags='gauge')
    
    # Display the score entered
    score_display = round(percentage * 5000)  # Actual value on the gauge
    score_display_label.config(text=str(score_display))

# Update button for the name, score, and gauge
update_button = ttk.Button(frame, text='Update Gauge', command=update_gauge_and_name)
update_button.grid(row=7, columnspan=2)

# Default values for the fields with a hint regarding score
score_entry.insert(0, 'Maximum: 5000') 
player_name_entry.insert(0, 'Player 1')

# Update the gauge, player name, and value display with default values
gauge = tk.DoubleVar()
gauge.set(1.0)  # fills the gauge initially
draw_gauge(gauge.get())

app.mainloop()

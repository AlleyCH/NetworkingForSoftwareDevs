#Lab 10
import random
import numpy as np
import tkinter as ttk
import time
import threading

# Class
class DynamicChart(ttk.Tk):
# Constructor
    def __init__(self, num_vals=20, range_start=0, range_end=5000):
        super().__init__()
        self.num_vals = num_vals
        self.range_start = range_start
        self.range_end = range_end
        self.historical_data = self.data_in_range()
        self.initUI()
    
    def generate_historical_data(self):
        def growth(series):
            m = (random.random() - 0.5) * 2
            return series * m

        def oscillation(i):
            delta = random.random() - 0.5
            coeff = random.randint(1, 10)
            return i + (coeff * delta)

        series = growth(np.array(range(self.num_vals)))
        series = np.array([oscillation(i) for i in series])
        # Scale it down to the mean of 0.5 and std of 1:
        return ((series - series.mean()) / (series.max() - series.min())) + 0.5

    def data_in_range(self):
        return (self.range_end - self.range_start) * self.generate_historical_data() + self.range_start
    

    def update_data_thread(self):
        while True:
            self.generate_historical_data.pop(0)
            new_value = random.uniform(self.range_start, self.range_end)
            self.generate_historical_data.append(new_value)
            self.generate_historical_data.draw_line()
            time.sleep(0.5)

# InitUI Method
    def initUI(self):
        self.title('Dynamic Display')
        self.geometry('400x400')

        # Create canvas for drawing rectangles and lines
        self.canvas = ttk.Canvas(self, width=400, height=300)
        self.canvas.grid(column=0, row=2, columnspan=3, pady=20)

        # Data range entry and button
        self.data_range = ttk.IntVar()
      #  ttk.Label(self, text='Data range:').grid(column=0, row=0, padx=10)
       # ttk.Entry(self, textvariable=self.data_range).grid(column=1, row=0, padx=10)
         # Create and start the thread

                # Created thread 
        self.update_thread = threading.Thread(target=self.update_data_thread)
                # set deamon to true
        self.update_thread.daemon = True
                # started thread
        self.update_thread.start()
        
        data_range = self.data_range.get()
        self.draw_line(data_range)

        # Button click handler
        def on_go_button_click():
            print(self.historical_data)
            self.canvas.delete('all')
            #data_range = self.data_range.get()
            #self.draw_rectangles(data_range)
            
           # data_range_label = ttk.Label(self,
                                         #text=f'Data range: {self.data_range.get()}-{self.data_range.get() + 5}')
           # data_range_label.grid(column=0, row=1)
            self.draw_line(self.data_range.get())

        # Create the "Go" button
        ttk.Button(self, text='Go', command=on_go_button_click).grid(column=2, row=0, padx=10)

# Draw Rectangles and Lines
    def draw_line(self, data_range):
        x_coord = 20  # Adjust this value for proper positioning
        old_x_coord = 0
        old_y2 = 0
        rect_thickness = 55
        rect_spacing = 5
        line_spacing = 8
        height = 300
        range_values = self.historical_data[data_range:data_range + 6]  # Get 6 values from historical_data

        canvas = self.canvas
        canvas.delete('all')

        for x, y in enumerate(range_values):
            x1 = x_coord
            x2 = x_coord + rect_thickness
            y1 = height
            y2 = y1 - (y * 200)  # Scale the value to fit the canvas
           # canvas.create_rectangle(x1, y1, x2, y2, fill='blue', outline='black')
            if x != 0:
                canvas.create_line(old_x_coord + line_spacing, old_y2,
                                x2 - ((rect_spacing + rect_thickness) / 2), y2,
                                fill='red', width=2)
            x_coord += rect_thickness + rect_spacing
            old_x_coord = x_coord - rect_thickness + rect_spacing
            old_y2 = y2

        

if __name__ == '__main__':
    app = DynamicChart(20, 0, 1)
    app.mainloop()
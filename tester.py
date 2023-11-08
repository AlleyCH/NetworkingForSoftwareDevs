import random
import numpy as np
import tkinter as ttk

# Class
class DisplayChart(ttk.Tk):
# Contructor
    def __init__(self, num_vals=10, range_start=0, range_end=1):
        super().__init__()
        self.num_vals = num_vals
        self.range_start = range_start
        self.range_end = range_end
        self.historical_data = self.data_in_range()
        self.initUI()

    def __gen_points(self):
        def growth(series):
            m = (random.random() - 0.5) * 2
            return series * m

        def oscillation(i):
            delta = random.random() - 0.5
            coeff = random.randint(1, 10)
            return i + (coeff * delta)

        series = growth(np.array(range(self.num_vals)))
        series = np.array([oscillation(i) for i in series])
        # scale it down to the mean of 0.5 and std of 1:
        return ((series - series.mean()) / (series.max() - series.min())) + 0.5

    def data_in_range(self):
        return (self.range_end - self.range_start) * self.__gen_points() + self.range_start


#InitUI Method
    def initUI(self):
        # Window properties
        app = ttk.Tk()
        frame = ttk.Frame(app)
        frame.pack(padx=10, pady=30)
        app.title('Historical Data')
        # Grid
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=3)
        self.columnconfigure(3, weight=3)
        # Variables
        self.data_range = ttk.IntVar()
        # Canvas
        #canvas = self.canvas
        canvas = ttk.Canvas(width=200, height=200)
        canvas.grid(column=1, row=3, pady=75)

# Button Handler
        def go():
            print(self.historical_data)
            canvas.delete('all')
            self.data_range_label.destroy()
            self.data_range_label = ttk.Label(self,
                                              text=f'Data rangeeeeeeeee: {self.data_range.get()}-{self.data_range.get() + 5}')
            self.data_range_label.grid(column=0, row=1)
            draw_rectangles(self.data_range.get())

# Draw Rectangles and Line
        def draw_rectangles(data_range):
            data_range = self.data_range.get()  # no use right now
            x_coord = 0
            old_x_coord = 0
            old_y2 = 0
            rect_thickness = 30
            rect_spacing = 5
            line_spacing = 8 
            canvas = ttk.Canvas(width=400, height=250)
            canvas.grid(column=1, row=3, pady=75)
            index = self.data_range.get()
            height = 300
            range = self.historical_data[index:index + 5]
            # rescale the range to fit within the box nicely
            range = range * (0.8 * height) / max(range)
            for x, y in enumerate(range):
                x1 = x_coord
                x2 = x_coord + rect_thickness
                y1 = height
                y2 = y1 - y
                canvas.create_rectangle(x1, y1, x2, y2, fill='blue', outline='black')
                if (x != 0):
                    canvas.create_line(old_x_coord + line_spacing, old_y2,
                                               x2 - ((rect_spacing + rect_thickness) / 2), y2,
                                               fill='red', width=2)
                x_coord += rect_thickness + rect_spacing
                old_x_coord = x_coord - rect_thickness + rect_spacing
                old_y2 = y2

        # Labels
        self.data_range_entrylabel = ttk.Label(self, text='Data range: ')
        self.data_range_label = ttk.Label(self, text=f'Data range: {self.data_range.get()}-{self.data_range.get() + 5}')
        self.data_range_entrylabel.grid(column=0, row=0, padx=25)
        self.data_range_label.grid(column=0, row=1)
        # Entry
        self.data_range_entry = ttk.Entry(self, textvariable=self.data_range)
        self.data_range_entry.grid(column=1, row=0, padx=50)
        # Button
        self.data_range_button = ttk.Button(self, text='Go', width=20,
                                            command=go)  # No you dont put () after the Go method
        self.data_range_button.grid(column=2, row=0)


if __name__ == "__main__":
    valuesList = []
    app = DisplayChart(11, 0, 20)
    app.mainloop()
# Alley Chaggar 
# Date: 2023/10/01

import tkinter as tk           #using an alias for tkinter, also only using tkinter
from tkinter import ttk
from tkinter import messagebox

class CentennialCollege(tk.Tk):

    def widgetContainer(self):

        frame = tk.Frame(self, width=400, padx=5, pady=10, relief='groove', bg='light green')
        frame.pack(padx=5, pady=10, fill='both', expand=True)

# Adjusts to the window (Resizing)
        for i in range(6):
            frame.grid_rowconfigure(i, weight=1)
            frame.grid_columnconfigure(i, weight=1)

        tk.Label(frame, text='ICET Student Survey', bg='light green', font=('Arial italic', 16, 'bold')).grid(row=0, columnspan=3, sticky='nsew')

        tk.Label(frame, text='Full name:            ', bg='light green').grid(row=1, column=0)
        self.full_name = tk.Entry(frame)
        self.full_name.grid(row=1, column=1, columnspan=2, sticky='ew')

#Radiobutton
        tk.Label(frame, text='Residency:            ', bg='light green').grid(row=2, column=0)
        self.residency = tk.StringVar()
        tk.Radiobutton(frame, text='Domestic', variable=self.residency, value='dom', bg='light green').grid(row=2, column=1, sticky='w')
        tk.Radiobutton(frame, text='International', variable=self.residency, value='intl', bg='light green').grid(row=3, column=1, sticky='w')

#Combobox
        tk.Label(frame, text='Program:            ', bg='light green').grid(row=4, column=0)
        self.program = ttk.Combobox(frame, values=['AI', 'Gaming', 'Health', 'Software'], state='readonly')
        self.program.grid(row=4, column=1, columnspan=2, sticky='ew')

        tk.Label(frame, text='Courses:            ', bg='light green').grid(row=5, column=0)
        self.course_vars = []
        row = 5
        for course, value in [('Programming I', 'COMP100'), ('Web Page Design', 'COMP213'), ('Software Engineering', 'COMP120')]:
            var = tk.StringVar()
            chk = tk.Checkbutton(frame, text=course, variable=var, onvalue=value, offvalue='', bg='light green')
            chk.grid(row=row, column=1, sticky='w')
            row += 1
            self.course_vars.append(var)

#Buttons
        tk.Button(frame, text='Ok', command=self.show_info, width=15).grid(row=row,column=0, padx=3, pady=5)
        tk.Button(frame, text='Reset', command=self.reset_form, width=15).grid(row=row, column=1,  padx=3, pady=5)
        tk.Button(frame, text='Exit', command=self.quit, width=15).grid(row=row, column=2, padx=3, pady=5) 

    def show_info(self):
        info = f"Full Name: {self.full_name.get()}\n"
        info += f"Residency: {self.residency.get()}\n"
        info += f"Program: {self.program.get()}\n"
        info += 'Courses: '
        for var in self.course_vars:
            if var.get():
                info += f"{var.get()}\n"
        messagebox.showinfo('Form Info', info)

    def reset_form(self):
        self.full_name.delete(0, 'end')
        self.full_name.insert(0, 'Narendra Pershad')
        self.residency.set('dom')
        self.program.set('Health')
        for var in self.course_vars:
            var.set('')

    def __init__(self): # toString method
        super().__init__()
        self.title('Centennial College')
        self.geometry('450x300')
        self.configure(bg='light green')
        self.widgetContainer()
        self.reset_form()

if __name__ == '__main__':
    app = CentennialCollege()
    app.mainloop()
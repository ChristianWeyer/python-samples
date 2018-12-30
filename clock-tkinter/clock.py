import tkinter as tk    
import time

class Clock:
    def __init__(self):
        self.current_time = time.strftime('%H:%M:%S')

        self.clockFrame = tk.Frame()
        self.clockFrame.pack(side = tk.TOP, expand = tk.YES, fill = tk.X)

        self.clock = tk.Label(self.clockFrame, text = self.current_time, font = ('arial', 48, 'bold'))
        self.clock.pack()

        self.updateClock()

    def updateClock(self): 
        self.current_time = time.strftime('%H:%M:%S')

        self.clock.configure(text = self.current_time)
        self.clockFrame.after(200, self.updateClock)

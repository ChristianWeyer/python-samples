import time
import tkinter as tk

from clock import *

root = tk.Tk()

myClock = Clock()

#interesting fullscreen hack: https://stackoverflow.com/a/42173885
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen', True)

root.mainloop()
import os
from tkinter import *

# Destructure functions from functions about, read ....
from functions import about


# Clean the console
os.system("clear")


def exit():
    root.destroy()


root = Tk()
root.title("Movies project")
root.resizable(0, 0)
root.geometry("500x300")

FrameActions = LabelFrame(root, text=" Actions ", bd=2)
FrameActions.pack(fill='x', side='bottom', padx=10, pady=10, )

buttonAbout = Button(FrameActions, text="About",
                     foreground='blue', command=about.about)
buttonAbout.grid(row=0, column=0, padx=10, pady=10)

buttonExit = Button(FrameActions, text="Exit",
                    foreground='#FF220C', command=exit)

buttonExit.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()

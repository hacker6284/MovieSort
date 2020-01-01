from tkinter import *
import tkinter.ttk as ttk


window = Tk()

window.title("Welcome to the Movie Sort app")
lbl = Label(window, text="Movie Sort", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)

window.geometry('450x300')

btn = Button(window, text="This One", bg="orange", fg="black",
             width=70, height=105)
btn.grid(column=0, row=1)

window.mainloop()

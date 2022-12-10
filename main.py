from tkinter import *
from lib import logic

root = Tk()

root.geometry('400x450')
root.title('Calculator')
root.eval("tk::PlaceWindow . center")

emptyElm = Label(root, text='                           ').grid(row=0, column=0)

title = Label(root, text="Calculator", font=('Arial', 19)).grid(row=0, column=1)

inputEnt = Entry(root, font=('Arial', 18)).grid(row=1, column=1)



root.mainloop()
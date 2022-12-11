from tkinter import *
from lib import logic

root = Tk()

root.geometry('360x266')
root.title('Calculator')
root.eval("tk::PlaceWindow . center")

# emptyElm = Label(root, text='                           ').grid(row=0, column=0)

title = Label(root, text="Calculator", font=('Arial', 19)).grid(row=0, column=0)

inputEnt = Entry(root, font=('Arial', 18), width=27).grid(row=1, column=0)

# num pad
oneBtn = Button(root, text="1", font=('Arial', 18), width=6).place(x=0, y=80)
twoBtn = Button(root, text="2", font=('Arial', 18), width=6).place(x=93, y=80)
threeBtn = Button(root, text="3", font=('Arial', 18), width=6).place(x=186, y=80)
muliplyBtn = Button(root, text="*", font=('Arial', 18), width=5).place(x=279, y=80)

fourBtn = Button(root, text="4", font=('Arial', 18), width=6).place(x=0, y=126)
fiveBtn = Button(root, text="5", font=('Arial', 18), width=6).place(x=93, y=126)
SixBtn = Button(root, text="6", font=('Arial', 18), width=6).place(x=186, y=126)
subtractBtn = Button(root, text="-", font=('Arial', 18), width=5).place(x=279, y=126)

sevenBtn = Button(root, text="7", font=('Arial', 18), width=6).place(x=0, y=172)
eightBtn = Button(root, text="8", font=('Arial', 18), width=6).place(x=93, y=172)
nineBtn = Button(root, text="9", font=('Arial', 18), width=6).place(x=186, y=172)
addBtn = Button(root, text="+", font=('Arial', 18), width=5).place(x=279, y=172)

pointBtn = Button(root, text=".", font=('Arial', 18), width=6).place(x=0, y=218)
zeroBtn = Button(root, text="0", font=('Arial', 18), width=6).place(x=93, y=218)
divideBtn = Button(root, text="/", font=('Arial', 18), width=6).place(x=186, y=218)
equalsToBtn = Button(root, text="=", font=('Arial', 18), width=5).place(x=279, y=218)



root.mainloop()
from tkinter import *

root = Tk()
root.geometry('300x300')

input_text = StringVar()

inputField =  Entry(root, textvariable=input_text, width=20)

inputField.grid(row=0, column=0)

def testing_stuffs():
    value = inputField.get()
    printedText = Label(root, text=value)
    printedText.grid(row=2, column=1)

button = Button(root, text='Click Me', command=testing_stuffs)

button.grid(row=1, column=1)

root.mainloop()
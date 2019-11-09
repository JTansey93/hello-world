import tkinter

root = tkinter.Tk()

def printname(event):
    label1 = tkinter.Label(bottomFrame, text='Sup home dog it\'s me')
    label1.pack(side='left')

def donothing():
    pass

mymenu = tkinter.Menu(root)
root.config(menu=mymenu)

submenu = tkinter.Menu(mymenu)
mymenu.add_cascade(label='File', menu=submenu)
submenu.add_command(label='Not another button', command='donothing')

topFrame = tkinter.Frame(root)
topFrame.pack(side='top')
middleFrame = tkinter.Frame(root)
middleFrame.pack(side='top')
bottomFrame = tkinter.Frame(root)
bottomFrame.pack(side='bottom')


HelloWorld = tkinter.Label(topFrame, text='Hello World')
button1 = tkinter.Button(middleFrame, text='Click me plz', fg='red')
button2 = tkinter.Button(middleFrame, text='I\'m serious', fg='blue')
button3 = tkinter.Button(bottomFrame, text='Click me now', fg='green')
button4 = tkinter.Button(bottomFrame, text='Or else', fg='purple')

button1.bind('<Button-1>', printname)

HelloWorld.pack(side='top')
button1.pack(side='left')
button2.pack(side='left')
button3.pack(side='left')
button4.pack(side='left')

root.mainloop()
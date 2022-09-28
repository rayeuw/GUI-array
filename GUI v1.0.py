# First GUI
# Copied and ajusted according from Mr Pingetts code.
# Author Bob He
# Base Version 1.0
from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lb11=Label(win, text='First number')
        self.lb12=Label(win, text='Second number')
        self.lb13=Label(win,text='Result')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.btn1 = Button(win, text='Add')
        self.btn2=Button(win, text='Subtract')
        self.lb11.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lb12.place(x=100, y=100)
        self.t2.place(x=200, y=100)

        self.b1=Button(win, text='Add', command=self.add)
        self.b1.place(x=100, y=150)

        self.b2=Button(win, text='Subtract', command= self.subtract)
        self.b2.place(x=200, y=150)

        self.lb13.place(x=100, y=200)
        self.t3.place(x=200, y=200)

    def add(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END, str(result))

    def subtract(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))

window=Tk()
mywin=MyWindow(window)
window.title('Hello Python')
window.geometry("400x300")
window.mainloop()
    
                

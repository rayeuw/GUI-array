# First GUI
# Copied and ajusted according from Mr Pingetts code.
# Author Bob He
# Base Version 1.0
from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lb11=Label(win, text='Number of terms')
        self.lb12=Label(win, text='First term')
        self.lb13=Label(win, text='Common Ratio')
        self.lb14=Label(win, text='Common difference')
        self.lb15=Label(win, text='result')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.t4=Entry()
        self.t5=Entry()
        self.btn1 = Button(win, text='Geometric')
        self.btn2=Button(win, text='Arithmetic')
        self.lb11.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lb12.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.lb13.place(x=100, y=30)
        self.t3.place(x=200, y=30)
        self.lb14.place(x=100, y=75)
        self.t4.place(x=200, y=75)

        self.b1=Button(win, text='Geometric', command=self.add)
        self.b1.place(x=100, y=150)

        self.b2=Button(win, text='Arithmetic', command= self.subtract)
        self.b2.place(x=200, y=150)

        self.lb15.place(x=100, y=200)
        self.t5.place(x=200, y=200)

    def add(self): #Geometric
        self.t5.delete(0, 'end')
        n=int(self.t1.get())
        a=int(self.t2.get())
        r=int(self.t3.get())
        result= a*(1-r**n)/(1-r)
        self.t5.insert(END, str(result))

    def subtract(self): #Arithmetic
        self.t5.delete(0, 'end')
        n=int(self.t1.get())
        a=int(self.t2.get())
        d=int(self.t4.get())
        result= (n/2)*(2*a+(n-1)*d)
        self.t5.insert(END, str(result))

window=Tk()
mywin=MyWindow(window)
window.title('Hello Python')
window.geometry("400x300")
window.mainloop()
    
                
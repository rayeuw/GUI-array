# First GUI
# Copied and ajusted according from Mr Pingetts code.
# Author Bob He
# Base Version 4.0
# Modifications : excemptions 
from tkinter import *
class MyWindow:
    def __init__(self, win,):
        self.label = Label(win, text='Welcome to the geometric and arithmetic calculator', bg='blue', fg='white')
        self.label.pack()
        self.lb11=Label(win, text='Number of terms')
        self.lb12=Label(win, text='First term')
        self.lb13=Label(win, text='Common Ratio')
        self.lb14=Label(win, text='Common difference')
        self.lb15=Label(win, text='result')
        self.t1=Entry()
        self.t2=Entry()
        self.t3=Entry()
        self.t4=Entry()
        self.t5=Entry(bd=3)
        self.btn1 = Button(win, text='Geometric')
        self.btn2=Button(win, text='Arithmetic')
        self.btn3 = Button(win, text='Clear')
        self.btn4 = Button(win, text='Exit')
        self.btn5 = Button(win, text='Try again')
        self.lb11.place(x=70, y=25)
        self.t1.place(x=200, y=25)
        self.lb12.place(x=70, y=50)
        self.t2.place(x=200, y=50)
        self.lb13.place(x=70, y=75)
        self.t3.place(x=200, y=75)
        self.lb14.place(x=70, y=100)
        self.t4.place(x=200, y=100)
        self.lb15.place(x=70, y=200)
        self.t5.place(x=200, y=200)

        self.b1=Button(win, text='Geometric', command=self.Geometric)
        self.b1.place(x=100, y=150)

        self.b2=Button(win, text='Arithmetic', command= self.Arithmetic)
        self.b2.place(x=200, y=150)

        self.b3=Button(win, text='Clear', command = self.Clear)
        self.b3.place (x=125,y=250)

        self.b4=Button(win, text='Exit', command=window.destroy)
        self.b4.place (x=250, y=250)



    def Geometric(self): #Geometric
        self.t5.delete(0, 'end')
        n=int(self.t1.get())
        a=float(self.t2.get())
        r=float(self.t3.get())
        if r == 1:
            root = Tk()
            MyError = Errorcode(root)
            root.mainloop()
        result= a*(1-r**n)/(1-r)
        self.t5.insert(END, str(result))

    def Arithmetic(self): #Arithmetic
        self.t5.delete(0, 'end')
        n=int(self.t1.get())
        a=float(self.t2.get())
        d=float(self.t4.get())
        result= (n/2)*(2*a+(n-1)*d)
        self.t5.insert(END, str(result))

    def Clear(self):
        self.t1.delete(0,'end')
        self.t2.delete(0,'end')
        self.t3.delete(0,'end')
        self.t4.delete(0,'end')
        self.t5.delete(0,'end')

class Errorcode:
    def __init__(self, top):
        top.title("Error!")
        msg = Message(top, text='Error! Please enter a valid number', bg='red', fg='white')
        msg.pack()
        button = Button(top, text="Dismiss", command=top.destroy)
        button.pack()
        top.geometry("200x150")





window=Tk()
mywin=MyWindow(window)
window.title('Geometric and Arithmetic Calculator')
window.geometry("400x300")
window.mainloop()
    
                

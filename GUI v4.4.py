# First GUI By Bob He
# Program designed to calculate the sum of either a geometric or arithmetic series
# Copied and ajusted according from Mr Pingetts code.
# Author Bob He
# Base Version 4.4
# Date 10/8/19
# Modifications : Extra text for instructions
#-----------------------------------------------------------------------------------------------------------------------------------#
from tkinter import *
class MyWindow:
    def __init__(self, win,):
        self.label = Label(win, text='Welcome to the geometric and arithmetic calculator', bg='blue', fg='white', font='times')
        self.label.pack()
        self.label2 = Label(win, text='''Please note that:
        \nCommon ratio is only needed for geometric series
        \nWhereas common difference is only needed for arithemetic series
        ''')
        self.label2.place (x=10, y=300)
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
        
        while True:
            try:
                n=int(self.t1.get())
                if n<=1:
                    root = Tk()
                    MyError = Errorcode(root)
                    root.mainloop()
                break
            except ValueError:
                root = Tk()
                MyError = Errorcode(root)
                root.mainloop()
                
        while True:
            try:
                a=float(self.t2.get())
                break
            except ValueError:
                root = Tk()
                MyError = Errorcode(root)
                root.mainloop()
                
        while True:
            try:
                r=float(self.t3.get())
                if r == 1 or r ==0:
                    root = Tk()
                    MyError = Errorcode(root)
                    root.mainloop()
                break
            except ValueError:
                root = Tk()
                MyError = Errorcode(root)
                root.mainloop()
            
        result= a*(1-r**n)/(1-r)
        self.t5.insert(END, str(result))

    def Arithmetic(self): #Arithmetic
        self.t5.delete(0, 'end')
        
        while True:
            try:
                n=int(self.t1.get())
                if n<=1:
                    root = Tk()
                    MyError = Errorcode(root)
                    root.mainloop()
                break
            except ValueError:
                root = Tk()
                MyError = Errorcode(root)
                root.mainloop()
                
        while True:
            try:
                a=float(self.t2.get())
                break
            except ValueError:
                root = Tk()
                MyError = Errorcode(root)
                root.mainloop()
                
        while True:
            try:
                d=float(self.t4.get())
                if d==0:
                    root = Tk()
                    MyError = Errorcode(root)
                    root.mainloop()
                break
            except ValueError:
                root = Tk()
                MyError = Errorcode(root)
                root.mainloop()
                
        result= (n/2)*(2*a+(n-1)*d)
        self.t5.insert(END, str(result))

    def Clear(self):
        self.t1.delete(0,'end')
        self.t2.delete(0,'end')
        self.t3.delete(0,'end')
        self.t4.delete(0,'end')
        self.t5.delete(0,'end')

class Errorcode: #The thing that pops up when there is an error/excemption
    def __init__(self, top):
        top.title("Error!")
        msg = Message(top, text='Error! Please enter a valid number', bg='red', fg='black', font='TkfixedFont')
        msg.pack()
        button = Button(top, text="Dismiss", command=top.destroy)
        button.pack()
        top.geometry("200x100")


window=Tk()
mywin=MyWindow(window)
window.title('Geometric and Arithmetic Calculator')
window.geometry("400x400")
window.mainloop()
    
                

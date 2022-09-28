#This program is designed to calculate the arithemtic and geometric sums
#Author : Bob He
#Date 31/07/2019
#Version 3 - exception of values

def main():
    keep = 1
    while keep ==1:
        Arithemticsum = 0
        Geometricsum = 0
        while True:
            try:
                option = int(input("Please enter 1 for geometric, 2 for arithmetic: "))
                if option != 1 and option != 2:
                    error = ValueError
                    raise error
                break
            except ValueError:
                print ("Please enter 1 OR 2")
        if option == 1:
            Geometric()
        elif option == 2:
            Arithmetic()
        while True:
            try:
                keep = int(input("Please enter 1 to CONTINUE or any other number to EXIT: "))
                break
            except ValueError:
                print ("ERROR!!!!! Please ONLY enter 1 to CONTINUE or any other number to EXIT")
                


def Geometric():
    print ("This is the geometric calculator")
    while True:
        try:
            n = int(input("Please enter the number of terms: "))
            if n<1:
                error = ValueError
                raise error
            break
        except ValueError:
            print ("Please enter vaild interger greater than 0")
    while True:
        try:
            a = float(input("Please enter the first term: "))
            break
        except ValueError:
            print ("Please enter vaild number")
    while True:
        try:
            r = float(input("Please enter the Common ratio: "))
            if r == 1 and r== 0:
                error = ValueError
                raise error
            break
        except ValueError:
            print ("please enter valid number, and the common ratio cannot be 1")
    Geometricsum = a*(1-r**n)/(1-r)
    print ("The geometric series is: ", Geometricsum )

def Arithmetic():
    print ("This is the Arithemtic calculator")
    while True:
        try:
            n = int(input("Please enter the number of terms: "))
            if n<1:
                error = ValueError
                raise error
            break
        except ValueError:
            print ("Please enter vaild number")
    while True:
        try:
            a = float(input("Please enter the first term: "))
            break
        except ValueError:
            print ("Please enter vaild number")
    while True:
        try:
            d = float(input("Please enter the difference: "))
            if d==0 :
                error = ValueError
                raise error
            break
        except ValueError:
            print ("please enter valid number")
    Arithemticsum = (n/2)*(2*a+(n-1)*d)
    print ("The sum of the Arithemtic series is: ", Arithemticsum )

main()


        
            

    

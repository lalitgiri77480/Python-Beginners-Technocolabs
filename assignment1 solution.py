


# assignment :1

#1. write a programe of python for taking two inputs from user and perform
# addition, substraction, multiplication,and divide operation on the input

a=int(input("Enter  a First Number "))
b=int(input("Enter  a Second Number"))
c=input("so what you want ? '+', '-'  '*', '/'  ")
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c == '/':
    print(a / b)


######################-********************###############################


#2. Write a programe to check given input is integer or not.

a=input("enter a number ")
if (a.isdigit()):print("yes, it is integer")
else: print(" No , it is not integer")

###################-**********************###############################


#3.
#Write a programme to check given input is the list item or not.

l=["lalit","giri", "ram"]

a=input("enter a name you want to be a search")
if a in l:
    print("yes, it is exist")
else:
     print("no, it is not exist")

###################-************************################################

#4.
# Write a program for taking the value from user in list such as your name, class,
# roll no, college name, Branch and to print all of this value in one line print function
a=input("Enter your Name")
b=input("Enter your Class")
c=input("Enter your RollNo.")
d=input("Enter your Collage Name")
e=input("Enter your Branch")
print("Name=",a, "Class=",b, "RollNo.=",c, "Collage Name=",d, "Branch=",e)

# another option we have to print all data in one line by using f string
#print(f"Name={a}    Class={b}      RollNo.={c}     Collage Name={d}    Branch={e}


############ Assignment 1 completing ############
##################-***************************###############################
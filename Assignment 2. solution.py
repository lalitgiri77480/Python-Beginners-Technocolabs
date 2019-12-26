
#Assignment 2 Solution

#Q1.Factorial of any number n is represented by n! and is equal to 1*2*3*....*(n-1)*n

n=int(input("Enter a number "))
f=1
for i in range(n):
    f=f*(i+1)
print("Factorial is = ",f)


#Q2.Print the following patterns using loop :-
#  1  *
#    ***
#   *****
#    ***
#     *

# 1. Solution
for i in range (5):
    for j in range(5):
        if j==2 or i==2  or ((j==1 or j==3)and i==1) or ((j==1 or j==3) and i==3):
            print("*",end="")
        else:
            print(end=" ")

    print()


############### OR  #####################
a=5
for i in range (1,a+1):
    print(" "*(a-i)+"* "*i)
for i in range (a-1,0,-1):
    print(" " *(a-i) + "* " * i)




# 2.
#     *
#    **
#   ***
#  ****

# 2. Solution
for i in range (4):
    for j in range(4):
        if j==3 or (i==3 and j<3) or ((j==1 or j==2)and i==2) or (i==1 and j==2):
            print("*",end="")
        else:
            print(end=" ")

    print()

###############        OR       ################
#
a=4
for i in range (1,a+1):
    print(" "*(a-i)+"*"*i)



# 3.
#     ******
#       ****
#        **
#         *
#

#3. solution
for i in range (4):
    for j in range(5):
        if j==3 or i==0  or ((j==1 or j==2 or j==4) and i==1)  or (j==2 and i==2):
            print("*",end="")
        else:
            print(end=" ")

    print()

################ OR   ####################


# a=5
for i in range (a-1,0,-1):
     print(" " *(a-i) + "* " * i)



# 4.     ********
#        *****
#        ***
#        **
#        *
#

#4. Solution
for i in range (5):
    for j in range(5):
        if j==0 or ( i==0and j<5) or ((j==1 or j==2)and (i==1 or i==2)) or (j==3 and i==1)or (j==1 and i==3):
            print("*",end="")
        else:
            print(end=" ")

    print()


############### OR ##########################


a=6
for i in range (a-1,0,-1):
    print(""*(a)+"*"*i)


# 5.      ********
#           ******
#             ****
#              ***
#               **
#                *


# 5. solution
for i in range (6):
    for j in range(8):
        if j==7or i==0 or ((i==1 or i==2 or i==3)and (j>4and  j<7)) or ((j==2 or j==3 or j==4 )and i==1) or (j==4 and i==2) or (j==6 and i==4) :
            print("*",end="")
        else:
            print(end=" ")

    print()

###################### OR #################


a=6
for i in range (a-1,0,-1):
    print(" "*(a-i)+"*"*i)







#Q3.Take 10 integers from keyboard using loop and print their average value on the screen.
# 3. Solution
a=0
for i in range (10):

    n=int(input(" enter a  number "))
    a=a+n
print("Average value of is= ", a/2)


#Q4. Write  a Programe for finding Even Number Between 1 to 100.

#4.solution
for i in range (100):
    if (i%2==0):
        print(i,end="  ")



#Q5. Write a Programe For printing A table by User input Number in The following Formate
#        2 x 1=2
# and also calculate the sum of result after the multiplying of table such as:-
#      2 x 1=2
#      2 x 2=4
# then sum is 2+4=6.

# Solution
b=0
for i in range(1,11):
    a = 2 * i
    print(" 2*",i,"=",a)
    b=b+a
print("sum of all multiple is =",b)

#################   Assignment 2. Completed  ##############
#################-**************************-##############
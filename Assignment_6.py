#1. Write a python script to check whether a given number is positive or non-positive
""" n  = int(input("enter a number: "))

print ("positive number" if (n>0) else "negative number") """

#2. Write a python script to check whether a given number is divisible by 5 or not

""" n = int(input("Enter a number: "))

print("Divisible by 5" if (n%5==0) else "Not Divisble by 5")  """

#3. Write a python script to check whether a given number is even or odd

""" 
n = int(input("Enter a number: "))

if (n%2==0):
    print("Even")
else:
    print("Odd") """

#4.  Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.

""" a1 = int(input("Enter 1st number: "))
b1 = int(input("Enter 2nd number: "))

if (a1>b1):
    print("%d is greater"%a1,b1)
elif (b1>a1):
    print("%d is greater"%b1,a1)
else:
    print("You took same number: %d"%a1) """


#5.Write a python script to print two given words in dictionary order
""" 
a = input("enter a first word: ")
b = input("enter a second word: ")

if (a>b):
    print(b)
    print(a)
else:
    print(a)
    print(b)  """


#6. Write a python script to check whether a given number is a three digit number or not.

""" n = int(input("Enter a number: "))

print ("3 Digit number" if (99<n<1000) else "not a 3 digit") """




#7. Write a python script to check whether a given number is positive, negative or zero.

""" n = eval(input("Enter a number: "))

if (n>0):
    print("Positive")
elif (n==0):
    print("Zero")
else:
    print("Negative") """


"""8. Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots"""




#9. Write a python script to check whether a given year is a leap year or not


""" y  = int(input())

if (y%400==0):
    print("leap year")
elif (y%100==0):
    print("not a leap year")
elif (y%4==0):
    print("leap year") """


#10.  . Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.

""" a1 = int(input("Enter 1st number: "))
b1 = int(input("Enter 2nd number: "))
c1 = int(input("Enter 3rd number: "))
if (a1>b1 and a1>c1):
    print("%d is greater"%a1,b1,c1)
elif (b1>a1 and b1>c1):
    print("%d is greater"%b1,a1,c1)
elif (a1==b1==c1):
    print("Same number")
else:
    print("%d is greater "%c1,a1,b1)

 """



#11. Write a python script to take the month value in numeric format and display the number of days in it.

""" n = int(input("Enter Month value: "))

match n:
    case 1:
        print("31 days")
    case 2:
        print("28 days")
    case 3:
        print("31 days")
    case 4:
        print("30 days")
    case 5:
        print("31 days")
    case 6:
        print("30 days")
    case 7:
        print("31 days")
    case 8:
        print("31 days")
    case 9:
        print("30 days")
    case 10:
        print("31 days")
    case 11:
        print("30 days")
    case 12:
        print("31 days")
    case _:
        print("Invalid value")
print("Bye") """



    










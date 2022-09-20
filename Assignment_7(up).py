#1. Write a python script to display the number of days in a given month number.

""" m = int(input("Enter a month (in numeric): "))

match m:
    case m if m in (1,3,5,7,8,10,12):
        print("31 days")
    case m if m in (4,6,9,11):
        print("30 days")
    case 2:
        print("28 or 29 days")
    case _:
        print("Wrong One") """

#2. Write a menu driven program to perform following operations - Addition, Subtraction, Multiplication, Division
""" 
i = 0
while(i<=3):

    n = int(input("Press 1.(+)          Press 2.(-)          Press 3.(x)         Press 4. (/) "))
    a = int(input("Enter 1st no. "))
    b = int(input("Enter 2nd no. "))

    match n:
        case 1:
            sum = a+b
            print(sum)
        case 2:
            sum = a-b
            print(sum)
        case 3:
            sum = a*b
            print(sum)
        case 4:
            sum = a/b
            print(sum)
        case _:
            print("Wrong Input")
    i=i+1 """
    
    
    
    
#3. 



#4. Write a program which takes user’s age and display the category of person. Age below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -Experienced, Age above or equal 60 - Senior Citizen
""" 
age = int(input("enter age: "))

match age:
    case age if age>=60:
        print("Senior Citizen")
    case age if 40<=age<=60:
        print("Experienced")
    case age if 20<=age<=40:
        print("Young")
    case age if 10<=age<=20:
        print("Teen")
    case age if age<10:
        print("Kid")
    case _:
        print("default")  """

        
"""       case age:
       if age>=60:
            print("Senior")
       elif 40<=age<=60:
            print("Experienced")
       elif 20<=age<=40:
            print("young")
       elif 10<=age<=20:
            print("Teen")
       else:
        print("Kid") """



#5. . Write a program which takes a number from user. Print Saurabh Shukla if the number is even, print Prateek Jain if the number is negative odd number and print AdityaChoudhary if number is positive odd number




""" n = int(input("Enter a number: "))
match n:
    case n:
        if (n%2==0):
            print("Saurabh Shukla")
        elif (n<0):
            print("Prateek Jain")
        else:
            print("Aditya Choudhary") """

#6. Write a python program to check whether a given string is a multiword string or single word string using match case statement

""" s = input("Enter a String: ")

0
match s:
    case s:
        if " " in s:
            print("Muliword")
        else:
            print("Singleword")  """


#7 . Write a python program to check whether a given number is positive, negative or zero using match case statement

""" n = int(input("Enter a number: "))
match n:
    case 0:
        print("Zero")
    case n if n>0:
        print("Positive")
    case n if n<0:
        print("Negative") """


#8. Write a python script to check whether two given strings are identical, first string comes before the second in dictionary order or first string comes after the second string in dictionary order using match case statement

""" s1 = input("Enter a 1st String: ")
s2 = input("Enter a 2nd String: ")

match (s1,s2):
    case (s1,s2) if s1>s2:
        print(s2)
        print(s1)
    case (s1,s2) if s2>s1:
        print(s1)
        print(s2) """

#9. 



"""10. Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday"""




    


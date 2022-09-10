#Importing A1 module instance object

#Type 1 

#import A1


"""
print("Name: "  + A1.name)
print("Age: " ,A1.age)
print("Job: " + A1.Job)

"""








#Type 2
 
#from A1 import *

"""
print("Name" , name)
print("Age: " , age)
print("Job: ",Job)
"""


#Type 3

#only importing "name" var. from A1.py module

from A1 import name

print(name)




#Type 4

#having same variable in both the modules

from A1 import name as Name 

name  = "Ganesh"

print(name)
print(Name)



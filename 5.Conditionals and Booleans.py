#Conditionals(and,or,not) and Booleans(True/1 , False/0)
#Conditonal Operators: and , or , not .

#!Structure : 
#? if condition1:
#*      runs if condition1 is True
#? elif condition2:
#*      runs if condition1 was False AND condition2 is True
#? else:
#*      runs if none of the above conditions are True
  

#Ex1:

age = 18

if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

#Ex2:

username = "tirtha"
password = "1234"

if username == "tirtha" and password == "1234":
    print("Login successful!")
elif username == "tirtha":
    print("Wrong password.")
else:
    print("User not found.")



#! Object identity : variable1 is variable2
#! id(variable) : Returns the loaction,where a variable is stored .

list1=[1,2,3]
list2=[1,2,3]
list3=['Hi','Hello','Bye']
list4=[]

print(list1==list2)         #Prints a true
print(id(list1))            #Prints the memory location of list1      
print(id(list2))            #Prints the memory location of list2 
print(id(list1)==id(list2)) #?Prints a false,cause the memory location is not same though they are same

list4=list3
print(id(list3))            #Prints the memory location of list3      
print(id(list4))            #Prints the memory location of list4
print(id(list3)==id(list4)) #?Prints a true,cause the memory location is same 


 
#!False Values in Python :
#* 1- False,None ,0
#* 2- Any empty sequences : empty strings,list,tuples - '' , [] , ()
#* 3- Any empty dictionary: {}
#? Everything else will be excecuted as true/1



#! --------------------------------------------- -End- --------------------------------------------------



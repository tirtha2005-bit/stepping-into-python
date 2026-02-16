#List: A built-in, ordered and mutable collection of data in python.

name =['Tirtha','Biswas','Joy','Ratul','Saswata','Pritom','Abhisek']
title=['Mr.','Ms.','Mrs.']


#Joining two lists
list1=['Tirtha','Biswas','Joy']     
list2=['Ratul','Saswata','Pritom']
list3=list1+list2 #Joins two lists and stores it in a new list
print(list3) #Prints the joined list    



# Append function - Adds a new item to the list, 1D list
name.append('Sourav')
print(name)


#Insert Function - Add a whole new list to the list ,2D list 
name.insert(2,'Krishna')
name.insert(0,title)
print(name)
print(name[0][0],name[1],name[2])
print(name[0][1],name[3],name[4])
print(name[0][2],name[5],name[6])


#Remove Function - Removes an item from the list
name.remove('Krishna')
print(name)


#name.remove(1)
# Throws an error if the item is not found in the list


#Pop Function - Removes an item from the list based on index,default is the last item
name.pop()
print(name)
a=name.pop(3) #Removes the 3rd index item
print(a) #Prints the removed item from the list
print(name)


#Reverse Function - Reverses the order of the list
b=name.reverse()
print(b) #Prints None
print(name) #Prints the reversed list


#Sort Function - Sorts the list in ascending order
#what is homogeneous and heterogeneous list?
#Homogeneous list - A list with same type of data
#Heterogeneous list - A list with different type of data - comes later

# sort,sorted,max,min,sum

num=[5,3,8,6,7,2,4,1]
num.sort() #Sorts the num list in ascending order
print(num) #Prints the num list in ascending order


name1=['Tirrtha','Biswas','Joy','Ratul','Saswata','Pritom','Abhisek']
name1.sort() #Sorts the name list in alphabitical order
print(name1) #Prints the name list in alphabitical order

name1.sort(reverse=True) #Sorts the name list in reverse alphabitical order
print(name1)
name1.sort(reverse=False) #Sorts the name list in alphabitical order
print(name1)


#sorted funtion- Returns a new sorted list witout changing the original list
#But a new varable is needed to store the sorted list
name1=['Tirrtha','Biswas','Joy','Ratul','Saswata','Pritom','Abhisek']
name2=sorted(name1) #Sorts the name list in alphabitical order and stores it in name2
print(name2) #Prints the name list in alphabitical order
print(name1) #Prints the original name list


#Finding values
print('Tirtha' in name1) #Returns True if the item is found in the list
print('Sourav' in name1) #Returns False if the item is not found in the list

name1.index('Joy') #Returns the index of the item in the list
print(name1.index('Joy')) #Prints the index of the item in the list
#name1.index('Sourav') #Throws an error if the item is not found in the list



#Looping through a List

for item in name1:
  print(item)  #Prints each item in the list

for numbers in num:
  print(numbers) #Prints each item in the list

#Using f string to print the items in the list
for item in name1: 
  print(f'Hello, {item}')  #Prints each item in the list with a greeting



# enumerate function - It returns two values, index and item
# Structure :
#  for a(variable1),b(variable2) in enumerate(list,start=counter):
#      print(a,b)  

# Counter is optional, default is 0
    
#So, two variables needed 


for index,item in enumerate(name1):
   print(index,item) #Prints the index and item in the list,starts from 0 by default

for a,b in enumerate(num,start=5): #Starts from 5
   print(a,b) 


#join function - Joins the items in the list with a specified separator

#Structure:
# separator = ',' or ' - ' or any other character
# variable = separator.join(list)
# print(variable)  
sept1=','
sept2=' - '
joined_name1 = sept1.join(name1)
joined_name2= sept2.join(name1)
print(joined_name1) #Prints the joined list with the specified separator
print(joined_name2)


#End 
#Apology - The output of the whole code might be messy, try to learn it topic-wise


#List Exercises - (collected) 
#Easy
#1. Create a list of your favorite fruits and print them one by one using a loop.
#2. Create a list of numbers and find the maximum and minimum number in the list.

#Medium
#1. Create a list of names and sort them in reverse alphabetical order.
#2. Create a list of numbers and remove all even numbers from the list.

#Hard
#1. Create a list of dictionaries where each dictionary contains information about a person (name, age, city). Sort the list by age.
#2. Create a list of tuples where each tuple contains a student's name and their score. Find the student with the highest score.

#Advanced
#1. Create a list of lists where each inner list contains information about a book (title, author, year). Sort the list by year.
#2. Create a list of sets where each set contains unique tags for a blog post.
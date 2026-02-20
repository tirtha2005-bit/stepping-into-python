# Dictionary ,creation,accessing,updating,deleting elements,methods
# A dictionary is a collection of key-value pairs, where each key is unique and maps to a specific value.

# Structure : 
#! variable name = {'key1':'value1' , 'key2':'value2' , 'key3':'value3',...}

# Example :
my_dict = {'name': 'Tirtha', 'age': 21, 'city': 'Chattogram'}
print(my_dict)



# Accessing elements : variable name['key']

print(my_dict['name'])   # Accessing name using key
print(my_dict['age'])    # Accessing age using key
print(my_dict['city'])   # Accessing city using key

#print(my_dict['number']) #*  Raise an error as the number is not in the dict.


#! To avoid error we can use get() method

print(my_dict.get('name'))                 # Accessing name using key
print(my_dict.get('number'))               #Prints 'None' as the number is not found = default
print(my_dict.get('number', 'Not Found'))  #Prints 'Not Found' as the number is not found
print(my_dict.get('School','Not saved'))   #Prints 'Not saved' as the key-value is not found





#! 1.Updating elements : variable name['key'] = 'new_value'

my_dict['number']= 10000            # Adding new key-value pair
my_dict['age'] =22     
my_dict['college'] = 'HTDC'        # Updating existing key-value pair
print(my_dict)

#! 2.Update method : variable.update({'key1':'value1', 'key2':'value2', ...})
#Update all the elements in one shot
#? Note: Adding list,tuple,set as a value is possible,Done in previous line

my_dict.update({'School':'Cuet School','age':21,'Id':2308031,'friends':['Ram','Ratul','Bipro','Tonmoy','Shanto']})
print(my_dict)


#! 1.Deleting elements : del variable['key']

del my_dict['number']  # Deleting key-value pair using key
print(my_dict)         # Print the updated dictionary


#! 2.pop() method : variable.pop('key') , we need a new variable to store the deleted value
#It removes the specified key and returns the corresponding value.
#But the methode 1 does not return the value,that only deletes the key-value pair

deleted_val = my_dict.pop('college')
print(my_dict)                        # Print the updated dictionary
print('Deleted value = ',deleted_val) # Print the deleted value




#! Important: 
print(my_dict.keys())    #Prints only the keys.
print(my_dict.values())  #Prints only the values.
print(my_dict.items())   #Prints all the key-value pairs.

a=len(my_dict)  #? Returns the length (i.e., the number of key-value pair stored in dict.)
print(a)
print(type(my_dict))  #? Returns the type of the variable (i.e., <class 'dict'>)


#! Looping through a dictionary 

for keys in my_dict: 
    print(keys)           #Prints only the keys

for i,(key,value) in enumerate(my_dict.items(), start=1):   
        print(i,'.',key,' - ',value)      #Prints both keys and values with index 




#! --------------------------------------- End -----------------------------------------




#!Extra : 
# Make the comments to change its color
# Downloaded an extension called "Better Comments",Then

#!        (shows in red)
#?        (shows in blue)
#TODO:    (shows in orange)
#*        (shows in green)
#         (default is green)


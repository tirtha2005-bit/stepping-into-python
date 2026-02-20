# Sets -  Another built-in Data Structure in Python 
# Sets are unordered collections of unique elements
# Sets are mutable, meaning you can add or remove elements after creation

# Sets are defined using curly braces {} or the set() function

# Sets do not allow duplicate values
# Sets do not support indexing or slicing like lists or tuples

# Sets are commonly used for membership testing, removing duplicates from a list, and -
#  performing mathematical set operations like union, intersection, and difference .


# Creating a Set
set1={1,4,2,5,3,6,7,8,9,23,45,67,89,90}
print(set1)                                    # Prints the entire set
# Run the line (15,16) multiple times to see that the order of elements may vary

print(type(set1))                              # Prints the type of the data structure
print(len(set1))                               # Prints the length of the set


# Accessing elements in a set
# Since sets are unordered, you cannot access elements by index
#If we add a duplicate element, it will not be printed again 


set1.add(10)
set1.add(1)
print(set1) 
# Prints the entire set after adding elements
#10 will be added and print,but -
# 1 will be added but not printed again as it was already present in the set


print('Tomuk' in set1)                  # Checks if string 'Tomuk' is in the set and prints True or False
print(20 in set1)                       # Checks if 20 is in the set and prints

# Removing elements from a set
set1.remove(5)          # Removes the element 5 from the set
print(set1)             # Prints the entire set after removing the element

set1.discard(20)        # Tries to remove the element 20 from the set, but does not raise an error if not found
print(set1)             # Prints the entire set after trying to remove the element`
# 20 was not present in the set, so no error is raised and the set remains unchanged`



Subjects={'EEE','ECE','MECHANICAL','CIVIL','ARCHI','AI'}
more_sub ={'ETE','MME','BME','URP','CSE','WRE','EEE','ECE','MECHANICAL','CIVIL','ARCHI'}

# Set Operations : Union, Intersection, Difference

print(more_sub.intersection(Subjects))  # Prints the common elements in both sets
print(Subjects.union(more_sub))         # Prints all unique elements from both sets
print(Subjects.difference(more_sub))    # Prints elements in Subjects that are not in more_sub
print(more_sub.difference(Subjects))    # Prints elements in more_sub that are not

# in Subjects
print(Subjects.symmetric_difference(more_sub))  # Prints elements in either set but not in both
# Looping through a Set
for subject in Subjects:
    print(subject)                   # Prints each item in the set
for a,item in enumerate(Subjects,start=1):
    print(a,item)                   # Prints the index and item in the set   

# Note: The order of elements may vary each time you run the code  

# Converting a List to a Set to remove duplicates
subjects_list=['EEE','ECE','MECHANICAL','CIVIL','ARCHI','AI','EEE','ECE','MECHANICAL']
print(subjects_list)                # Prints the original list with duplicates
subjects_set=set(subjects_list)     # Converts the list to a set to remove duplicates
print(subjects_set)                  # Prints the set with unique elements  
# Note: The order of elements may vary each time you run the code

# End of code
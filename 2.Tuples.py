# Mutable Structure = List
# Lists are mutable, meaning they can be changed after creation
# Lists are defined using square brackets []

# Immutable Structure = Tuple
# Tuples are immutable, meaning they cannot be changed after creation
# Tuples are defined using parentheses () 

# Tuples can't be assigned after creation
# Manupulating functions like reverse(),sort() etc are not available for tuples
# Only Accessing functions like index(),count() are available for tuples



# Creating a Tuple
singers =('Manna dey','Kishore Kumar','Hemanta Mukharjee','Lata Mangeskar','Sonu Nigam','Shreya Ghoshal')

print(singers)                                    # Prints the entire tuple
print(type(singers))                              # Prints the type of the data structure
print(singers[2])                                 # Prints the item at index 2
print(singers[-1])                                # Prints the last item in the tuple
print(singers[1:3])                               # Prints items from index 1 to 2
print(singers[0:4:2])                             # Prints items from index 0,by giving gap of 1
print(singers[::-1])                              # Prints the entire tuple in reverse order





#Reminders of list :
singers1=['Manna dey','Kishore Kumar','Hemanta Mukharjee','Lata Mangeskar','Sonu Nigam','Shreya Ghoshal']
singers1.reverse() 
print(singers1)                              # Prints the entire list in reverse order




tuple(singers1)           # Converts the list to tuple
print(singers1)


#Looping through a Tuple
for singer in singers:
    print(singer)                   # Prints each item in the tuple

for a,item in enumerate(singers,start=1):
    print(a,item)                   # Prints the index and item in the tuple

sept=','                   # Separator
singers3=sept.join(singers)
print(singers3)                     # Prints the entire tuple as a string with ',' in between each item



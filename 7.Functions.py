#  A function is a block of code that performs a specific task.
# You can reuse it whenever needed instead of writing the same code again and again.

#? Defining :
#* def      → tells Python we’re defining a function
#* Any name → function name
#* ()       → parentheses (can hold parameters)
#* :        → starts the function block
#* Then the code block ... 
 
def pray () :           #Without parameters
    print('Hare Krishna,hare krishna,krishna krishna hare hare,hare rama,hare rama,rama rama hare hare.')

pray()  #* The code block will be executed without being rewrote
pray()
pray()
print('\n'*2)


def greet_user(name):    # With parameter
    print("Hello,", name)

greet_user("Tirtha")
greet_user("Tirtha")
print('\n'*2) #prints two of new lines


def add(a, b):            #* With parameters and return values
    return a+b            #* Wrong
    s=a+b                  
    print(s)
add(5,7)

#! In Python (and most programming languages):
#! return means → “give back this value and exit the function immediately.”
#! Once Python hits a return, it stops executing anything else inside that function.
#! Everything after return is ignored

def add(a, b):            #* With parameters and return values
  s=a+b
  print(s)

#? Or def add(a, b):
#?   print(a+b) 

add(70,9)


#! Important :
#* In function only care about the parameters(input) and returned values (output)
#* If the returned value is string, we can apply all the built in funtions of stings on the defined one.
#* If the returned value is integer/float, we can apply all the built in funtions of string/flaot on the defined one.

def word(name):
    return 'Hello '+ name               #? Returns a string
print(word("Tirtha"))
print(word("Tirtha").upper())
print(word("Tirtha").lower())
print(len(word("Tirtha")))

def ward(names):
    return ('Tirtha','Juboraj',names)   #? Returns a tuples

print(ward('Bro'))
for i in range(0,3):
    print(ward('Krishna')[i].upper())
    print(ward('Krishna')[i].lower())
    print(len(ward('Krishna')[i]))




#! Another topic - Positional Arguments - The format method:
#* The format() method in Python is used with strings to insert values into placeholders .
#? {} → placeholder
#? .format() → fills the placeholders

#* Works with position, names, numbers, formatting

text1= 'I am {} and I am {} years old.'
print(text1.format('Tirtha', 20))

text2= 'I am {name} and I am from {district}.'
print(text2.format(name='Tirtha Biswas Joy',district='The mighty Chattogram'))


#! The order of place holders can be controlled by using indexes,index starts from Zero

text3 = 'I am {1},My friend is {0},My father is {3},My mother is {2}.'
print(text3.format('Gae','Tirtha','housewife','strict'))



#! Now apply function on this
 
def info(st1,st2,st3,st4):
    text4 = '{0} is not a green {2},It is a green {1}.It gives us {3}'
    print('\n'*2)
    print(text4.format(st1,st2,st3,st4))
    print('\n'*2)

info("Cuet","hell","Heaven","big big bamboo")



#! Uses of star(*) and double star(**) in positional Argument.
#! It prints the inserted and extra arguments separately.
#! *  - Actual/inserted 
#! ** - Extra

def info(*courses,**extra):
   print(courses)
   print(extra)
info('Math','Physics','Chemistry',name='Tirtha',age='20')                      #* Right 

''' info('Math','Physics','Chemistry',name='Tirtha',age='20','Finance')  '''   #* Error

course_list =['Math','Chemistry','Biology','ICT']
infoes={'name1':'Tirtha','title1':'Biswas','last1':'Joy','name2' : 'Juboraj','title2':'Biswas','last2':'Shanto'}
print('\n'*2)

info(course_list,infoes)     # Prints 
info(*course_list,**infoes)  #Prints course list as Args and infoes as kwarga


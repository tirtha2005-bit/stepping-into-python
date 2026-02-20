# PYTHON LOOPS: FOR and WHILE
# --- FOR LOOPS ---
# Used for iterating over a sequence (lists,tuples,dictionaries,sets,or strings).

#! Ex1: Iterating with Enumerate
list1 = ['BMW', 'Tesla', 'Audi', 'Duranta_Cycle', 'Mercedes_Benz', 'Rolls Royce']
tuples1 = ('Stark', 'McCullum', 'Zampa', 'Shanto', 'Ms_Dhoni')

print('\n\n\nOutput of Code Block 1 :')
for i, items in enumerate(list1, start=1):
    print(i, '.', items)

print('\n' + '-'*30)

#! Ex2: Control Statements (Break & Continue)
#? Break Statement: Used to exit the loop permanently when a condition is met
print('\n\n\nBreak Example:')
for index in list1:
    print(index)
    if index == 'Duranta_Cycle':
        break 

print('\n\n\nContinue Example:')
#? Continue Statement: Skips the current iteration and moves to the next one
for item in tuples1:
    if item == 'Shanto':
        continue
    print(item)

print('\n' + '-'*30)

#! Ex3: Range and Conditional Logic
print('\n\n\nOutput of Code Block 2 (Range):')
for a in range(1, 11):
    if a != 5:
        continue
    print(a, '. Tirtha Biswas Joy')

print('\n' + '-'*30)

#! Ex4: Nested Loops
print('\n\n\nNested Loop Example:')
for x in range(3):        # Outer loop
    for y in range(2):    # Inner loop
        print(f"X: {x}, Y: {y}")

print('\n' + '-'*30)


# --- WHILE LOOPS ---
# A while loop repeats as long as a certain boolean condition is True.
#? To avoid an infinite loop, the condition must eventually become False

print('Corrected While Loop (Countdown):')
count = 5
while count > 0:
    print(f"Value: {count}")
    count -= 1  # Decrementing the counter to ensure the loop stops
print("Loop completed!")



#! Infinite Loop Warning:
# while i != 0:
#    i = i + 1 
#* If i starts at 1, it will never reach 0. This creates an infinite loop.
# To stop an infinite loop in the terminal: Press Ctrl + C
# numeric Variables
# set indepently
x = 1
y = -2
z = 3

# set multiple at once
x, y, z = 1, -2, 3

# operations
answer = x + y + z
print(answer)

# alphanumeric Variables
# set indepently
x = "a1"
y = "b2"
z = "c3"

# set multiple at once
x, y, z = "a1", "b2", "c3"

# operations
answer = x + y + z
print(answer)

# lists
my_list = [1, 2, 3]
print(my_list) # print list object (Literal)

# print via iter
for i in my_list:
    print(i)

# dictionaries
my_dict = {"key 1": "value 1", "key 2": "value 2", "key 3": "value 3"}
print(my_dict) # print dictionary object (Literal)

# print via iter
for key, value in my_dict.items():
    print(f'Key:{key} | Value: {value}') # use an f string to interpolate values into the string without concatinating

# Stacks
stack = [] # init empty stack

# add items to the stack
stack.append("first") # add to top of stack
stack.append("second") # add to top of stack
stack.append("third") # add to top of stack

# getting items from the stack
print(stack[0]) # read item at index (LIFO principle -> Last element in = First element out)
print(stack.pop()) # pop the top element and print it

# reversing a stack
print(stack)
stack.reverse() # flip the stack around
print(stack)

# remove specific item
stack.remove("first")
print(stack)

# clear the stack
stack.clear()

# sorting stacks
stack.append("B") # add to top of stack
stack.append("A") # add to top of stack
stack.append("C") # add to top of stack

print(stack)
stack.sort()# default sort will work on both int and string, and will order accordingly
print(stack)
stack.sort(reverse=True)# reverse sort
print(stack)




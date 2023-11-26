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
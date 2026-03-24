#Code taken from https://www.w3schools.com/python/python_dsa_stacks.asp
#Code was slightly modified to fit the demonstration purposes of this course

stack = []

# Push
stack.append('Oranges')
stack.append('Apples')
stack.append('Strawberries')
#print("Stack: ", stack)

# Peek
topElement = stack[-1]
# print("Peek: ", topElement)

# Pop
# poppedElement = stack.pop()
# print("Pop: ", poppedElement)
# print(stack)

# # Stack after Pop
# print("Stack after Pop: ", stack)

# isEmpty
# isEmpty = not bool(stack)
# hasItems = bool(stack)
# print("isEmpty: ", isEmpty)
# Another way to check if the list is empty
if stack:
    print("This stack is not empty.")
else:
    print("This stack is empty.")

# Size
print("Size: ",len(stack))
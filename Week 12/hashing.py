#Code taken from: https://www.w3schools.com/python/python_dsa_hashtables.asp

#Building a hashtable from scratch
# To get the idea of what a Hash Table is, let's try to build one from scratch, to store unique first names inside it.

# We will build the Hash Table in 5 steps:

# Create an empty list. 
# Create a hash function.
# Inserting an element using a hash function.
# Looking up an element using a hash function.
# Handling collisions.

# Step 1: Create an Empty List
# To keep it simple, let's create a list with 10 empty elements.

#my_list = [None, None, None, None, None, None, None, None, None, None]
# print(my_list)

my_list=[None]*10
print(my_list)

# Step 2: Create a Hash Function
def hash_function(value):
  sum_of_chars = 0
  for char in value:
    sum_of_chars += ord(char)
  return sum_of_chars % 10

print("'Bob' has hash code:", hash_function('Bob'))

# #Step 3: Inserting an Element
# # According to our hash function, "Bob" should be stored at index 5.
# def add(name):
#   index = hash_function(name)
#   my_list[index] = name

# add('Bob')
# print(my_list)

# #  Add more people
# add('Pete')
# add('Jones')
# add('Lisa')
# add('Siri')
# print(my_list)

# #Step 4: Looking up a name
# def contains(name):
#   index = hash_function(name)
#   return my_list[index] == name

# print("'Pete' is in the Hash Table:", contains('Pete'))

# #So far, so good, but how do we handle collisions? Look at the code in collisions.py

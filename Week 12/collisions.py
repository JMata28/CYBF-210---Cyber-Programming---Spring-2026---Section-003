# Node class for linked list entries
class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return str(self.value)

# Our hashtable of 10 buckets
my_list = [None] * 10


# Hash function
def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)
    return sum_of_chars % 10


# New function: collision_add()
def collision_add(name):
    index = hash_function(name)
    print(f"Name {name} gave an index of {index}")
    # Case 1: bucket is empty → insert directly
    if my_list[index] is None:
        my_list[index] = Node(name)
        return

    # Case 2: bucket is NOT empty → traverse linked list
    current = my_list[index]

    while True:
        # If name already exists, do nothing (set stores unique values)
        if current.value == name:
            return

        # If at end of list, insert new node
        if current.next_node is None:
            current.next_node = Node(name)
            return

        current = current.next_node


# Updated contains() for linked list chaining
def contains(name):
    index = hash_function(name)
    current = my_list[index]

    while current is not None:
        if current.value == name:
            return True
        current = current.next_node

    return False

# ---- TESTING ----
collision_add('Bob')
collision_add('Pete')
collision_add('Jones')
collision_add('Lisa')
collision_add('Siri')
collision_add('Stuart')

print("'Pete' is in the Hash Table:", contains('Pete'))
print("'Lisa' is in the Hash Table:", contains('Lisa'))
print("'Stuart' is in the Hash Table:", contains('Stuart'))
print("'NotInTable' is in the Hash Table:", contains('NotInTable'))
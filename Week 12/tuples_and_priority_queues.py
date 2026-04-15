#Code originally taken from:
# https://www.w3schools.com/python/python_tuples.asp
# https://www.geeksforgeeks.org/python/heap-and-priority-queue-using-heapq-module-in-python/

#TUPLES
#One way to create tuples
# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)
# # thistuple[0] = "strawberry" #this gives an error since tuple items can't be changed
# #Another way to create tuples
# new_tuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(new_tuple)

# #Length of a tuple
# tuple_3 = ("apple", "banana", "cherry")
# print("The length of tuple_3 is: ", len(tuple_3))

# #Tuples can have multiple data types inside
# tuple_4 = ("abc", 34, True, 40, "male")

# #For loops can be used to iterate through tuples
# for item in tuple_4:
#     print(item)

#PRIORITY QUEUES
# import modules
import heapq

# list of students
list_stu = [(5,'Rina'),(1,'Anish'),(3,'Moana'),(2,'Cathy'),(4,'Lucy')]
print("Heap before the heapify function", list_stu)
# Arrange based on the roll number
heapq.heapify(list_stu)
print("Heap after the heapify function", list_stu)

#This is the order of the list items themselves (this won't always match the order of priority)
# for i in list_stu:
#   print(i[0],':',i[1])

#This is the order of priority 
print("The order of presentation is :")
for _ in range(len(list_stu)):
    print(heapq.heappop(list_stu))
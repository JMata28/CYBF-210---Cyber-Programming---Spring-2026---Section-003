#Code from: https://www.geeksforgeeks.org/python/heap-queue-or-heapq-in-python/ 
#Additional explanation can be found here: https://www.youtube.com/watch?v=E2v9hBgG6gE 


#CREATE MIN HEAP
import heapq
li = [25, 20, 15, 30, 40]
# Convert the list into a min heap
heapq.heapify(li)
print("Min heap:", li)


#APPENDING AND POPPING ELEMENTS TO HEAP
# heapq.heappush(li, 5)
# # Heap before popping
# print("Heap after pushing 5: ", li)
# # Pop the smallest element from the heap
# min = heapq.heappop(li)
# print("Smallest:", min)
# print("List after popping the smallest: ", li)

#APPENDING AND POPPING SIMULTANEOUSLY
# Push a new element (22) and pop the smallest element at the same time
# min = heapq.heappushpop(li, 2)
# print("New smallest: ", min)
# print("List after popping the new smallest: ", li)

#FINDING LARGEST AND SMALLEST ELEMENTS
# Find the 3 largest elements
# maxi = heapq.nlargest(3, li)
# print("3 largest elements:", maxi)
# # Find the 3 smallest elements
# min = heapq.nsmallest(3, li)
# print("3 smallest elements:", min)

#REPLACING AND MERGING
# Replacing the smallest element with 5
min = heapq.heapreplace(li, 5)
print(min)
print("Heap after replacement: ", li)
# Merging Heaps
h2 = [2, 4, 6, 8]
# Merging the lists
h3 = list(heapq.merge(li, h2)) #notice how the output of heapq.merge is then made into a list
print("Merged heap:", h3)



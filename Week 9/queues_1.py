#Sources and additional explanations:
# https://www.youtube.com/watch?v=vOx3vY1w4tM&t=176s
# https://www.geeksforgeeks.org/python/queue-in-python/

from collections import deque #This is a way to import some additional functionalities from the standard Python library "collections"

#Create a queue
q = deque()
#print(q)

#Enqueue elements to the queue. In other words, add an element to the end of the queue.
# In this case, we are adding people to a queue of people waiting to get their food at the cash register:
q.append("Emma")
q.append("Bruce")
q.append("Gary")
q.append("Lilly")
q.append("Sarah")
q.append("Jeff")
print(q)

#Dequeue elements of the queue. In other words, remove elements from the leftmost side of the queue (the start of the queue).
#Emma gets her food, so the line moves up.
satiesfied_customer = q.popleft()
print(f"{satiesfied_customer} has received their order, so the line moves up.")
print(q)
#Let's do that again. Who will be the person receiving their order now?
satiesfied_customer = q.popleft()
print(f"{satiesfied_customer} has received their order, so the line moves up.")

# #Let's peek at who is next in the queue
next_in_queue = q[0]
print(f"{next_in_queue} is the next person in line.")

#Let's peek at who is the last person in the queue
last_in_queue = q[-1]
print(f"{last_in_queue} is the last person in line.")

# What if someone came in after Jeff?
q.append("Ben")
print(q)
last_in_queue = q[-1]
print(f"{last_in_queue} is the last person in line.")


#How to check if there is a line. Similar to how we checked the stack.
def check_queue(q):
    if q:
        print("There are one or more people waiting in line.")
    else:
        print("There are no more people waiting in line.")

check_queue(q)

#We can get the length of a deque using the function len()
#Notice how we name our variable in the for loop _ because we don't use it.
for _ in range(len(q)): 
    q.popleft()

check_queue(q)
import heapq

pq = []

def add_task():
    priority = int(input("Please enter the priority level of this task:   "))
    description = input("Please enter the description of this task: ")
    new_task = (priority, description) #create the new task as a tuple
    pq.append(new_task) #add task to priority queue 
    heapq.heapify(pq) #We use heapify so that the priority queue remains as a minimum heap, which means that the next item to be popped will be the highest in priority (lowest in value)
    print(f"Your task with a priority of {priority} and description of {description} has been succesfully added to your schdeule!")

def process_task():
    if pq:
        completed_task = heapq.heappop(pq) #this pops the highest-priority task while keeping our pq a minimum heap
        print(f"Your task {completed_task[1]}, with a priority of {completed_task[0]}, has been completed!")
    else:
        print("Your schedule has no tasks in it.")

def peek_next_task():
    if pq:
        print(f"The next task in your schedule has a priority of {pq[0][0]} and has the description: {pq[0][1]}")
    else: 
        print("Your schedule has no tasks in it.")

while (True):
    answer = int(input("\n\nSelect one of the following options.\n" \
    "1. Create a new task for your schedule.\n" \
    "2. Complete the next highest-priority task.\n" \
    "3. See (but not complete) the next highest-priority task.\n"
    "4. Exit program.\n"))
    if answer == 1:
        add_task()
    elif answer == 2:
        process_task() 
    elif answer == 3:
        peek_next_task()
    elif answer == 4:
        print("Exiting program. Have a good day.")
        break
    else:
        print("Invalid input. Please try again.")
from collections import deque

q = deque()

while(True):
    answer = int(input("\n\nChoose a number between 1-4 to select an option.\n" \
    "1. Add customer to the queue.\n" \
    "2. Serve the next customer.\n" \
    "3. View the current queue.\n" \
    "4. Exit the program.\n"))
    if answer == 1:
        name = input("Please enter the name of the customer that you want to add: ")
        q.append(name)
        print(f"{name} was succesfully addewd to the queue!")
    elif answer == 2:
        try:
          satusfied_customer = q.popleft()
        except IndexError:
           print("Queue is empty. Cannot perform popleft.")
        else:
            print(f"{satusfied_customer} was served!")
    elif answer == 3:
        print("This is the current queue: ")
        for name in q:
            print(name)
    elif answer == 4:
        print("Exiting program. Goodbye!")
        break
    else:
        print("You entered an invalid number. Please try again.")
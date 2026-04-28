from collections import deque #We will use deques to implement a queue

class Order: #Represents each order made
    total_orders = 0  #Keeps track of the total number of order

    def __init__(self, name, product):
        self.name = name
        self.product = product
        Order.total_orders += 1 #Order number increased by one every time we create a new order
        self.number = Order.total_orders #This way, each order retains their own order number as they are created 
    
    def __str__(self):
        return f"Order {self.number}: {self.name} ordered {self.product}."

class SinglyOrder: #Represents each node in the singly linked list
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def __str__(self):
        return str(self.value)

#Create the empty stacks and queues that will be used in the program
stack_of_fullfilled_orders = []
queue_of_orders = deque()

def insert_node_at_end(head_node, new_order_node):
    curr = head_node #start at the head node
    while(curr.next_node): #this loop stops when curr is the last node in the singly linked list
        curr = curr.next_node
    curr.next_node = new_order_node #add the new order node to the end of the singly linked list
    print("Order added to the end of the linked list!")
    return head_node

# Creates a new order and adds it to the queue
def create_new_order(head_node):
    name = input("Enter the name of the person ordering: ").title() #Capitalize the first letter of each word and make the rest of the letters lowercase
    product = input("Enter the name of the product you want to purchase: ").title() #Capitalize the first letter of each word and make the rest of the letters lowercase
    new_order = Order(name, product) #Creates new order
    queue_of_orders.append(new_order) #Adds new order to the queue
    print(f"New order created. Order number {new_order.number} added for {new_order.name}: {new_order.product}")
    new_order_node = SinglyOrder(new_order) #Create a node from this order for the singly linked list
    if new_order.number == 1:
        head_node = new_order_node #Set the first order ever made to be the head node
        print(f"This order is now the head node in our linked list!")
        return head_node #if this is the first order, we don't need to "insert" the head node into the linked list. It already is just made the head node, so the return keyword exits the create_new_order function without calling the insert_node_at_end function
    head_node = insert_node_at_end(head_node, new_order_node)
    return head_node
    

# Completes (fulfills) the next order in the queue (leftmost order)
def complete_next_order():
    if queue_of_orders: #if there are one or more unfulfilled orders in the queue
        fullfilled_order = queue_of_orders.popleft() #remove fulfilled order from queue
        stack_of_fullfilled_orders.append(fullfilled_order) #add fulfilled order to stack
        print(f"Order number {fullfilled_order.number}, {fullfilled_order.product} ordered by {fullfilled_order.name} has been fulfilled!")
    else:
        print("There are no orders in the queue waiting to be fulfilled at this moment.\n")

# Undoes the last fulfilled order by removing it from the stack and re-adding it to the end of the queue
def undo_last_order():
    if stack_of_fullfilled_orders: #if there are one or more fulfilled orders in the stack
        undone_order = stack_of_fullfilled_orders.pop() #remove last order (rightmost order) from the stack
        queue_of_orders.append(undone_order) #add the undone order to the end of the queue (leftmost side of queue)
        print(f"Order number {undone_order.number}, {undone_order.product} ordered by {undone_order.name} has been undone and re-added to the end of the queue!")
    else:
        print("There is no order previously fullfilled that can be undone.\n")

# Iterates through the queue and displays all current orders.
def display_current_orders():
    if queue_of_orders: #if there are one or more unfulfilled orders in the queue
        print("The following are the orders in the queue waiting to be fulfilled:")
        for order in queue_of_orders:
            print(order)
    else:
        print("There are no orders in the queue waiting to be fulfilled at this moment.\n")

# Simply iterates through the linked list and prints each order
def display_all_orders_ever(head_node):
    if head_node: #as long as head node exists (as long as the first order has been created)
        print("These are all the orders ever made: ")
        curr = head_node #curr is the "current node" that we are looking at. We start at the head node
        #This while loop below only stops when curr is None (when curr is the tail node)
        while(curr): #Will run as long as curr is not after the tail node 
            print(curr)
            curr = curr.next_node
    else: 
        print("No orders have ever been created yet.\n")

# Recursive function that 
def traverse_linked_list(curr_node, count_of_orders): 
    if curr_node:
        count_of_orders += 1
        if curr_node.next_node: 
            count_of_orders = traverse_linked_list(curr_node.next_node, count_of_orders)
        return count_of_orders #base case: eventually, curr_node.next node will be None, so the function won't call itself forever
    else: 
        print("No orders have ever been created yet.\n")

# Main menu. Simple selection of 1-7 with a check in place for any other input.
def main():
    print("Welcome to Prof. Mata's Tech Goods Store!")
    head_node = None
    while(True):
        answer = int(input("\nPlease choose one of the following options:\n" \
            "1. Add a new order to the queue.\n"
            "2. Complete the next order.\n"
            "3. Undo the last fulfilled order.\n"
            "4. Display the queue of current orders.\n"
            "5. Display all the orders ever made.\n" 
            "6. Count the number of total orders ever made.\n"
            "7. Exit the program.\n"))
        if answer == 1:
            head_node = create_new_order(head_node) # We pass to the function and receive back the head node
        elif answer == 2:
            complete_next_order()
        elif answer == 3:
            undo_last_order()
        elif answer == 4:
            display_current_orders()
        elif answer == 5:
            display_all_orders_ever(head_node)    
        elif answer == 6:
            #Even though we could simply use the class attribute "total_orders" to know the total amount of orders, to practice recursion and singly-linked list traversion, we will call the count the amount of links in the linked list to determine how many total orders have ever been made.
            count_of_orders = traverse_linked_list(head_node, 0)
            if count_of_orders: #As long as there is at least one order, print the total number of orders
                print(f"Total number of orders ever made: {count_of_orders}")
        elif answer == 7:
            print("Exiting the program. Have a good day!")
            return #ends the main() function
        else: 
            print("Invalid input. Please try again.")

main()
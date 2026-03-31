#Sources and additional explanations:
# https://www.youtube.com/watch?v=dqLHTK7RuIo
# https://www.w3schools.com/python/python_dsa_linkedlists.asp 

#Create a class to create the nodes
class DoublyNode:
    def __init__(self, val, next_node=None, previous_node=None):
        self.val = val
        self.next_node = next_node
        self.previous_node = previous_node

    def __str__(self):
        return str(self.val)

#Create nodes
head_node = DoublyNode("square")
A = DoublyNode("rectangle")
B = DoublyNode("circle")
tail_node = DoublyNode("triangle")

#Assign nodes their next and previous nodes
head_node.next_node = A
A.next_node = B
A.previous_node = head_node
B.next_node = tail_node
B.previous_node = A
tail_node.previous_node = B

#A neat useful way to modify this code to display the linked list to give us a useful visual:
#Here we assume we are given the head node
def display_doubly(first_node):
    curr = first_node
    list_of_nodes = []
    while(curr): 
        list_of_nodes.append(str(curr.val))
        curr = curr.next_node
    print(' <-> '.join(list_of_nodes))

display_doubly(head_node)


#To delete a specific node, assuming you have access to that node
def delete_specific_node_doubly(head_node, tail_node, node_to_delete):
    if node_to_delete is None:
        return head_node, tail_node

    # If deleting the head node
    if node_to_delete == head_node:
        head_node = node_to_delete.next_node
        if head_node:
            head_node.previous_node = None
        else:
            tail_node = None  # List is now empty
        return head_node, tail_node

    # If deleting the tail node
    if node_to_delete == tail_node:
        tail_node = node_to_delete.previous_node
        if tail_node:
            tail_node.next_node = None
        else:
            head_node = None  # List is now empty
        return head_node, tail_node

    # Otherwise, deleting a middle node
    previous_node = node_to_delete.previous_node
    next_node = node_to_delete.next_node

    if previous_node:
        previous_node.next_node = next_node
    if next_node:
        next_node.previous_node = previous_node

    # Optional: clear the deleted node’s pointers for safety
    node_to_delete.previous_node = None
    node_to_delete.next_node = None

    return head_node, tail_node

head_node, tail_node = delete_specific_node_doubly(head_node, tail_node, tail_node)
display_doubly(head_node)

#To insert a new node, assuming what you have is the position (assuming imaginary zero indexing: head_node has an imaginary index of 0, the second node has an imaginary index of 2, and so on and so forth.)

def insert_Node_At_Position_Doubly(head_node, tail_node, new_node, position):
    # Case 1: Insert at the head (position 0)
    if position == 0:
        new_node.next_node = head_node
        new_node.previous_node = None
        if head_node:
            head_node.previous_node = new_node
        else:
            tail_node = new_node  # List was empty
        head_node = new_node
        return head_node, tail_node

    currentNode = head_node
    index = 0

    # Traverse to the node before the insertion point
    while currentNode and index < position - 1:
        currentNode = currentNode.next_node
        index += 1

    # If we reached the end before the target position → insert at tail
    if currentNode is None or currentNode.next_node is None:
        if tail_node:
            tail_node.next_node = new_node
            new_node.previous_node = tail_node
            new_node.next_node = None
        else:
            # Empty list
            head_node = tail_node = new_node
            new_node.previous_node = new_node.next_node = None
        tail_node = new_node
        return head_node, tail_node

    # Normal insertion in the middle
    new_node.next_node = currentNode.next_node
    new_node.previous_node = currentNode
    currentNode.next_node.previous_node = new_node
    currentNode.next_node = new_node

    return head_node, tail_node

D = DoublyNode("hexagon")
E = DoublyNode("octagon")

head_node, tail_node = insert_Node_At_Position_Doubly(head_node, tail_node, D, 1)
display_doubly(head_node)
head_node, tail_node = insert_Node_At_Position_Doubly(head_node, tail_node, E, 2)
display_doubly(head_node)

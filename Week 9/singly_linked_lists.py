#Sources and additional explanations:
# https://www.youtube.com/watch?v=dqLHTK7RuIo
# https://www.w3schools.com/python/python_dsa_linkedlists.asp 

#Create a class to create the nodes
class SinglyNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

    def __str__(self):
        return str(self.val)

#Create the nodes of the linked list with their values
head_node = SinglyNode("wrench") #I only need to pass one value, since "next_node" defaults to None
A = SinglyNode("hammer")
B = SinglyNode("nail")
C = SinglyNode("screwdriver")

#Make the nodes of the linked list point to the next node
head_node.next_node = A
A.next_node = B
B.next_node = C
#At this point C is already pointing to None

#How to traverse the linked list
curr = head_node #curr is the "current node" that we are looking at. We start at the head node

# #This loop below only stops when curr is None (when curr is the tail node)
# while(curr): #Will run as long as curr is not after the tail node 
#     print(curr)
#     curr = curr.next_node

#A neat useful way to modify this code to display the linked list to give us a useful visual:
def display(first_node):
    curr = first_node
    list_of_nodes = []
    while(curr): 
        list_of_nodes.append(str(curr.val))
        curr = curr.next_node
    print(' -> '.join(list_of_nodes))

# display(head_node)

#How to search for a node in the linked list
def search_linked_list(head_node, target_value):
    curr = head_node
    while curr:
        if curr.val == target_value:
            return True
        curr = curr.next_node
    return False

# #What do we expect as output for the next two statements?
# print(search_linked_list(head_node, "nail"))
# print(search_linked_list(head_node, "helmet"))

#To delete a specifc node
def delete_specific_node(head_node, node_to_delete):
  if head_node == node_to_delete:
    return head_node.next_node

  curr = head_node
  while curr.next_node and curr.next_node != node_to_delete:
    curr = curr.next_node

  if curr.next_node is None:
    return head_node

  curr.next_node = curr.next_node.next_node

  return head_node

new_head_node = delete_specific_node(head_node, B)
display(new_head_node)

#To insert a specific node
#Let's assume that the position works as a zero-based index (first position is 0, second position is 1, and so on.)
def insert_Node_At_Position(head_node, new_node, position):
  if position == 0:
    new_node.next_node = head_node
    return new_node

  currentNode = head_node
  #We loop (position-1) times because we only need to get to the node BEFORE the position where we want to insert. For example: if you want to insert at position 3 (the fourth node), you want to stop at position 2 (the third node). So looping with range (2) will give traverse through nodes of indexes 0 and 1, leaving the current node as the node with index 2. 
  for _ in range(position-1): 
    if currentNode is None:
      break
    currentNode = currentNode.next_node

  new_node.next_node = currentNode.next_node
  currentNode.next_node = new_node
  return head_node

new_node = SinglyNode("shovel")
new_head_node = insert_Node_At_Position(new_head_node, new_node, 1)
display(new_head_node)
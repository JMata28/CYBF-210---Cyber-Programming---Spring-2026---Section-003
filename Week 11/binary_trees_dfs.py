#Code taken from: https://www.w3schools.com/python/python_dsa_binarytrees.asp
#Look there for additional explanations

#Create binary tree. This is the same tree as the one in "binary_trees.py"
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG


#Pre-Order Traversal of this binary tree
def preOrderTraversal(node):
  if node is None: #base case
    return
  #the keyword end is used to tell print the print function what to print INSTEAD of starting a newline character, like it usually would.
  print(node.data, end=", ") 
  preOrderTraversal(node.left)
  preOrderTraversal(node.right)

print("Pre-order traversal DFS: ")
preOrderTraversal(root)
print("\n\n")

#In-Order Traversal of this binary tree
def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=", ")
  inOrderTraversal(node.right)

print("In-order traversal DFS: ")
inOrderTraversal(root)
print("\n\n")

#Post-Order Traversal of this binary tree
def postOrderTraversal(node):
  if node is None:
    return
  postOrderTraversal(node.left)
  postOrderTraversal(node.right)
  print(node.data, end=", ")

print("Post-order traversal DFS: ")
postOrderTraversal(root)
print("\n\n")
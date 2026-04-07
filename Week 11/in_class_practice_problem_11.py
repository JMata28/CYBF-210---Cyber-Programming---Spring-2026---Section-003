from collections import deque

def levelOrder(root):
    if root is None:
        return
    
    result = []

    q = deque([root])

    while q:
        q_length = len(q)
        level = []
        for _ in range(q_length):
            node = q.popleft()
            #print(node.data)
            if node:
                level.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)
    
    return result

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

print(levelOrder(root))
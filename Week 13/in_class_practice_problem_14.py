edge_list = [
    [0,1],
    [1,3],
    [1,2],
    [2,4],
    [4,1],
    [4,5],
    [5,1],
    [3,5],
    [5,6],
    [6,2]
]

from collections import defaultdict

adjacency_list = defaultdict(list)

for start_node, end_node in edge_list:
    adjacency_list[start_node].append(end_node)

print("This is the adjacency list: ", adjacency_list)


#DFS with recursion
def dfs_recursive(node):
    print(node)
    for neighbor_node in adjacency_list[node]:
        if neighbor_node not in seen:
            seen.add(neighbor_node)
            dfs_recursive(neighbor_node)

source = 0 #starting point of our graph
seen = set()
seen.add(source)
print("\nThe following output is the DFS pre-order output: ")
dfs_recursive(source)


#BFS with queue 
print("\nThe following output is the BFS output: ")
source = 0 

from collections import deque

seen = set()
seen.add(source)
q = deque()
q.append(source)

while q:
    node = q.popleft()
    print(node)
    for neighbor_node in adjacency_list[node]:
        if neighbor_node not in seen:
            seen.add(neighbor_node)
            q.append(neighbor_node)
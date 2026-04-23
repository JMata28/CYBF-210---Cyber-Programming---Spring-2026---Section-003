#Code obtained from: https://www.youtube.com/watch?v=4jyESQDrpls 

n=8 #number of nodes
A = [
    [0,1],
    [1,2],
    [0,3],
    [3,4],
    [3,6],
    [3,7],
    [4,2],
    [4,5],
    [5,2]
]

#Convert to Adjacency List
#defaultdict works like a regular Python dictionary, but automatically creates a default value for a missing key using a function you provide.
from collections import defaultdict

D = defaultdict(list) #creates an empty list as the value for every key by default

for u, v in A:
    D[u].append(v)
    #if it is an undirected graph, also point the edges the other way by uncommenting the line below
    #D[v].append(u)

print(D)


#DFS with recursion
def dfs_recursive(node):
    print(node)
    for neighbor_node in D[node]:
        if neighbor_node not in seen:
            seen.add(neighbor_node)
            dfs_recursive(neighbor_node)

source = 0 #starting point of our graph
seen = set()
seen.add(source)
dfs_recursive(source)



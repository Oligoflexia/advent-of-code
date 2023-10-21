from utils.get_input import get_input
import numpy as np

input = get_input(2015, 9)

nodes = {}
node_names = set()

class Node:
    def __init__(self, name, edges=None):
        self.name = name
        self.edges = edges if edges is not None else {}

for line in input.splitlines():
    data = line.split(" ")
    
    n1 = data[0]
    n2 = data[2]
    distance = int(data[-1])
    
    if n1 not in nodes:
        nodes[n1] = Node(n1)
    if n2 not in nodes:
        nodes[n2] = Node(n2)
    
    nodes[n1].edges[n2] = distance
    nodes[n2].edges[n1] = distance
    
for n in node_names:
    obj = nodes[n]
    print(f"{obj.name}: {obj.edges}")
    
def solve(curr, not_visited, path):
    if len(not_visited) == 0:
        return path
    
    path.append(curr.name)
    not_visited.remove(curr.name)
    
    if not_visited:
        next_node = min((k for k in curr.edges.keys() if k in not_visited), key=curr.edges.get)
        curr = nodes[next_node]
        return solve(curr, not_visited, path)
    else:
        return path
    
start_node = nodes[next(iter(nodes.keys()))]
not_visited = set(nodes.keys())
path = []
result = solve(start_node, not_visited, path)

print(result)

total = 0

for i in range(len(result) - 1):
    n1 = nodes[result[i]]
    n2 = nodes[result[i+1]]
    
    total += n1.edges[n2.name]

print(f"total distance is {total}KM")
    
    
    


        


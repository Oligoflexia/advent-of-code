from utils.helpers import get_input

input = get_input(2015, 9)

class Node:
    def __init__(self, name, edges=None):
        self.name = name
        self.edges = edges if edges is not None else {}

nodes = {}

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
    
# for n in nodes:
#     obj = nodes[n]
#     print(f"{obj.name}: {obj.edges}")
    
def solve(graph, start, visited=set()):
    if len(visited) == len(graph):
        return 0, []
    
    min_d = float('inf')
    path = []
    
    for n, d in graph[start].edges.items():
        if n not in visited:
            visited.add(n)
            remaining_distance, remaining_path = solve(graph, n, visited)
            visited.remove(n)   
             
            total_distance = d + remaining_distance
            if total_distance < min_d:
                min_d = total_distance
                path = [n] + remaining_path
            
    return min_d, path

global_optima = float('inf')
g_path = []

for start_node in nodes.keys():
    min_d, path = solve(nodes, start_node, {start_node})
    if min_d < global_optima:
        global_optima = min_d
        g_path = [start_node] + path

print(f"Optimal shortest path is {global_optima} KM")
print(f"The path taken is {' --> '.join(g_path)}")


def solve_max(graph, start, visited=set()):
    if len(visited) == len(graph):
        return 0, []
    
    max_d = float('-inf')
    path = []
    
    for n, d in graph[start].edges.items():
        if n not in visited:
            visited.add(n)
            remaining_distance, remaining_path = solve_max(graph, n, visited)
            visited.remove(n)   
             
            total_distance = d + remaining_distance
            if total_distance > max_d:
                max_d = total_distance
                path = [n] + remaining_path
            
    return max_d, path

global_maxima = float('-inf')
gm_path = []

for start_node in nodes.keys():
    max_d, path = solve_max(nodes, start_node, {start_node})
    if max_d > global_maxima:
        global_maxima = max_d
        gm_path = [start_node] + path

print(f"The least optimal path is {global_maxima} KM")
print(f"The path taken is {' --> '.join(gm_path)}")
    
    


        


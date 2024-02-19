from collections import deque

class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

def add_edge(node1, node2):
    node1.neighbors.add(node2)
    node2.neighbors.add(node1)

def bfs_coloring(start_node, max_degree):
    colors = {i for i in range(max_degree + 1)}
    queue = deque([start_node])
    
    while queue:
        current = queue.popleft()
        if current.color is None:
            used_colors = {neighbor.color for neighbor in current.neighbors if neighbor.color is not None}
            for color in colors:
                if color not in used_colors:
                    current.color = color
                    break
                    
        for neighbor in current.neighbors:
            if neighbor.color is None and neighbor not in queue:
                queue.append(neighbor)
# Create nodes
a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')
d = GraphNode('d')
e = GraphNode('e')
f = GraphNode('f')
g = GraphNode('g')
h = GraphNode('h')

# Add edges
add_edge(a, b)
add_edge(a, c)
add_edge(a, d)
add_edge(b, d)
add_edge(c, d)
add_edge(c, e)
add_edge(d, f)
add_edge(e, f)
add_edge(e, g)
add_edge(f, h)
add_edge(g, h)

# Perform BFS coloring
bfs_coloring(a, 3)  # We use 3 because it's the maximum degree in the example graph.

# Print the color of each node
for node in [a, b, c, d, e, f, g, h]:
    print(f'Node {node.label} has color: {node.color}')

# This will print colors for each node such that no two adjacent nodes have the same color.

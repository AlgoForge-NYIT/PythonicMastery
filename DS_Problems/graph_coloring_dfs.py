class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

def add_edge(node1, node2):
    node1.neighbors.add(node2)
    node2.neighbors.add(node1)

def dfs_coloring_iterative(start_node, max_degree):
    stack = [start_node]
    visited = set()

    while stack:
        node = stack.pop()
        if node in visited:
            continue

        visited.add(node)  # Mark the node as visited
        available_colors = set(range(max_degree + 1))  # Prepare available colors

        # Determine which colors are already in use by adjacent nodes
        used_colors = set(neighbor.color for neighbor in node.neighbors)
        available_colors -= used_colors  # Remove used colors from the available colors

        # Assign the first available color to the node
        node.color = available_colors.pop()

        # Add all unvisited neighbors to the stack
        for neighbor in node.neighbors:
            if neighbor not in visited:
                stack.append(neighbor)

# Example usage:
# Create nodes
nodes = {label: GraphNode(label) for label in 'abcdefgh'}
# Add edges as per the provided graph structure
edges = [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'd'), ('c', 'd'), 
         ('c', 'e'), ('d', 'f'), ('e', 'f'), ('e', 'g'), ('f', 'h'), ('g', 'h')]

for edge in edges:
    add_edge(nodes[edge[0]], nodes[edge[1]])

# Perform iterative DFS coloring with a maximum degree of 3
dfs_coloring_iterative(nodes['a'], 3)

# Print the color of each node
for label in 'abcdefgh':
    print(f'Node {nodes[label].label} has color: {nodes[label].color}')

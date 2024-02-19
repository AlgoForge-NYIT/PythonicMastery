# Define the vertices and the initial distances
vertices = ["S", "A", "B", "C", "D", "E"]
memo = {
    "S": 0,
    "A": float("inf"),
    "B": float("inf"),
    "C": float("inf"),
    "D": float("inf"),
    "E": float("inf")
}

# Define the graph with edges and their costs
graph = [
    {"from": "S", "to": "A", "cost": 4},
    {"from": "S", "to": "E", "cost": -5},
    {"from": "A", "to": "C", "cost": 6},
    {"from": "B", "to": "A", "cost": 3},
    {"from": "C", "to": "B", "cost": -2},
    {"from": "D", "to": "C", "cost": 3},
    {"from": "D", "to": "A", "cost": 10},
    {"from": "E", "to": "D", "cost": 8}
]

# Function to iterate over the graph and update distances
def iterate():
    do_it_again = False
    for from_vertex in vertices:
        edges = [path for path in graph if path["from"] == from_vertex]
        for edge in edges:
            potential_cost = memo[edge["from"]] + edge["cost"]
            if potential_cost < memo[edge["to"]]:
                memo[edge["to"]] = potential_cost
                do_it_again = True
    return do_it_again

# Run the Bellman-Ford algorithm
for vertex in vertices:
    if not iterate():
        break

# Print the shortest paths to all vertices
print(memo)

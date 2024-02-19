class MemoTable:
    def __init__(self, vertices):
        self.S = {"name": "S", "cost": 0, "visited": False}
        self.table = [self.S] + [{"name": vertex, "cost": float("inf"), "visited": False} for vertex in vertices]

    def get_candidate_vertices(self):
        return [entry for entry in self.table if not entry["visited"]]

    def next_vertex(self):
        candidates = self.get_candidate_vertices()
        if candidates:
            return min(candidates, key=lambda x: x["cost"])
        else:
            return None

    def set_current_cost(self, vertex, cost):
        self.get_entry(vertex)["cost"] = cost

    def set_as_visited(self, vertex):
        self.get_entry(vertex)["visited"] = True

    def get_entry(self, vertex):
        return next(entry for entry in self.table if entry["name"] == vertex)

    def get_cost(self, vertex):
        return self.get_entry(vertex)["cost"]

    def __str__(self):
        return str(self.table)

# Graph and vertices definition
vertices = ["A", "B", "C", "D", "E"]
graph = [
    {"from": "S", "to": "A", "cost": 4},
    {"from": "S", "to": "E", "cost": 2},
    {"from": "A", "to": "D", "cost": 3},
    {"from": "A", "to": "C", "cost": 6},
    {"from": "A", "to": "B", "cost": 5},
    {"from": "B", "to": "A", "cost": 3},
    {"from": "C", "to": "B", "cost": 1},
    {"from": "D", "to": "C", "cost": 3},
    {"from": "D", "to": "A", "cost": 1},
    {"from": "E", "to": "D", "cost": 1}
]

# Initialize memo table
memo = MemoTable(vertices)

def evaluate(vertex):
    edges = [edge for edge in graph if edge["from"] == vertex["name"]]
    for edge in edges:
        current_vertex_cost = memo.get_cost(edge["from"])
        to_vertex_cost = memo.get_cost(edge["to"])
        tentative_cost = current_vertex_cost + edge["cost"]
        if tentative_cost < to_vertex_cost:
            memo.set_current_cost(edge["to"], tentative_cost)
    memo.set_as_visited(vertex["name"])
    next_vertex = memo.next_vertex()
    if next_vertex:
        evaluate(next_vertex)

# Kick off the evaluation from the source vertex
evaluate(memo.S)
print(memo)

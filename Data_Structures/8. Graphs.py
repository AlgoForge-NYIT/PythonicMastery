class Graph:
    def __init__(self):
        self._nodes = {}

    def addNode(self, value):
        if value is None:
            return
        self._nodes[value] = self._nodes.get(value, [])

    def removeNode(self, value):
        if value in self._nodes:
            for neighbor in self._nodes[value]:
                self._nodes[neighbor].remove(value)
            del self._nodes[value]

    def contains(self, value):
        return value in self._nodes

    def addEdge(self, value1, value2):
        if value1 not in self._nodes or value2 not in self._nodes:
            return 'Invalid node value'
        self._nodes[value1].append(value2)
        self._nodes[value2].append(value1)

    def removeEdge(self, value1, value2):
        if value1 not in self._nodes or value2 not in self._nodes:
            return 'Invalid node value'
        self._nodes[value1].remove(value2)
        self._nodes[value2].remove(value1)

    def hasEdge(self, value1, value2):
        return value2 in self._nodes[value1]

    def forEach(self, fn):
        for node, neighbors in self._nodes.items():
            fn(node, neighbors)

    def traverseDepthFirst(self, value, fn, visited=None, distance=0):
        if value not in self._nodes or not callable(fn):
            return 'Invalid value or function'
        visited = visited or {}
        distance = distance
        fn(value, distance)
        visited[value] = True
        for neighbor in self._nodes[value]:
            if neighbor not in visited:
                self.traverseDepthFirst(neighbor, fn, visited, distance + 1)

    def traverseBreadthFirst(self, value, fn):
        if value not in self._nodes or not callable(fn):
            return 'Invalid value or function'
        visited = {value: 0}
        queue = [value]
        while queue:
            node = queue.pop(0)
            fn(node, visited[node])
            for neighbor in self._nodes[node]:
                if neighbor not in visited:
                    visited[neighbor] = visited[node] + 1
                    queue.append(neighbor)


g = Graph()

# Test 1: Graph Construction
g.addNode('A')
g.addNode('B')
g.addEdge('A', 'B')
print("Test 1 - Expected: True, True - Actual:", g.contains('A'), g.hasEdge('A', 'B'))

# Test 2: Depth-First Traversal
print("Test 2 - Depth-First Traversal:")
g.traverseDepthFirst('A', lambda node, distance: print(f"Visited {node} at distance {distance}"))

# Test 3: Breadth-First Traversal
print("Test 3 - Breadth-First Traversal:")
g.traverseBreadthFirst('A', lambda node, distance: print(f"Visited {node} at distance {distance}"))


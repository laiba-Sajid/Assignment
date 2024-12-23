
import Graph
import Node
def dfs(graph, start_name, goal_name, visited=None):
    if visited is None:
        visited = set()
    node = graph.get_node(start_name)
    goal = graph.get_node(goal_name)
    visited.add(node)
    print(f"Visiting: {node.name}")
    if node == goal:
        print(f"Goal {goal.name} found!")
        return True
    for neighbor, _ in node.neighbors:
        if neighbor not in visited:
            if dfs(graph, neighbor.name, goal_name, visited):
                return True
    return False
# Example usage:
g = Graph.Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('E', 'F')
dfs(g, 'A', 'F')

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
    def add_neighbor(self, neighbor, cost=1):
        self.neighbors.append((neighbor, cost))
    def __repr__(self):
        return f"Node({self.name})"
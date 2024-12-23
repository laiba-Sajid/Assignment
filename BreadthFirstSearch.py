
import Graph
import Node
def bfs(graph, start_name, goal_name):
    start = graph.get_node(start_name)
    goal = graph.get_node(goal_name)
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        print(f"Visiting: {node.name}")
        if node == goal:
            print(f"Goal {goal.name} found!")
            return True
        if node not in visited:
            visited.add(node)
            for neighbor, _ in node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
    return False
# Example usage:
g = Graph.Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('E', 'F')
bfs(g, 'A', 'F')
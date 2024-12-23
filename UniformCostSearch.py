
import Graph
import Node
def ucs(graph, start_name, goal_name):
    start = graph.get_node(start_name)
    goal = graph.get_node(goal_name)
    queue = [(0, start)]  # (cost, node)
    visited = set()
    while queue:
        # Find the node with the lowest cost
        min_index = 0
        for i in range(1, len(queue)):
            if queue[i][0] < queue[min_index][0]:
                min_index = i
        cost, node = queue.pop(min_index)
        print(f"Visiting: {node.name} with cost: {cost}")
        if node == goal:
            print(f"Goal {goal.name} found with cost {cost}!")
            return True
        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in node.neighbors:
                if neighbor not in visited:
                    queue.append((cost + edge_cost, neighbor))
    return False
# Example usage:
g = Graph.Graph()
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'D', 5)
g.add_edge('B', 'E', 2)
g.add_edge('C', 'F', 1)
g.add_edge('E', 'F', 3)
ucs(g, 'A', 'F')
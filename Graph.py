import Node
class Graph:
    def __init__(self):
        self.nodes = {}
    def add_node(self, name):
        if name not in self.nodes:
            self.nodes[name] = Node.Node(name)
    def add_edge(self, from_node, to_node, cost=1):
        if from_node not in self.nodes:
            self.add_node(from_node)
        if to_node not in self.nodes:
            self.add_node(to_node)
        self.nodes[from_node].add_neighbor(self.nodes[to_node], cost)
    def get_node(self, name):
        return self.nodes.get(name)
    def __repr__(self):
        return f"Graph({self.nodes.keys()})"
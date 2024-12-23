
class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
    def add_neighbor(self, neighbor, cost=1):
        self.neighbors.append((neighbor, cost))
    def __repr__(self):
        return f"Node({self.name})"
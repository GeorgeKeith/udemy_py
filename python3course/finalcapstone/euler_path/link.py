#from graph import Graph
#from node import Node

class Link:

    def __init__(self, node_a, node_b, cost=1):
        self.node_a = node_a
        self.node_b = node_b
        self.cost = cost
        self.node_a.add_link(self)
        self.node_b.add_link(self)

    def __str__(self):
        result = f"({self.node_a}, {self.node_b}, {self.cost})"
        return result

    def name(self, node):
        if node == self.node_a:
            source, destination = self.node_a, self.node_b
        else:
            source, destination = self.node_b, self.node_a

        return f"{source}-{destination}"

    def node_from(self, node):
        if self.node_a == node:
            return self.node_b
        else:
            return self.node_a

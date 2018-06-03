#from link import Link

class Node:

    # Nodes are created in Graph
    def __init__(self, name):
#        self.graph = graph
        self.name = name
        self.links = {}

    def __len__(self):
        return len(self.links)

    def __str__(self):
        return self.name

    # def add_neighbor(self, neighbor):
    #     link = Link(self, self, neighbor)
    #     self.links[neighbor] = link

    def add_link(self, link):
        neighbor = link.node_from(self)
        self.links[neighbor] = link

    def cost(self, neighbor):
        return self.links[neighbor].cost

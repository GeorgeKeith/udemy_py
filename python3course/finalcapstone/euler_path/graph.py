from node import Node
from link import Link

class Graph:

    def __init__(self):
        self.nodes = {}

    def __len__(self):
        return len(self.nodes)

    def add_node(self, name):
        node = Node(name)
        self.nodes[name] = node

    def add_nodes(self, names):
        name_list = names.split(",")
        for name in name_list:
            self.add_node(name)

    def add_link(self, name_a, name_b, cost=1):
        node_a = self.nodes[name_a]
        node_b = self.nodes[name_b]

        link = Link(node_a, node_b, cost)

    def node(self, name):
        return self.nodes[name]

    def link_set(self):
        result = set()
        for node in self.nodes.values():
            for link in node.links.values():
                result.add(link)
        return result
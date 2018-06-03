#from graph import Graph
from node import Node
from link import Link
from unittest import TestCase

class TestNode(TestCase):

    # Node tests

    def test_init(self):
        print("test_init")
#        graph = Graph()
        name = "A"
        node = Node(name)
        self.assertEqual(node.name, name)
        self.assertEqual(len(node), 0)

    def test_len(self):
        print("test_len")
#        graph = Graph()

        node_a = Node("A")
        node_b = Node("B")
        node_c = Node("C")

        link_ab = Link(node_a, node_b)
        link_ac = Link(node_a, node_c)
        self.assertEqual(len(node_a), 2)

    def test_str(self):
        name = "ABC"
        node = Node(name)
        self.assertEqual(str(node), name)

    def test_add_link(self):
        print("test_add_link")
        cost = 5
        node_a = Node("A")
        node_b = Node("B")

        link = Link(node_a, node_b, cost)

        node_a.add_link(link)
        self.assertEqual(len(node_a), 1)

    def test_cost(self):
        print("test_cost")
        cost = 6
        node_a = Node("A")
        node_b = Node("B")

        link = Link(node_a, node_b, cost)
        node_a.add_link(link)
        self.assertEqual(node_a.cost(node_b), cost)


    def test_all(self):
        print("test_node-------------------")
        self.test_init()
        self.test_len()
        self.test_str()
        self.test_add_link()
        self.test_cost()

if __name__ == "__main__": # pragma: no cover
    test = TestNode()
    test.test_all()
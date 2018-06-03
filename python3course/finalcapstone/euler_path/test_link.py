from link import Link
from node import Node
from unittest import TestCase

class TestLink(TestCase):

    def test_init(self):
        print("test_init")
        node_a = Node("A")
        node_b = Node("B")
        cost = 4
        link = Link(node_a, node_b, cost)
        self.assertEqual(link.node_from(node_a), node_b)
        self.assertEqual(link.node_from(node_b), node_a)
        self.assertEqual(link.cost, cost)
        self.assertEqual(node_a.links[node_b], link)
        self.assertEqual(node_b.links[node_a], link)

    def test_str(self):
        print("test_str")
        node_a = Node("A")
        node_b = Node("B")
        cost = 4
        link = Link(node_a, node_b, cost)
        self.assertEqual(str(link), "(A, B, 4)")

    def test_node_from(self):
        print("test_node_from")
        node_a = Node("A")
        node_b = Node("B")
        link = Link(node_a, node_b)
        self.assertEqual(link.node_from(node_a), node_b)
        self.assertEqual(link.node_from(node_b), node_a)

    def test_name(self):
        print("test_name")
        node_a = Node("A")
        node_b = Node("B")
        link = Link(node_a, node_b)
        self.assertEqual(link.name(node_a), "A-B")
        self.assertEqual(link.name(node_b), "B-A")


    def test_all(self):
        print("test_link-------------------")
        self.test_init()
        self.test_str()
        self.test_name()
        self.test_node_from()

if __name__ == "__main__": # pragma: no cover
    test = TestLink()
    test.test_link()
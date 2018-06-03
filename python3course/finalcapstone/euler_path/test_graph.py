from graph import Graph
from unittest import TestCase

class TestGraph(TestCase):

    # Graph tests

    def test_init(self):
        print("test_init")
        graph = Graph()
        self.assertEqual(len(graph), 0)

    def test_len(self):
        print("test_len")
        graph = Graph()
        self.assertEqual(len(graph), 0)
        graph.add_node("A")
        self.assertEqual(len(graph), 1)
        graph.add_node("B")
        self.assertEqual(len(graph), 2)

    def test_add_node(self):
        print("test_add_node")
        graph = Graph()
        graph.add_node("A")
        self.assertEqual(len(graph), 1)

    def test_add_nodes(self):
        print("test_add_nodes")
        graph = Graph()
        graph.add_nodes("A,B,C,D,E,F")
        self.assertEqual(len(graph), 6)

    def test_add_link(self):
        print("test_add_link")
        cost = 3
        graph = Graph()
        graph.add_node("A")
        graph.add_node("B")
        graph.add_link("A", "B", cost)
        node_a = graph.node("A")
        node_b = graph.node("B")
        self.assertEqual(node_a.cost(node_b), cost)
        self.assertEqual(node_b.cost(node_a), cost)

    def test_link_set(self):
        print("test_link_set")
        graph = Graph()
        graph.add_nodes("A,B,C")
        node_a = graph.node("A")
        node_b = graph.node("B")
        node_c = graph.node("C")

        graph.add_link("A", "B")
        graph.add_link("A", "C")
        graph.add_link("B", "C")

        link_ab = node_a.links[node_b]
        link_ac = node_a.links[node_c]
        link_bc = node_b.links[node_c]

        link_set = graph.link_set()
        self.assertTrue(link_ab in link_set)
        self.assertTrue(link_ac in link_set)
        self.assertTrue(link_bc in link_set)
        self.assertEqual(len(link_set), 3)

    def test_all(self):
        print("test_graph-------------------")
        self.test_init()
        self.test_len()
        self.test_add_node()
        self.test_add_nodes()
        self.test_add_link()
        self.test_link_set()

if __name__ == "__main__": # pragma: no cover
    test = TestGraph()
    test.test_all()
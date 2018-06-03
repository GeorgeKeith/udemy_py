from euler import Euler
from graph import Graph
from node import Node
from link import Link
from unittest import TestCase

class TestEuler(TestCase):

    def test_init(self):
        graph = Graph()
        graph.add_nodes("A,B,C")
        graph.add_link("A", "B")
        graph.add_link("A", "C")
        graph.add_link("B", "C")

        node = graph.node("A")
        euler = Euler(graph, node)
        self.assertEqual(euler.graph, graph)
        self.assertIsNotNone(euler.unused_links)
        self.assertEqual(len(euler.unused_links), 3)
        self.assertIsNotNone(euler.link_count)
        self.assertEqual(len(euler.link_count), 0)

    def test_add_link(self):
        graph = Graph()
        node_a = Node("A")
        euler = Euler(graph, node_a)

        node_a = Node("A")
        node_b = Node("B")
        link = Link(node_a, node_b)

        euler.unused_links.add(link)

        self.assertEqual(len(euler.unused_links), 1)
        self.assertEqual(euler.link_count[link], 0)

        euler.add_link(link)
        self.assertEqual(len(euler.unused_links), 0)
        self.assertEqual(euler.link_count[link], 1)

        euler.add_link(link)
        self.assertEqual(len(euler.unused_links), 0)
        self.assertEqual(euler.link_count[link], 2)

    def test_remove_link(self):
        graph = Graph()

        node_a = Node("A")
        euler = Euler(graph, node_a)
        node_b = Node("B")
        link = Link(node_a, node_b)

        euler.unused_links.add(link)

        euler.add_link(link)

        self.assertEqual(len(euler.unused_links), 0)
        self.assertEqual(euler.link_count[link], 1)

        euler.remove_link(link)
        self.assertEqual(len(euler.unused_links), 1)
        self.assertEqual(euler.link_count[link], 0)

        euler.add_link(link)
        euler.add_link(link)

        self.assertEqual(len(euler.unused_links), 0)
        self.assertEqual(euler.link_count[link], 2)

        euler.remove_link(link)
        self.assertEqual(len(euler.unused_links), 0)
        self.assertEqual(euler.link_count[link], 1)

        euler.remove_link(link)
        self.assertEqual(len(euler.unused_links), 1)
        self.assertTrue(link in euler.unused_links)
        self.assertEqual(euler.link_count[link], 0)

    def test_euler(self):
        graph = Graph()
        graph.add_nodes("A,B,C")
        graph.add_link("A", "B")
        graph.add_link("A", "C")
        graph.add_link("B", "C")
        node_a = graph.node("A")
        euler = Euler(graph, node_a)
        path = []
        success = euler.euler(node_a, node_a, path)
        self.assertTrue(success)

        node_b = graph.node("B")
        euler = Euler(graph, node_a)
        path = []
        success = euler.euler(node_a, node_b, path)
        self.assertFalse(success)

        graph.add_nodes("D,E")
        graph.add_link("B", "D")
        graph.add_link("B", "E")
        graph.add_link("E", "D")
        euler = Euler(graph, node_b)
        path = []
        success = euler.euler(node_b, node_b, path)
        self.assertTrue(success)

    def test_all(self):
        self.test_init()
        self.test_add_link()
        self.test_remove_link()
        self.test_euler()

if __name__ == "__main__": # pragma: no cover
    test = TestEuler()
    test.test_all()

from test_node import TestNode
from test_link import TestLink
from test_graph import TestGraph
from test_euler import TestEuler

if __name__ == "__main__":
    test = TestNode()
    test.test_all()
    test = TestLink()
    test.test_all()
    test = TestGraph()
    test.test_all()
    test = TestEuler()
    test.test_all()
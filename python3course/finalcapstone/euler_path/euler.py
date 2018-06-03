from collections import defaultdict
from graph import Graph

class Euler:

    def __init__(self, graph, origin):
        self.graph = graph
        self.origin = origin
        self.unused_links = graph.link_set()

        self.link_count = defaultdict(lambda : 0)

    def add_link(self, link):
        if link in self.unused_links:
            self.unused_links.remove(link)
        self.link_count[link] += 1

    def remove_link(self, link):
        if self.link_count[link] > 1:
            self.link_count[link] -= 1
        elif self.link_count[link] == 1:
            self.link_count[link] = 0
            self.unused_links.add(link)

    # def path_str(self, path):
    #     result = "["
    #     if len(path) > 0:
    #         result = result + path[0].name(self.origin)
    #         next = path[0].node_from(self.origin)
    #         for i in range(1,len(path)):
    #             result = result + ", " + path[i].name(next)
    #             next = path[i].node_from(next)
    #     result = result + "]"
    #     return result

    def euler(self, start, finish, path):

        for link in start.links.values():
            if link in self.unused_links:
                self.add_link(link)
                next = link.node_from(start)
                path.append(link)
                if next == finish:
                    if len(self.unused_links) == 0:
                        return True
                    else:
                        success = self.euler(next, finish, path)
                        if success:
                            return True
                elif len(self.unused_links) != 0:
                    success = self.euler(next, finish, path)
                    if success:
                        return True
                path.pop()
                self.remove_link(link)

        return False

if __name__ == "__main__": # pragma: no cover
    graph = Graph()
    graph.add_nodes("A,B,C,D,E,F")
    graph.add_link("A", "B")
    # graph.add_link("A", "D")
    graph.add_link("B", "C")
    graph.add_link("C", "D")
    graph.add_link("B", "E")
    graph.add_link("B", "F")
    graph.add_link("C", "E")
    graph.add_link("C", "F")
    graph.add_link("D", "E")
    graph.add_link("D", "F")
    graph.add_link("E", "F")
    node_a = graph.node("A")
    euler = Euler(graph, node_a)
    path = []
    node_d = graph.node("D")
    success = euler.euler(node_a, node_d, path)
    if success:
        print(f"Success: path = {euler.path_str(path)}")
    else:
        print("There is no euler path")

class Node:
    def __init__(self, content, children=[]):
        self.content = content
        self.children = children

class RTree(Node):
    def __init__(self, root: Node, sub_tree: list[Node]):
        self.sub_tree = sub_tree

    def display_tree_prof(self):
        if self.content is not None:
            print(self.content)
        for node in self.children:
            node.display_tree_prof()

    def display_tree_large(self):
        if self.sub_tree:
            for node in reversed(self.sub_tree):
                node.display_tree_large()
        if self.content is not None:
            print(self.content)


if __name__ == "__main__":
    n_3 = Node('3')
    n_9 = Node('9')
    n_2 = Node('2', [n_3, n_3, n_9])
    n_a = Node('a')
    n_m = Node('m')

    z = RTree(Node('z'), [n_2, n_a, n_m])

    #display_tree_prof(z)
    z.display_tree_large()
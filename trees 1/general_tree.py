from dataclasses import dataclass, field


@dataclass
class TreeNode:
    element: None = None
    children: list = field(default_factory=list)


class GeneralTree(object):
    def __init__(self, root=None):
        self.root = root

    def populate_tree(self):
        element = input("ROOT element: ")
        if element:
            node = TreeNode(element)
            self.root = node
            self.populate_node(node)

    def populate_node(self, parent, depth=0):
        n = 1
        element = True
        while element:
            element = input(depth * "\t" + f"child #{n} of {parent.element}: ")
            if element:
                node = TreeNode(element)
                parent.children.append(node)
                self.populate_node(node, depth + 1)
            n += 1

    def print_preorder(self):
        print(self.preorder_string(self.root))

    def preorder_string(self, node):
        string = str(node.element)
        for child in node.children:
            child_str = self.preorder_string(child)
            if child_str:
                string += " " + child_str
        return string

    def print_postorder(self):
        print(self.postorder_string(self.root))

    def postorder_string(self, node):
        string = ""
        for child in node.children:
            child_str = self.postorder_string(child)
            if child_str:
                string += child_str + " "
        return string + str(node.element)

    def count_recur(self, element, node=None):
        if node is None:
            return 0
        total = int(node.element == element)
        for child in node.children:
            total += self.count_recur(element, child)
        return total

    def count(self, element):
        return self.count_recur(element, self.root)

    def replace_recur(self, element, with_element, node=None):
        if node is None:
            return
        if node.element == element:
            node.element = with_element
        for child in node.children:
            self.replace_recur(element, with_element, child)

    def replace(self, element, with_element):
        return self.replace_recur(element, with_element, self.root)

    def parent_swap_recur(self, element, node=None):
        if node is None:
            return
        parent_element = node.element
        for child in node.children:
            if child.element == element:
                node.element, child.element = element, parent_element
            self.parent_swap_recur(element, child)

    def parent_swap(self, element):
        self.parent_swap_recur(element, self.root)


if __name__ == "__main__":
    # tree = GeneralTree()
    # tree.populate_tree()
    # tree.print_preorder()
    # tree.print_postorder()
    sample_tree = GeneralTree(TreeNode(
        "A", [TreeNode("B", [TreeNode("C")]), TreeNode("D", [TreeNode("C")])]))
    sample_tree.print_preorder()
    sample_tree.print_postorder()
    print(sample_tree.count("A"))
    sample_tree.replace("C", "A")
    print(sample_tree.count("A"))
    print(sample_tree.count("C"))
    sample_tree.print_preorder()
    sample_tree.parent_swap("A")
    sample_tree.print_preorder()

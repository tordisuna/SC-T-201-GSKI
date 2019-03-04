class BinTreeNode():
    def __init__(self, element=None, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right


class BinaryTree(object):  # Linked structure binary tree
    def __init__(self):
        self.root = None
        # self.size = 0

    def populate_tree(self):
        element = input("ROOT element: ")
        if element:
            node = BinTreeNode(element)
            self.root = node
            self.populate_node(node)

    def populate_node(self, parent, depth=0):
        left_element = input(depth * "\t" + f"LEFT of {parent.element}: ")
        if left_element:
            node = BinTreeNode(left_element)
            parent.left = node
            self.populate_node(node, depth + 1)
        right_element = input(depth * "\t" + f"RIGHT of {parent.element}: ")
        if left_element:
            node = BinTreeNode(right_element)
            parent.right = node
            self.populate_node(node, depth + 1)

    def print_preorder(self):
        print(self.preorder_string(self.root))

    def preorder_string(self, node):
        if node is None:
            return ""
        string = str(node.element)
        left_str = self.preorder_string(node.left)
        if left_str:
            string += " " + left_str
        right_str = self.preorder_string(node.right)
        if right_str:
            string += " " + right_str
        return string

    def print_postorder(self):
        print(self.postorder_string(self.root))

    def postorder_string(self, node):
        if node is None:
            return ""
        string = self.postorder_string(node.left)
        if string:
            string += " "
        right_str = self.postorder_string(node.right)
        if right_str:
            string += right_str + " "
        return string + str(node.element)

    def print_inorder(self):
        print(self.inorder_string(self.root))

    def inorder_string(self, node):
        if node is None:
            return ""
        string = self.inorder_string(node.left)
        if string:
            string += " "
        string += str(node.element)
        right_str = self.inorder_string(node.right)
        if right_str:
            string += " " + right_str
        return string



if __name__ == "__main__":
    tree = BinaryTree()
    tree.populate_tree()
    tree.print_preorder()
    tree.print_postorder()
    tree.print_inorder()

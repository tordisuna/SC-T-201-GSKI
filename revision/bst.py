class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BST(object):
    def __init__(self):
        self.root = None

    def add(self, data):
        self.root = self._add_recur(self.root, data)

    def _add_recur(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._add_recur(node.left, data)
        elif node.data < data:
            node.right = self._add_recur(node.right, data)
        return node

    def _inorder(self, node):
        """Create a generator for the inorder version of the subtree."""
        if node is not None:
            yield from self._inorder(node.left)
            yield node.data
            yield from self._inorder(node.right)

    def __str__(self):
        return " ".join(map(str, self._inorder(self.root)))

    def max(self):
        return self._rightmost(self.root).data

    def _rightmost(self, node):
        """Get the rightmost node in the subtree of the given node."""
        if node.right is not None:
            return self._rightmost(node.right)
        return node


if __name__ == "__main__":
    t = BST()
    from random import randint
    for i in range(100):
        t.add(randint(0, 10000))
    print(t)
    print(t.max())
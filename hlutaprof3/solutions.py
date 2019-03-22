class Item(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return other.key == self.key
        return other == self.key


class BSTNode(object):
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.item.key)


class TreeClass:
    # Part 1
    def __init__(self, preset=0):
        self.root = None
        preset1 = (5, 2, 8, 1, 4, 7, 9)
        preset2 = ("c", "a", "e", "b", "d", "f")
        preset3 = (20, 13, 27, 8, 15, 21)
        presets = [[], preset1, preset2, preset3]
        for key in presets[preset]:
            self[key] = None

    def __str__(self):
        string = " ".join(self._order(self.root, "preorder")) + "\n"
        string += " ".join(self._order(self.root)) + "\n"
        return string + " ".join(self._order(self.root, "postorder"))

    def _order(self, node, order_type="inorder"):
        if node is not None:
            if order_type == "preorder":
                yield str(node)
            yield from self._order(node.left, order_type)
            if order_type == "inorder":
                yield str(node)
            yield from self._order(node.right, order_type)
            if order_type == "postorder":
                yield str(node)

    # Part 3

    def __setitem__(self, key, value):
        self.root = self._set(self.root, key, value)

    def _set(self, node, key, value):
        if node is None:
            return BSTNode(Item(key, value))
        elif key < node.item.key:
            node.left = self._set(node.left, key, value)
        elif node.item.key < key:
            node.right = self._set(node.right, key, value)
        else:
            node.item.value = value
        return node

    def __getitem__(self, key):
        return self._get(self.root, key)

    def _get(self, node, key):
        if node is None:
            return
        elif key < node.item.key:
            return self._get(node.left, key)
        elif node.item.key < key:
            return self._get(node.right, key)
        return node.item.value


class HashClass:
    def __init__(self):
        self.buckets = [list() for _ in range(16)]
        self.bucket_count = 16

    def __setitem__(self, key, data):
        try:
            self._get_item(key).value = data
        except ValueError:
            self.buckets[hash(key) % 16].append(Item(key, data))

    def __getitem__(self, key):
        try:
            return self._get_item(key).value
        except ValueError:
            return None

    def _get_item(self, key):
        bucket = self.buckets[hash(key) % 16]
        return bucket[bucket.index(key)]


# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    h = HashClass()

    t = TreeClass()
    t = TreeClass(1)
    print("\nTesting TreeClass __init__ & __str__")
    t = TreeClass()
    print("The tree: \n" + str(t))
    t = TreeClass(3)
    print("The tree: \n" + str(t))
    t = TreeClass(0)
    print("The tree: \n" + str(t))

    print("\nTesting HashClass __setitem__ & __getitem__")
    h = HashClass()
    h[3] = "three"
    h[17] = "seventeen"
    h[23] = "twntythree"

    print(str(h[23]))
    h[23] = "twentythree"

    print(str(h[23]))
    print(str(h[3]))
    print(str(h[4]))

    print("\nTesting TreeClass __setitem__ & __getitem__")
    t = TreeClass()
    t[17] = "seventeen"
    t[3] = "three"
    t[23] = "twntythree"

    print(str(t[23]))
    t[23] = "twentythree"

    print(str(t[23]))
    print(str(t[3]))
    print(str(t[4]))

    print(str(t))

    t = TreeClass(2)
    print(t)

    t = TreeClass(1)
    print(t)

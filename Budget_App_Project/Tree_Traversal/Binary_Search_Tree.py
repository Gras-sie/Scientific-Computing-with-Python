class TreeNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None
    
    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        return node

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self._search(node.left, key)

        return self._search(node.right, key)

    def search(self, key):
        result_node = self._search(self.root, key)
        return result_node is not None

    def _min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _in_order_traversal(self, node, result):
        if node is not None:
            self._in_order_traversal(node.left, result)
            result.append(node.key)
            self._in_order_traversal(node.right, result)

    def in_order_traversal(self):
        result = []
        self._in_order_traversal(self.root, result)
        return result

    def _pre_order_traversal(self, node, result):
        if node is not None:
            result.append(node.key)
            self._pre_order_traversal(node.left, result)
            self._pre_order_traversal(node.right, result)

    def pre_order_traversal(self):
        result = []
        self._pre_order_traversal(self.root, result)
        return result

    def _post_order_traversal(self, node, result):
        if node is not None:
            self._post_order_traversal(node.left, result)
            self._post_order_traversal(node.right, result)
            result.append(node.key)

    def post_order_traversal(self):
        result = []
        self._post_order_traversal(self.root, result)
        return result

    def clear(self):
        self.root = None
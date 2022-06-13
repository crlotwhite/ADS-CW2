from common.ads.q import Queue


class BinarySearchTree:
    class _BinarySearchTreeNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None

    class _BinarySearchTreeIterator:
        def __init__(self, root):
            self._the_queue = Queue()
            self._traverse_inorder(root)

        def __iter__(self):
            return self

        def __next__(self):
            if self._the_queue.isempty():
                raise StopIteration
            else:
                node = self._the_queue.dequeue()
                key = node.key

                return key

        def _traverse_inorder(self, subtree):
            if subtree is not None:
                self._the_queue.enqueue(subtree)
                self._traverse_inorder(subtree.left)
                self._traverse_inorder(subtree.right)

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        return self._BinarySearchTreeIterator(self._root)

    def __contains__(self, key):
        return self._bst_search(self._root, key) is not None

    def value_of(self, key):
        node = self._bst_search(self._root, key)
        if node is not None:
            return node.value
        else:
            return None

    def _bst_search(self, subtree, target):
        if subtree is None:
            return None
        elif target < subtree.key:
            return self._bst_search(subtree.left, target)
        elif target > subtree.key:
            return self._bst_search(subtree.right, target)
        else:
            return subtree

    def _bst_minimum(self, subtree):
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self._bst_minimum(subtree.left)

    def add(self, key, value):
        node = self._bst_search(self._root, key)

        if node is not None:
            node.value = value
            return False
        else:
            self._root = self._bst_insert(self._root, key, value)
            self._size += 1
            return True

    def _bst_insert(self, subtree, key, value):
        if subtree is None:
            subtree = self._BinarySearchTreeNode(key, value)
        elif key < subtree.key:
            subtree.left = self._bst_insert(subtree.left, key, value)
        elif key > subtree.key:
            subtree.right = self._bst_insert(subtree.right, key, value)
        return subtree

    def remove(self, key):
        assert key in self, "Invalid map key."
        self._root = self._bst_remove(self._root, key)
        self._size -= 1

    def _bst_remove(self, subtree, target):
        if subtree is None:
            return subtree
        elif target < subtree.key:
            subtree.left = self._bst_remove(subtree.left, target)
            return subtree
        elif target > subtree.key:
            subtree.right = self._bst_remove(subtree.right, target)
            return subtree
        else:
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None or subtree.right is None:
                if subtree.left is not None:
                    return subtree.left
                else:
                    return subtree.right
            else:
                successor = self._bst_minimum(subtree.right)
                subtree.key = successor.key
                subtree.value = successor.value
                subtree.right = self._bst_remove(subtree.right, successor.key)
                return subtree

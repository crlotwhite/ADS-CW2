from common.ads.q import Queue


class SortedLinkedList:
    class _ListNode:
        def __init__(self, key, value, next=None):
            self.key = key
            self.value = value
            self.next = next

        def __str__(self):
            return f'{self.key} | {self.value}'

    class _ListIter:
        def __init__(self, head):
            self._the_queue = Queue()
            self._listing(head)

        def __iter__(self):
            return self

        def __next__(self):
            if self._the_queue.isempty():
                raise StopIteration
            else:
                return self._the_queue.dequeue()

        def _listing(self, node):
            cur = node
            while cur is not None:
                self._the_queue.enqueue(cur)
                cur = cur.next

    def __init__(self):
        self._head = None
        self._size = 0

    def __iter__(self):
        return self._ListIter(self._head)

    def __len__(self):
        return self._size

    def add(self, key, value):
        if self.isempty():
            self._head = self._ListNode(key, value)
        else:
            prev = self._head
            for node in self:
                if node.key > key:
                    new_node = self._ListNode(key, value, node)
                    if node.key == self._head.key:
                        self._head = new_node
                    else:
                        prev.next = new_node
                    break
                else:
                    prev = node
            else:
                prev.next = self._ListNode(key, value)

        self._size += 1

    def remove(self, key):
        prev = self._head
        for node in self:
            if node.key == key:
                prev.next = node.next
                self._size -= 1
                return node
            else:
                prev = node
        else:
            return None

    def search(self, key):
        for node in self:
            if node.key == key:
                return node.value
        else:
            return None

    def isempty(self):
        return self._size == 0

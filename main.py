from common.ads.bst import BinarySearchTree
from common.ads.sll import SortedLinkedList
from customer.container import CustomerBTreeType
from dvd.container import DVListType
from ui.navigator import route_main


def tree_test():
    print("===\n\n tree test \n\n")
    tree = BinarySearchTree()
    tree.add(2, 'b')
    tree.add(1, 'a')
    tree.add(4, 'd')
    tree.add(3, 'c')
    tree.add(5, 'e')

    for i in tree:
        print(i)

    print(tree.value_of(5))
    tree.remove(3)

    for i in tree:
        print(i)


def list_test():
    print("===\n\n list test \n\n")
    sll = SortedLinkedList()

    print(sll.isempty())

    sll.add('a', 1)
    sll.add('b', 2)
    sll.add('c', 3)
    sll.add('e', 4)
    sll.add('d', 5)

    for tp in sll:
        print(tp)

    print(sll.isempty())

    print(sll.search('b'))
    print(sll.search('f'))

    print(sll.remove('f'))
    print(sll.remove('e'))

    for tp in sll:
        print(tp)


if __name__ == "__main__":
    context = {
        'customer': CustomerBTreeType(),
        'dvd': DVListType()
    }
    route_main(context)

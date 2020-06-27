class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        nodes = []
        current = node
        while node is not None:
            next = node.next_node
            nodes.append(node)
            node.next_node = None
            node = next

        print([node.value for node in nodes])

        for node in nodes:
            print(node.value)
            next = self.head.next_node
            self.head = node
            self.head.next_node = next

        #print([node.value for node in nodes])

        # if prev is None:
        #     nodes.append(node)
        # else:
        #     if prev.prev:
        #         nodes.append(prev.reverse_list(prev, prev.prev))
        # return nodes

    def __str__(self):
        values = ""
        node = self.head
        while node is not None:
            values += f'({node.value})'
            if node.get_next():
                values += '->'
            node = node.get_next()
        return values


ll = LinkedList()
ll.add_to_head(3)
ll.add_to_head(2)
ll.add_to_head(1)
print(ll)
last = ""
ll.reverse_list(ll.head, ll.head)
print(ll)
# node = ll.head
# while node is not None:
#     if node.get_next():
#         node = node.get_next()
#     else:
#         last = node
#         node = None
# print(last.value) # 3
# ll.reverse(last)

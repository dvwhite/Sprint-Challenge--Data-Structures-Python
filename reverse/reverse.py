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
        if node is None:
            return None
        # Track all visited nodes to allow iteration without cycles
        visited = []
        orig_head = self.head
        while node not in visited:
            # Add all but the head to the head in ascending order
            # reverses the list
            if node != self.head:
                self.add_to_head(node.value)
                if prev:
                    if node.next_node and not prev is orig_head:
                        prev.next_node = node.next_node
                    else:
                        prev.next_node = None
            visited.append(node)
            # You only need a prev and next if there is a next
            if node.next_node:
                prev = node
                node = node.next_node

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

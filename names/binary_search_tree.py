"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
#import ipdb


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # If a leaf exists, traverse to the next leaf
            # Otherwise, create a new leaf
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            # If a leaf exists, traverse to the next leaf
            # Otherwise, create a new leaf
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Return true if the value is found on current node
        if target == self.value:
            return True
        # Otherwise, traverse the tree
        else:
            # Traverse the left hand path if the value is less than self.value
            # Keep searching until all edges are checked
            if target < self.value:
                if self.left:
                    if self.left.value == target:
                        return True
                    else:
                        return self.left.contains(target)
                else:
                    return False
            # Travese the right path otherwise
            # Keep searching until all edges are checked
            else:
                if self.right:
                    if self.right.value == target:
                        return True
                    else:
                        return self.right.contains(target)
                else:
                    return False

    # Return the maximum value found in the tree
    def get_max(self):
        # Base case is reached when there are no more right edges to traverse
        if not self.right:
            return self.value
        # Navigate down all right edges until it hits the max
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Use recursion
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------
    def is_leaf(self):
        """Returns true if the node is a leaf"""
        if not self.left and not self.right:
            return True
        return False

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.in_order_print(node.left)
        print(node.value)  # Make sure to print the intermediary nodes
        if node.right:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, root):
        queue = [root]
        while queue:
            # Dequeue each node off the stack
            node = queue.pop()
            print(node.value)

            # Add existing edges to the stack if they are not in visited
            if node.left:
                queue = [node.left] + queue
            if node.right:
                queue = [node.right] + queue

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Use iterative DFS to call the function on every node
        # Use a stack to add nodes that have not been visited
        stack = [self]
        visited = []
        while stack:
            # Pop each node off the stack
            node = stack.pop()

            # Call fn passing the node's value if not visited
            if not node in visited:
                print(node.value)

            # Add existing edges to the stack if they are not in visited
            if node.right and node.right not in visited:
                stack.append(node.right)
            if node.left and node.left not in visited:
                stack.append(node.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            node.pre_order_dft(node.left)
        if node.right:
            node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            node.post_order_dft(node.left)
        if node.right:
            node.post_order_dft(node.right)
        print(node.value)

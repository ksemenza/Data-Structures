
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
from queue import Queue
from stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        # Case 1: value is less than self.value
        if value == self.value:
            return f"Value already exists"

        # If there is no right child, insert value here
        if value > self.value:
            if self.right:
                self.right.insert(value)

            # Repeat the process on right subtree
            else:
                self.right = BSTNode(value)

        # Case 2: value is greater than or equal self.value
        elif value < self.value:
            if self.left:
                # Repeat the process on left subtree
                self.left.insert(value)
            else:
                self.left = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if not self:
            return False

         # Case 1: self.value is equal to the target
        if self.value == target:
            return True

        # Case 2: target is greater than self.value
        if target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False

        # Case 3: target is less than self.value
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:

                # if self.left is None, it isn't in the tree
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if not self:
            return
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):

        # Node used to declare None on both
        if not node:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        ans = ''
        while q:
            curr = q.dequeue()
            if not curr:
                continue
            ans += str(curr.value) + '\n'
            q.enqueue(curr.left)
            q.enqueue(curr.right)
        print(ans[:-1])

  # Print the value of every node, starting with the given node,
  # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        ans = ''
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            ans += str(curr.value) + '\n'
            stack.push(curr.right)
            stack.push(curr.left)
        print(ans[:-1])

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if not node:
            return
        print(node.value)
        self.pre_order_dft(node.left)
        self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if not node:
            return
        self.post_order_dft(node.left)
        self.post_order_dft(node.right)
        print(node.value)

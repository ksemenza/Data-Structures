"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

        """
        Wrap the given value in a ListNode and insert it
        after this node.
        """

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

        """
        Wrap the given value in a ListNode and insert it
        before this node. 
        """

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

        """
        Rearranges this ListNode's previous and next pointers
        accordingly.
        """

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

    """Our doubly-linked list class. It holds references to
    the list's head and tail nodes.
    """


class DoublyLinkedList:

    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
      # create instance of ListNode with value
        # increment the DLL length attribute

        if isinstance(value, ListNode):
            new = value
        else:
            new = ListNode(value)

            # if DLL is empty
        if not self.head:

            # set head and tail to the new node instance
            self.head = new
            self.tail = new

        # if DLL is not empty
        else:
            # set new node's next to current head
            new.next = self.head
            # set head's prev to new node
            self.head.prev = new
            # set head to the new node
            self.head = new
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):

        # store the value of the head
        if not self.head:
            return
        val = self.head.value

        # set head to None
        # set tail to None
        if self.head is self.tail:
            self.head, self.tail = None, None

            self.length = 0
        # return the value
            return val

        # if head.next is not None
        # set head to head.next
        self.head = self.head.next
        if self.head:

            # set head.next's prev to None
            self.head.prev = None
        # decrement the length of the DLL
        self.length -= 1
        return val

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):

        # create instance of ListNode with value
        if isinstance(value, ListNode):
            new = value

        # if DLL is empty
        else:
            new = ListNode(value)

        # set head and tail to the new node instance
        if not self.tail:
            self.head = new
            self.tail = new

        # if DLL is not empty
        else:
            # set new node's prev to current tail
            new.prev = self.tail

            # set tail's next to new node
            self.tail.next = new

            # set tail to the new node
            self.tail = new

        # increment the DLL length attribute
        self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if not self.tail:
            return
        val = self.tail.value
        # set head and tail to the new node instance
        if self.tail is self.head:

            # set head to None
            # set tail to None
            self.tail, self.head = None, None
            self.length = 0
            return val
            # return the value

        # set tail to tail.prev
        self.tail = self.tail.prev
        if self.tail:

            # set tail.prev's next to None
            self.tail.next = None

        # decrement the length of the DLL
        self.length -= 1
        return val

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if self.tail is node:
            self.tail = self.tail.prev
            self.tail.next = None
        node.delete()
        self.length -= 1
        self.add_to_head(node)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if self.head is node:
            self.head = self.head.next
            self.head.prev = None
        node.delete()
        self.length -= 1
        self.add_to_tail(node)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        if self.head and self.head.value == node.value:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
        if self.tail and self.tail.value == node.value:
            if self.tail.prev:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.tail = None
        node.delete()
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        if not self.head:
            return -1
        max_ = self.head.value
        curr = self.head
        while curr.next:
            curr = curr.next
            if curr.value > max_:
                max_ = curr.value
        return max_

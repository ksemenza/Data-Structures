"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
      First in First Out (FIFO)   
   An array is organized with an index based system. Each element is associated with with a data object that sequentially stores values in allocated memory.  
   Array are under common heading or variables name. They have a fixed size and need to be delcared prior to initiating 
   
   Linked list rely on nodes that consist of data that refers to the previous and next node element. 
   Linked list ae not restricted by size and during execution they can expand and contract. 
   
   There are two fields in an linked list element
   1. a data field that contains the actual value that is stored or being processed.
   2. Link field contains the address of the next data item in the linked list. 
   The address used to access the node is known as a pointer.
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.append(value)

    def dequeue(self):
        if len(self.storage) > 0:
            self.size -= 1
            return self.storage.pop(0)
        else:
            pass


q = Queue()
q.enqueue(1)
q.enqueue(3)
print(len(q.storage))
q.dequeue()
print(q.storage)
print(q.size)

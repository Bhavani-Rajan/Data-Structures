import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list_implemented import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1 
#         print(f"added {self.storage.tail.value} to queue's tail")

    def dequeue(self):
        if (self.storage.head is None):
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_head()
             

    def len(self):
        return self.size

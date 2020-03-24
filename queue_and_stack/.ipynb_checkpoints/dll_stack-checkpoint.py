import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list_implemented import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        #adding to head is expensive for a singly linked list, but for doubly linked
        #list it is an identical process
        self.storage.add_to_tail(value)
        self.size += 1 
#         print(f"added {self.storage.tail.value} to the stack's tail")


    def pop(self):
        if (self.storage.tail is None):
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_tail()
             
            
    def len(self):
        return self.size

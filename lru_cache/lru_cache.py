from doubly_linked_list import *
class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.cache = DoublyLinkedList()
        self.cache_dict = {}


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.cache_dict.keys():
            self.re_order(key)
            return self.cache_dict[key]
        else:
            return None


    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.cache_dict.keys():
            self.cache_dict[key] = value
            self.re_order(key)
        else:
            if (len(self.cache_dict) == self.limit):
                rm_from_dict = self.cache.remove_from_tail()
                self.cache_dict.pop(rm_from_dict)
            
            self.cache_dict[key] = value
            self.cache.add_to_head(key)
    
    """ Parses the linked list from head to the value and makes that as the head"""
    def re_order(self, key):
        i = 0
        len_dict = len(self.cache_dict)
        node = self.cache.head
        while( i < len_dict):
            if(node.value == key):
                self.cache.move_to_front(node)
                i = len_dict
            node = node.next
            i += 1

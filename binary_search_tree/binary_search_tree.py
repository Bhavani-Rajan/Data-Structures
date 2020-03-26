import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if empty

        # if empty put node here/at root

        # if self.value is None:
        #     self = BinarySearchTree(value)


        # if new < node.value
        #     leftnode.insert value

        if value < self.value:
            # print(f"{value} is less than {self.value}")
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        # if >= 
        #     rightnode.insertvalue
        elif value >= self.value:
            # print(f"value is greater than or == {self.value}")
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # find:

        # if node is none
        #     return false
        
        
        if self == None:
            return False

        # if node.value == findvalue
        #     return true

        elif self.value == target:
            return True

        # else
        #     if find <  node.value
        #         find on  left node
        #     else
        #         find on right node
        else:
            if target < self.value:
                if self.left == None:
                    return False
                else:
                    return self.left.contains(target)

            elif target >= self.value:
                if self.right == None:
                    return False
                else:
                    return self.right.contains(target)



    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value    
        return self.right.get_max() 
    
    # Return the minimum value found in the tree
    def get_min(self):
        if self.left == None:
            return self.value    
        return self.left.get_min() 

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb=None):
        cb(self.value)
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)


        # q = Queue()
        # q.enqueue(self)
        # while q.size != 0:
        #     node = q.dequeue()
        #     cb(node.value)
        #     if node.left:
        #         q.enqueue(node.left)
        #     if node.right:
        #         q.enqueue(node.right)
          

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def traverse(self):
        # Try to traverse every elements in array
        pass

    def search(self):
        # search one or many elements follow some requirements
        pass
    def update(self):
        # find and update data for one node in this linked list
        pass

    def insert_head(self, node):
        # insert a node into head of linked list
        pass

    def insert_after(self, node):
        # insert a node after a node
        pass
    def remove_head(self):
        pass

    def get_min(self):
        # Return the min value of linked list
        my_node = my_linked_list.head
        min = my_node.data
        while (my_node):
            if my_node.data < min:
                min = my_node.data
            my_node = my_node.next

        return min

    def count(self,x):
        count = 0
        my_node = my_linked_list.head
        while (my_node):
            if my_node.data == x:
                count +=1
            my_node= my_node.next
        return count
    
    def insert_tail(self, node):
        # first we have link the current tail to the next tail
        #first verify this linkedlist is empty or not
        if (self.head == self.tail == None):
            #initilize
            self.head= self.tail = node
        else:
            self.tail.next = node
            # update the tail
            self.tail = node

my_linked_list = LinkedList()
my_linked_list.insert_tail(Node(7))
my_linked_list.insert_tail(Node(-2))
my_linked_list.insert_tail(Node(99))
my_linked_list.insert_tail(Node(10))
my_linked_list.insert_tail(Node(99))

min = my_linked_list.get_min()
print(my_linked_list.count(min))


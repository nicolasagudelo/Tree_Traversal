from node import Node

class Stack():
    def __init__(self, max_size = None):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_size = max_size
    
    def peek(self):
        if self.is_empty():
            print('Nothing to see here!')
        else:
            return self.head.get_value()
    
    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.size
    
    def is_empty(self):
        return self.get_size() == 0

    def push(self, value):
        if self.has_space():
            item_to_add = Node(value)
            # print('Adding ' + str(item_to_add.get_value()) + ' to the stack!')
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                item_to_add.set_next_node(self.head)
                self.head = item_to_add
            self.size += 1
        else:
            print('Sorry, no more room!')

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.head
            # print('Removing ' + str(item_to_remove.get_value()) + ' from the stack!')
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = item_to_remove.get_next_node()
            self.size -= 1
            return(item_to_remove.get_value())
        else:
            print('This stack is totally empty!')
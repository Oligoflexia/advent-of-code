from utils.get_input import get_input

input = get_input(2015, 7)

class Node:
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.next = []
        self.prev = None
    
    def set_next(self, Node):
        self.next.append(Node)
        return
    
    def get_next(self):
        return self.next
    
    def set_prev(self, Node):
        self.prev = Node
        return
    
    def get_prev(self):
        return self.prev



#queue_python.py
from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque()
        
    def enqueue(self,element):
        self.elements.append(element)
        print(f"Enqueue {element}")
    
    def dequeue(self):
        if not self.is_empty():
            element = self.elements.popleft()
            print(f"Dequeue {element}")
            return element
        else:    
            print("Queue is empty")
            return None
        
    def is_empty(self):
        return len(self.elements) == 0
    
    def size(self):
        return len(self.elements)
    
    def display_all(self):
        print("Queue: ",list(self.elements))
        
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.display_all()
    
    front_item = queue.dequeue()
    print("empty queue: ",queue.is_empty())     
    
    while not queue.is_empty():
        queue.dequeue()
        
    print("empty queue: ",queue.is_empty()) 
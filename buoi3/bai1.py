import sys
sys.stdout.reconfigure(encoding='utf-8')
class stack:
    def __init__(self):
        self.elements = []
    def push(self, item):
        self.elements.append(item)
        print(f"Pushed {item} into stack")
        
    def pop(self):
        if not self.is_empty():
            item = self.elements.pop()#pop the last element
            print(f"Popped {item} from stack")
            return item
        else:
            print("Stack is empty")
            return None
        
    def peak(self):
        if not self.is_empty():
            return self.elements[-1]
        else:
            print("Stack is empty")
            return None
        
    def is_empty(self):
        return len(self.elements) == 0
    def size(self):
        return len(self.elements)
    def display(self):
        print("Stack: ", self.elements[::-1])
        
if __name__ == '__main__':
    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.display()
    
    top_item = s.peak()
    print("Top item is: ", top_item)
    s.pop()
    s.display()
    print("Size of stack is: ", s.size())
    print("Is stack empty? ", s.is_empty())
    while(s.is_empty() == False):
        s.pop()
        
    print("Is stack empty? ", s.is_empty())
    s.display()
    top_item = s.peak()
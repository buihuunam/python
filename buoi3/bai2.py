class Stack:
    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)
        print(f"Pushed '{item}' to the stack")

    def pop(self):
        if not self.is_empty():
            item = self.elements.pop()
            print(f"Popped '{item}' from the stack")
            return item
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.elements[-1]
        else:
            print("Stack is empty")
            return None

    def is_empty(self):
        return len(self.elements) == 0

    def display(self):
        print("Stack:", self.elements)

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.display()

    top_item = s.peek()
    print("Top item:", top_item)
    s.pop()
    s.display()

    while not s.is_empty():
        s.pop()
    s.display()
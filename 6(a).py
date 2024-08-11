class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

my_stack = Stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Stack:", my_stack.items) 
print("Pop:", my_stack.pop())   
print("Stack:", my_stack.items)  
print("Peek:", my_stack.peek())  
print("Size:", my_stack.size())  

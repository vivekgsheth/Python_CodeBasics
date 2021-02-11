from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)
    
# Exercise 1

def reverse_string(s):
    stack = Stack()
    for ch in s:
        stack.push(ch)

    rstr = ''
    while not stack.is_empty():
        rstr += stack.pop()

    return rstr

def is_balanced(s):
    stack = Stack()
    
    for ch in s:
        if ch == '(' or ch == '{' or ch == '[':
            stack.push(ch)
        elif ch == ')':
            if not stack.is_empty() :
                char = stack.pop()
                if char != '(':
                    return False
            else:
                return False
        elif ch == ']':
            if not stack.is_empty() :
                char = stack.pop()
                if char != '[':
                    return False
            else:
                return False
        elif ch == '}':
            if not stack.is_empty() :
                char = stack.pop()
                if char != '{':
                    return False
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False


if __name__ == '__main__':
    #print(reverse_string("We will conquer COVID-19"))
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))

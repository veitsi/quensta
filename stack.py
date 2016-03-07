class Stack:
    def __init__(self):
        self.__data = []
    def push(self, value):
        self.__data.append(value)
    def top(self):
        return self.__data[-1]
    def pop(self):
        del self.__data[-1]
    def is_empty(self):
        return not self.__data
    def size(self):
        return len(self.__data)
s = Stack()
assert s is not None
assert s.is_empty()
s.push(1)
assert not s.is_empty()
assert s.top() == 1
s.pop()
assert s.is_empty()
s.push(1)
s.push(2)
assert s.size() == 2
assert s.top() == 2




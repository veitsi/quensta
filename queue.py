class Queue:
    def __init__(self):
        self.__data=[]
    def is_empty(self):
        return not self.__data
    def push_back(self,value):
        self.__data.append(value)
    def front(self):
        return self.__data[0]
    def pop_front(self):
        del self.__data[0]
    def size(self):
        return len(self.__data)
    def join_back(self,queue):
        self.__data.extend(queue.__data)
    def clear(self):
        self.__data=[]


queue=Queue()
assert queue is not None, "queue is empty"
assert queue.is_empty()

queue.push_back(1)
assert not queue.is_empty()
assert queue.front()==1

queue.pop_front()
assert queue.is_empty()

queue.push_back(2)
queue.push_back(3)
assert queue.front()==2
assert queue.size()==2

queue2=Queue()

queue2.push_back(4)
queue2.push_back(5)
assert queue2.size()==2

queue.join_back(queue2)
assert queue.size()==4
print(queue._Queue__data)
queue.clear()
assert queue.is_empty()
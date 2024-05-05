"""
VERSION 1 using 1 queue
"""
from collections import deque

class myStack:
    def __init__(self):
        self.q = deque()
    
    def push(self, x:int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        #pop every value except the last one and add it to the end of the queue
        #example: current stack - 1,2,3
            #pop(1), pop(2) and append to q
            #3,2,1  
        for i in range(len(self.q)-1):
            self.push(self.q.popleft())
        
        #return and pop the last value
        return self.q.popleft()
    
    def top(self) -> int:
        #return the last added element
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


"""
VERSION 2
"""
#implemeting queue
# https://realpython.com/queue-in-python/#stack-last-in-first-out-lifo

# from collections import deque

# class Queue:
#     def __init__(self):
#         self._elements = deque()
#         #_elements member variable of class Queue that is private 
#         # and should only be modified by the class itself

#     def enqueue(self, element):
#         self._elements.append(element)

#     def dequeue(self):
#         return self._elements.popleft()
    
# fifo = Queue()

# fifo.enqueue("1")
# fifo.enqueue("2")
# fifo.enqueue("3")

"""
VERSION 3
"""
# from collections import deque

# class Queue:
#     def __init__(self, *elements):
#         ## elements - optional arg of varied length iterable

#         self._elements = deque(elements)

#     def __len__(self):
#         return len(self._elements)
    
#     #size is reduced as we iterate over the queue
#     def __iter__(self):
#         while len(self)>0:
#             yield self.dequeue()

#     def enqueue(self, element):
#         self._elements.append(element)

#     def dequeue(self):
#         return self._elements.popleft()

# print("adding to queue: 1,2,3")
# fifo = Queue("1","2","3")

# len(fifo)
# print("poping from queue FIFO")
# for element in fifo:
#     print(element)

# len(fifo)

# class Stack(Queue):
#     def dequeue(self):
#         return self._elements.pop()


# print("adding to stack: 1,2,3")
# lifo = Stack("1","2","3")
# for element in lifo:
#     print(element)
# print("poping from stack LIFO")

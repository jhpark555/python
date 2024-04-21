
class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if self.isEmpty():
            return None 
        else :
            return self.stack.pop()
    def isEmpty(self):
        return len(self.stack)==0
        
class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if self.isEmpty():
            return None 
        else :
            return self.queue.pop(0)
    def isEmpty(self):
        return len(self.queue)==0
        
        
s=Stack()
s.push(10)
s.push(20)
s.push(30)
r=s.pop()
print(r)
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
r=q.dequeue()
print(r)


import queue
q=queue.Queue()
q.put("Hello ")
q.put("World ")
q.put("Fuck ")
while not q.empty():
    print(q.get(),end="")



        
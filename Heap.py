class Heap:
    def __init__(self):
        self.heap=[0]
        self.size=0
    def float(self,k):
        while k//2 >0:
            if self.heap[k] < self.heap[k//2]:
                self.heap[k],self.heap[k//2]=self.heap[k//2],self.heap[k]
            k //=2    
    def insert(self,item):
        self.heap.append(item)
        self.size +=1
        self.float(self.size)
    def minindex(self,k):
        if k*2+1 >self.size:
            return k*2
        elif self.heap[k*2+1] > self.heap[k*2]:
            return k*2
        else:
            return k*2+1
    def sink(self,k):
        while k*2 <=self.size:
            mi=self.minindex(k)
            if self.heap[k]> self.heap[mi]:
                self.heap[k],self.heap[mi] = self.heap[mi],self.heap[k]
            k=mi
    def pop(self):
        item=self.heap[1]
        self.heap[1]=self.heap[self.size]
        self.size -=1
        self.heap.pop()
        self.sink(1)
        return item
        

   
h=Heap()
for i in (4, 8, 7, 2, 9, 10, 5, 1, 3, 6):
    h.insert(i)
x=h.pop()
print(x)
print(h.heap)

    
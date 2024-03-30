class Ourheap:
    def __init__(self,items):
        self.heap=[None]
        self.rank={}
        for x in items:
            self.push(x)
            #print(x)

    def __len__(self):
        return len(self.heap)-1
    
    def push(self,x):
        assert x not in self.rank
        i=len(self.heap)
        self.heap.append(x)   # add new leaf
        self.rank[x]=i
        self.up(i)

    def pop(self):
        root=self.heap[1]
        del self.rank[root]
        x=self.heap.pop()     # last leaf 
        if self:
            self.heap[1]=x    #move leaf to root
            self.rank[x]=1
            self.down(1)
        return root
    
    def up(self,i):
        x=self.heap[i]
        while i>1 and x<self.heap[i//2]:    # child is less than parent
            self.heap[i]=self.heap[i//2]    #swap
            self.rank[self.heap[i//2]]=i
            i //=2
        self.heap[i]=x
        self.rank[x]=i

    def down(self,i):
        x=self.heap[i]
        n=len(self.heap)
        while True:
            left=2*i
            right=left+1
            if( right<n and self.heap[right]<x and self.heap[right] < self.heap[left]):
                self.heap[i]=self.heap[right]     # swap with min
                self.rank[self.heap[right]]=i
                i=right
            elif left<n and self.heap[left]<x:
                self.heap[i]=self.heap[left]
                self.rank[self.heap[left]]=i    #move left childup
                i=left
            else:
                self.heap[i]=x
                self.rank[x]=i
                return
            
    def update(self,old,new):        
        i=self.rank[old]
        del self.rank[old]
        self.heap[i]=new
        self.rank[new]=i
        if old< new:
            self.down(i)
        else:
            self.up(i)
    
    def show(self):
        l=len(self.heap)
        for i in range(1,l):
            print(self.heap[i])
    

H=Ourheap([2,5,7,13,9,8,30,20,17,11,12,15])
#H.update(2,5)
H.show()
x=H.pop()
print(x)



    
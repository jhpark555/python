from newarray import Array

class Maxheap:
    def __init__(self,maxSize):
        self._elements=Array( maxSize)
        self._count =0
    def __len__(self):
        return self._count
    def capacity(self):
        return len(self._elements)
    def add(self,value):
        assert self._count < self.capacity(), "Cannot add to a full heap"
        self._elements[self._count]=value
        self._count +=1
        self._shiftUp(self._count -1)
    def extract(self):
        assert self._count >0, "Cannot extract from an empty heap"
        value=self._elements[0]
        self._count -=1
        self._elements[0]=self._elements[self._count]
        self._shiftDown(0)
        return value

    def _shiftUp(self,ndx):
        if ndx>0 :
            parent = (ndx-1)//2
            if self._elements[ndx] > self._elements[parent]:
                tmp=self._elements[ndx]
                self._elements[ndx]=self._elements[parent]
                self._elements[parent]=tmp
                self._shiftUp(parent)
    def _shiftDown(self,ndx):
        left=2*ndx+1
        right=2*ndx+2
        largest=ndx
        if left< self._count and self._elements[left] >=self._elements[largest]:
            largest =left
        if right< self._count and self._elements[right]>=self._elements[largest]:
            largest =right

        if largest !=ndx:
            #swap(self._elements[ndx],self._elements[largest])
            tmp=self._elements[ndx]
            self._elements[ndx]=self._elements[largest]
            self._elements[largest]=tmp
            self._shiftDown(largest)


def simpleHeapSort(theSeq):
    n=len(theSeq)
    heap=Maxheap(n)
    buff=Array(n)

    for item in theSeq:
        heap.add(item)

    #for i in heap._elements:
    #    print(i)

    for i in range(n-1,-1,-1):       # extract from max value
        theSeq[i]=heap.extract()

    

list=[51,10,2,18,4,31,13,5,23,64,29]

simpleHeapSort(list)
print(list)



m=Maxheap(20)
m.add(100)
m.add(84)
m.add(71)
m.add(60)
m.add(23)
m.add(12)
m.add(29)
m.add(1)
m.add(37)
m.add(4)
#m.add(101)
#m.add(72)

#for i in m._elements:
#    if i is not None:
#        print(i)

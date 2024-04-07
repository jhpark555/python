from llistqueue import Queue
from newarray import Array

def radixSort(intList,numDigits):
    binArray = Array(10)
    for k in range(10):
        binArray[k]=Queue()

    column=1
    
    for d in range(numDigits):
        for key in intList:
            digit=(key//column) %10
            binArray[digit].enqueue(key)
            #print(binArray[digit])
        print("len=",len(binArray))
        i=0
        for bin in binArray:
            while not bin.isEmpty() :
                intList[i]=bin.dequeue()
                print(intList[i])
                i +=1
        column *=10

x=[23,10,18,51,5,13,31,54,48,62,29,8,37]
radixSort(x,2)
print(x)

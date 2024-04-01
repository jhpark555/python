def insertionSort(theSeq):
    n = len(theSeq)

    for i in range(1,n):
        value=theSeq[i]

        pos=i
        while pos>0 and value < theSeq[pos-1]:
            theSeq[pos]=theSeq[pos-1]
            pos -=1

        theSeq[pos]=value


list=[9,8,7,6,5,4,3]
insertionSort(list)
print(list)
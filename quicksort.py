def recQuickSort(theSeq,first,last):
    if first >=last:
        return
    else :
        pivot=theSeq[first]

        pos=partitionSeq(theSeq,first,last)

        recQuickSort( theSeq,first,pos-1)
        recQuickSort(theSeq,pos+1,last)

def partitionSeq(theSeq,first,last):
    pivot=theSeq[first]

    left=first+1
    right=last

    while left<=right:
        while left< right and theSeq[left] < pivot:
            left+=1
        while right>=left and theSeq[right] >=pivot:
            right-=1
        
        if left< right:
            tmp=theSeq[left]
            theSeq[left]=theSeq[right]
            theSeq[right]=tmp

    if right!=first:
        theSeq[first]=theSeq[right]
        theSeq[right]=pivot
    
    return right



def quicksort(theSeq):
    n=len(theSeq)
    recQuickSort(theSeq,0,n-1)



l=[10,23,51,18,4,31,5,13]
quicksort(l)
print(l)
        
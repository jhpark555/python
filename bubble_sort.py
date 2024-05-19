def bubblesort(theValue):
    n=len(theValue)

    for i in range(n):
        for j in range(n-i-1) :
            if theValue[j]> theValue[j+1]:
                temp=theValue[j]
                theValue[j]=theValue[j+1]
                theValue[j+1] =temp

list=[9,8,7,6,5,4,3]
bubblesort(list)
print(list)


def partition(array,first,last):
    pivot= array[first]
    pivot_index=first
    pivot_index1=first+1
    last_index=last

    while True:
        while array[pivot_index1]< pivot and pivot_index1 <last:
            pivot_index1 +=1
        while array[last_index] >pivot and last_index >first:
            last_index -=1
        if pivot_index1 < last_index:
            temp=array[pivot_index1] 
            array[pivot_index1]=array[last_index]
            array[last_index]=temp  
        else: break
    
    array[pivot_index]=array[last_index]   #swap pivot and last_index
    array[last_index]=pivot

    return last_index

def quick_sort(array,first,last):
    if first> last:
        return
    else:
        partition_point=partition(array,first,last)
        quick_sort(array,first,partition_point-1)
        quick_sort(array,partition_point+1,last)

def quick_select(array,left,right,k):

    split = partition(array,left,right)
    if split==k:
        return array[split]
    elif split < k:
        return quick_select(array,split+1,right,k)
    else:
        return quick_select(array,left,split-1,k)



l=[43,3,20,89,4,77]
quick_sort(l,0,len(l)-1)
print(l)
r=quick_select(l,0,len(l)-1,1)
print(r)




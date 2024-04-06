
def mergeSortedLists(lista,listb):
    newList =list()
    a=0
    b=0

    while a<len(lista) and b< len(listb):
        if lista[a] < listb[b]:
            newList.append(lista[a])
            a +=1
        else :
            newList.append(listb[b])
            b +=1

    while a<len(lista):
        newList.append(lista[a])
        a+=1
    while b<len(listb):
        newList.append(listb[b])
        b +=1

    return newList


def pythonMergeSort(theList):
    if len(theList) <=1:
        return theList
    else:
        mid=len(theList)//2

        leftHalf=pythonMergeSort(theList[:mid])
        rightHalf=pythonMergeSort(theList[mid:])

        newList=mergeSortedLists(leftHalf,rightHalf)
        print(newList)
        return newList
    

l=[6,4,5,2,8,9,1,10]
s=pythonMergeSort(l)
print(s)
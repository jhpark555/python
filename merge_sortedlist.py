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

a=[1,2,3,4]
b=[5,6,7,8]

c=mergeSortedLists(a,b)
print(c)
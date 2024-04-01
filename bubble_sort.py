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

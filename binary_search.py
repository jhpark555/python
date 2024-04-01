def binarySearch(theValue,target):
    low=0
    high=len(theValue)-1

    while low<=high:
        mid = (high+low) //2

        if theValue[mid] ==target:
            return True
        elif theValue[mid] > target:
            high = mid-1
        else:
            low=mid+1
    return False

list=[1,2,3,4,5,6,7,8]
print(binarySearch(list,9))

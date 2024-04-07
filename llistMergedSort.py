def llistMergedSort(theList):
    if theList is None:
        return None
    
    rightList=_splitLinkedList(theList)
    leftList=theList

    leftList=llistMergedSort(leftList)
    rightList=llistMergedSort(rightList)

    theList=_mergedLinkedLists( leftList,rightList)

    return theList

def _splitLinkedList(subList):
    midPoint=subList
    curNode=midPoint.next

    while curNode is not None:
        curNode=curNode.next
        if curNode is not None:     # 2 jump node faster than sing jump
            midPoint=midPoint.next
            curNode=curNode.next
    rightList=midPoint.next
    midPoint.next=None
    return rightList

""""
def _splitLinkedList(subList):
    curNode=subList
    dcurNode=subList
    
    while dcurNode.next.next is not None:
        dcurNode=dcurNode.next.next
        #print(dcurNode.data)
        curNode=curNode.next
    rightList=curNode.next
    #tmp=rightList
    #while tmp is not None:
    #    print(tmp.data)
    #    tmp=tmp.next
    curNode.next=None
    return rightList
"""
def _mergedLinkedLists(subListA,subListB):
    newList =ListNode(None)
    newTail=newList

    while subListA is not None and subListB is not None:
        if subListA.data <=subListB.data:
            newTail.next=subListA
            subListA=subListA.next
        else:
            newTail.next=subListB
            subListB=subListB.next
        newTail=newTail.next
        newTail.next=None

    if subListA is not None:
        newTail.next=subListA
    else:
        newTail.next=subListB

    return newList.next
        

class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None


a=ListNode(23)
b=ListNode(51)
c=ListNode(2)
d=ListNode(18)
e=ListNode(4)
f=ListNode(31)

a.next=b
b.next=c
c.next=d
d.next=e
e.next=f

llistMergedSort(a)
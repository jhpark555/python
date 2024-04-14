from bstmap import *

LEFT_HIGH =1
EQUAL_HIGH =0
RIGHT_HIGH =-1

class AVLMap:
    def __init__(self):
        self._root=None
        self._size=0
    def __len__(self):
        return self._size
    def __contains__(self,key):
        return self._bstSearch(self._root,key) is not None
    def _bstSearch(self,subtree,target):
        if subtree is None:
            return None
        elif target < subtree.key:
            return self._bstSearch(subtree.left,target)
        elif target > subtree.key:
            return self._bstSearch(subtree.right,target)
        else :
            return subtree  
    def add(self,key,value):
        node =self._bstSearch(self._root,key)
        if node is not None:
            node.value=key
            return False
        else :
            (self._root,tmp)=self._avlInsert(self._root,key,value)
            #print(node.key)
            self._size +=1
            return True
    def valueOf(self,key):
        node =self._bstSearch(self._root,key)
        assert node is not None, "Invalid map key"
        return node.value
    
    def getheight(self,subtree):
        if subtree is None:
            return None
        return subtree.taller            
            
            
            
    def remove(self,key):
        #assert key in self, "Invalid map key"
        (self._root,tmp) =self._avlRemove(self._root,key)
        self._size -=1
    def __iter__(self):
        return _BSTMapIterator(self._root)
    
    def inorder(self,subtree):
        if subtree is not None:
            self.inorder(subtree.left)
            print(subtree.key)
            self.inorder(subtree.right)

    def _avlRotateRight(self,pivot):
        C=pivot.left
        pivot.left=C.right
        C.right=pivot
        return C
    def _avlRotateLeft(self,pivot):
        C=pivot.right
        pivot.right=C.left
        C.left=pivot
        return C
    
    def _avlLeftBalance(self,pivot):
        C=pivot.left
        if C.bfactor==LEFT_HIGH:
            pivot.bfactor=EQUAL_HIGH
            C.bfactor=EQUAL_HIGH
            pivot=self._avlRotateRight(pivot)
            return pivot
        else:
            G=C.right
            if G.bfactor==LEFT_HIGH:
                pivot.bfactor=RIGHT_HIGH
                C.bfactor=EQUAL_HIGH
            elif G.bfactor==EQUAL_HIGH:
                pivot.bfactor=EQUAL_HIGH
                C.bfactor=EQUAL_HIGH
            else: #G.bfactor=RIGHT_HIGH
                pivot.bfactor=EQUAL_HIGH
                C.bfactor=LEFT_HIGH
            G.bfactor =EQUAL_HIGH
            print("L")
            pivot.left=self._avlRotateLeft(C)
            pivot=self._avlRotateRight(pivot)
            return pivot

        
    def _avlRightBalance(self,pivot):
        C=pivot.right
        if C.bfactor==RIGHT_HIGH:
            pivot.bfactor=EQUAL_HIGH
            C.bfactor=EQUAL_HIGH
            pivot=self._avlRotateLeft(pivot)
            return pivot
        else:
            G=C.left
            if G.bfactor==RIGHT_HIGH:
                pivot.bfactor=LEFT_HIGH
                C.bfactor=EQUAL_HIGH
            elif G.bfactor==EQUAL_HIGH:
                pivot.bfactor=EQUAL_HIGH
                C.bfactor=EQUAL_HIGH
            else: #G.bfactor=LEFT_HIGH
                pivot.bfactor=EQUAL_HIGH
                C.bfactor=RIGHT_HIGH
            G.bfactor =EQUAL_HIGH
            print("R")
            pivot.left=self._avlRotateRight(C)
            pivot=self._avlRotateLeft(pivot)
            return pivot
        
    def _avlInsert(self,subtree,key,newItem):
        if subtree is None:
            subtree=_AVLTreeNode(key,newItem)
            print("#",subtree.key)
            taller= True
        elif key==subtree.key:
            return (subtree,False)
        elif key< subtree.key:
            (subtree,taller) = self._avlInsert(subtree.left,key,newItem)
            if taller:
                if subtree.bfactor ==LEFT_HIGH:
                    subtree=self._avlLeftBalance(subtree)
                    taller=False
                elif subtree.bfactor==EQUAL_HIGH:
                    subtree.bfactor=LEFT_HIGH
                    taller=True
                else :  #Right_HIGH
                    subtree.bfactor=EQUAL_HIGH
                    taller=False
        else :# key> subtree.key
            (subtree, taller) = self._avlInsert(subtree.right,key,newItem)
            if taller :
                if subtree.bfactor == LEFT_HIGH:
                    subtree.bfactor=EQUAL_HIGH
                    taller=False
                elif subtree.bfactor ==EQUAL_HIGH:
                    subtree.bfactor=RIGHT_HIGH
                    taller =True
                else : #RIGHT_HIGH
                    subtree=self._avlRightBalance(subtree)
                    taller= False
        return (subtree,taller)


    

class _AVLTreeNode:
    def __init__(self,key,value):
        self.key =key
        self.data=value
        self.bfactor=EQUAL_HIGH
        self.left=None
        self.right=None


A=AVLMap()
A.add(60,60)
A.add(25,25)
A.add(100,100)
A.add(17,17)
A.add(30,30)
A.add(80,80)
A.add(120,120)
A.add(28,28)
A.add(35,35)
#A.remove(17)
A.inorder(A._root)

from newarray import Array
from lliststack import Stack

class BSTMap:
    def __init__(self):
        self._root=None
        self._size=0
    def __len__(elf):
        return self._size
    def __iter__(self):
        return _BSTMapIterator(self._root,self._size)
    def __contains__(self,key):
        return self._bstSearch(self._root,key) is not None
    def valueOf(self,key):
        node =self._bstSearch(self._root,key)
        assert node is not None, "Invalid map key"
        return node.value    
    def _bstSearch(self,subtree,target):
        if subtree is None:
            return None
        elif target < subtree.key:
            return self._bstSearch(subtree.left,target)
        elif target > subtree.key:
            return self._bstSearch(subtree.right,target)
        else :
            return subtree    
    def _bstMinimum(self,subtree):
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self._bstMinimum(subtree.left)
        
    def add(self,key,value):
        node =self._bstSearch(self._root,key)
        if node is not None:
            node.value = value
            return False
        else:
            self._root=self._bstInsert(self._root,key,value)
            self._size +=1
            return True
    def _bstInsert(self,subtree,key,value):
        if subtree is None:
            subtree=_BSTMapNode(key,value)
        elif key < subtree.key:
            subtree.left=self._bstInsert(subtree.left,key,value)
        elif key > subtree.key:
            subtree.right =self._bstInsert(subtree.right, key,value)
        return subtree
    def remove(self,key):
        assert key in self, "Invalid map key"
        self._root =self._bstRemove(self._root,key)
        self._size -=1
    def _bstRemove(self,subtree,target):
        if subtree is None:
            return subtree
        elif target <subtree.key:
            print("L",subtree.key)
            subtree.left=self._bstRemove(subtree.left,target)
            return subtree
        elif target > subtree.key:
            print("R",subtree.key)
            subtree.right=self._bstRemove(subtree.right,target)
            return subtree
        else :
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None or subtree.right is None:
                if subtree.left is not None:
                    return subtree.left
                else :
                    return subtree.right
            else :
                print("#",subtree.right.key)
                successor = self._bstMinimum(subtree.right)
                print("*",successor.key)
                subtree.key =successor.key
                subtree.value=successor.value
                subtree.right = self._bstRemove(subtree.right, successor.key)
                return subtree
    def inorder(self,subtree):
        if subtree is not None:
            self.inorder(subtree.left)
            print(subtree.key)
            self.inorder(subtree.right)


class _BSTMapNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.left=None
        self.right=None


class _BSTMapIterator:
    def __init__(self,root,size):
        self._theKeys= Array(size)
        self._curItem=0
        self._bstTraversal(root)
    def __iter__(self):
        return self
    def __next__(self):
        if self._curItem < len(self._theKeys):
            key = self._theKeys[self._curItem]
            self._curItem +=1
            return key
        else:
            raise StopIteration
    def _bstTraversal( self,subtree):    #inorder trav
        if subtree is not None:
            self._bstTraversal( subtree.left)
            self._theKeys[self._curItem] = subtree.key
            print(subtree.key)
            self._curItem +=1
            self._bstTraversal(subtree.right)

'''
class _BSTMapIterator:
    def __init__(self,root,size):
        self._theStack = Stack()
        self._traverseToMinNode(root,size)
    def __iter__(self):
        return self
    def __next__(self):
        if self._theStack.isEmpty():
            raise StopIteration
        else :
            node =self._theStack.pop()
            print(key)
            print(key)           
            if node.right is not None:
                self._traverseToMinNode(node.right)
    def _traverseToMinNode(self,subtree,size):
        if subtree is not None:
            self._theStack.push( subtree)
            self._traverseToMinNode(subtree.left,size)
 '''       
    




T=BSTMap()
T.add(60,60)
T.add(12,12)
T.add(90,90)
T.add(4,4)
T.add(41,41)
T.add(71,71)
T.add(100,100)
T.add(1,1)
T.add(29,29)
T.add(84,84)
T.add(23,23)
T.add(37,37)

T.remove(12)
#T.inorder(T._root)
T.__iter__()
class Tree:
    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by subclass')
        def __eq__(self,other):
            raise NotImplementedError('must be implemented by subclass')
        def __ne__(self,other):
            return not (self==other)
    def root(self):
        raise NotImplementedError('must be implemented by subclass')
    def parent(self,p):
        raise NotImplementedError('must be implemented by subclass')
    def num_children(self,p):
        raise NotImplementedError('must be implemented by subclass')
    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')
    def is_root(self,p):
        return self.root==p    
    def is_leaf(self,p):
        return self.num_of_children(p)==0
    def is_empty(self,p):
        return len(self)==0
    
class BinaryTree(Tree):
    def left(self,p):
        raise NotImplementedError('must be implemented by subclass')
    def right(self,p):
        raise NotImplementedError('must be implemented by subclass')
    def sibling(self,p):
        parent=self.parent(p)
        if parent is None:
            return None
        else:
            if p==self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)           
    def children(self,p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slot__='_element','_parent','_left','_right'
        def __init__(self,element,parent=None,left=None,right=None):
            self._element=element
            self._parent=parent
            self._left=left
            self._right=right
    class Pisition(BinaryTree.Position):
        def __init__(self,container,node):
            self._container=container
            self._node=node
        def element(self):
            return self._node._element
        def __eq__(self,other):
            return type(other) is type(self) and other._node is self._node
    def _validate(self,p):
        if not isinstant(p,self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p must not belong to this container')
        if p._node._parent is p._node :
            raise ValueError('p must no longer valid')
        return p._node
    def _make_position(self,node):
        return self.Position(self,node) if node is not None else None
    def __init__(self):
        self._root=None
        self._size=0
    def __len__(self):
        return self._size
    def root(self):
        return self._make_position(self.root)
    def parent(self,p):
        node =self._validate(p)
        return self._make_position(node._parent)
    def left(self,p):
        node =self._validate(p)
        return self._make_position(node._left)
    def right(self,p):
        node =self._validate(p)
        return self._make_position(node._right)
    def num_children(self,p):
        node =self._validate(p)
        count=0
        if node._left is not None:
            cpunt +=1
        if node._right is not None:
            coubt +=1
        return count





            

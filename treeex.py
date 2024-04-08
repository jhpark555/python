class _BinTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def preorderTrav(subtree):
    if subtree is not None:
        print(subtree.data)
        preorderTrav(subtree.left)
        preorderTrav(subtree.right)

def inorderTrav(subtree):
    if subtree is not None:
        inorderTrav(subtree.left)
        print(subtree.data)
        inorderTrav(subtree.right)

def postorderTrav(subtree):
    if subtree is not None:
        postorderTrav(subtree.left)
        postorderTrav(subtree.right)
        print(subtree.data)

t=_BinTreeNode('T')
x=_BinTreeNode('X')
c=_BinTreeNode('C')
b=_BinTreeNode('B')
g=_BinTreeNode('G')
j=_BinTreeNode('J')
r=_BinTreeNode('R')
z=_BinTreeNode('Z')
k=_BinTreeNode('K')
m=_BinTreeNode('M')
t.left=x
t.right=c
x.left=b
x.right=g
c.left=j
c.right=r
g.left=z
r.left=k
r.right=m


#preorderTrav(t)
#inorderTrav(t)
postorderTrav(t)
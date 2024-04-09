from arrayqueue import Queue

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

def breadthFirstTrav(bintree):
    q=Queue(10)
    q.enqueue(bintree)
    #print("*",bintree.data)

    while not q.isEmpty():
        node=q.dequeue()
        print(node.data)

        if node.left is not None:
            q.enqueue(node.left)
        if node.right is not None:
            q.enqueue(node.right)





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
#postorderTrav(t)
breadthFirstTrav(t)
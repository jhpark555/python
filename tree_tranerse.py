def preorder(self):
    if not self.is_empty():
        for p in self._subtree_preorder(self.root()):
            yield p
            
def _subtree_preorder(self,p):
    yield(p)
    for c in self.children(p):
        for other in self._subtree_preorder(c):
            yield other
            
def postorder(self):
    if not self.is_empty():
        for p in self._subtree_postorder(self.root()):
            yield p
            
def _subtree_postorder(self,p):
    for c in self.children(p):
        for other in self._subtree_postorder(c):
            yield other
        yield p
        
def breadthfirst(self):
    if not self.is_empty():
        fringe=LinkedQueue()
        fringe.enqueue(self.root())
        while not fringe.is_empty():
            p=fringe.dequeue()
            yield p
            for c in self.children(p):
                frige.enqueue(c)
                
def inorder(self):
    if not self.is_empty():
        for p in self._subtree_inorder(self.root()):
            yield p
def _subtree_inorder(self,p):
    if self.left(p) is not None:
        for other in self._subtree_inorder(self.left(p)):
            yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other
                
def positions(self):
    return self.inorder(self)


            

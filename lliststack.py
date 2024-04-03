class Stack:
    def __init__(self):
        self._top=None
        self._size=0
    def isEmpty(self):
        return self._top is None
    def __len__(self):
        return self._size
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stak"
        return self._top.item
    def pop(self):
        assert not self.isEmpty(), "Cannot pop at an empty stack"
        node =self._top
        self._top=self._top.next
        self._size -=1
        return node.item
    def push(self,item):
        self._top=_StackNode(item,self._top)
        self._size +=1
class _StackNode:
    def __init__(self,item,link):
        self.item=item
        self.next=link

s=Stack()
s.push(10)
s.push(20)
#x=s.pop()
print(len(s))

values=Stack()
for i in range(16):
    if i%3 ==0:
        values.push(i)
        print(values.peek())


def isValidSource(srcfile):
    s=Stack()

    for line in srcfile:
        for token in line:
            if token in "{[(":
                s.push(token)
            elif token in "}])":
                if s.isEmpty():
                    return False
                else :
                    left =s.pop()
                    if (token=="}" and left !="{") or \
                       (token=="]" and left !="[" ) or \
                       (toekn==")" and left!="(") :
                        return False
    return s.isEmpty()
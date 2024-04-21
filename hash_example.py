hash_table=[None]*10
def insert(key,value):
    index=hash(key)
    hash_table[index]=value
    #print(index)

def get(key):
    index=hash(key)
    return hash_table[index]

class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
class HashTable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*self.size
    def hash(self,key):
        return key%self.size
    def insert(self,key,value):
        index=self.hash(key)
        print('#',index)
        node=Node(key,value)
        if self.table[index]==None:
            self.table[index]=node
        else :
            cur=self.table[index]
            while cur.next is not None:
                cur=cur.next
            cur.next=node
    def get(self,key):
        index=self.hash(key)
        cur=self.table[index]
        while cur is not None:
            if cur.key ==key:
                return cur.value
            else:
                cur=cur.next
        return None


h=HashTable(3)

h.insert(1,2)
h.insert(3,4)
h.insert(5,6)
h.insert(7,8)

print(h.get(3))
#for i in range(len(hash_table)):
#   print(i,hash_table[i])
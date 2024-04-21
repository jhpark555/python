class HashTable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*self.size
    def hash(self,key):
        return key%self.size
    def insert(self,key,value):
        index=self.hash(key)
        if self.table[index]==None:
            self.table[index]=(key,value)
        else :
            i= (index+1)%self.size
            while i!=index and self.table[i]!=None:
                i=(i+1)%self.size
            if i==index:
                return False
            else :
                self.table[i]=(key,value)
        return True
    def get(self,key):
        index=self.hash(key)
        if self.table[index]==None:
            return None
        else :
            i=index
            while i!=(index+1)% self.size and self.table[i]!=None and \
            self.table[i][0]!=key:
                i=(i+1)%self.size
            if i==(index+1)%self.size:
                return None
            else:
                return self.table[i][1]


h=HashTable(10)

h.insert(1,2)
h.insert(3,4)
h.insert(5,6)
h.insert(7,8)

print(h.get(7))

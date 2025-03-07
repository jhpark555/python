class HashItem:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        
class HashTable:
    def __init__(self):
        self.size=10
        self.slots=[None for i in range(self.size)]
        self.count=0
        self.MAXLOADFACTOR=0.65
        self.prime_num=5
        
    def _hash(self,key):
        mult=1
        hv=0
        for ch in key:
            hv +=mult* ord(ch)
            mult +=1
        return hv %self.size
    
    def put(self,key,value):
        item=HashItem(key,value)
        h=self._hash(key)
        while self.slots[h] !=None:
            if self.slots[h].key==key:
                break
            h=(h+1) % self.size
        if self.slots[h]==None:
            self.count +=1
        self.slots[h]=item
        self.check_growth()
        
    def put_quadratic(self,key):
        item=HashItem(key,valuse)
        h=self._hash(key)
        j=1
        while self.slots[h] !=None:
            if self.slots[h].key==key:
                break
            h=(h+j*j) % self.size
            j +=1
        if self.slots[h]==None:
            self.count +=1
        self.slots[h]= item
        self.check_growth()
        
        
    def check_growth(self):
        loadfactor = self.count/ self.size
        if loadfactor > self.MAXLOADFACTOR:
            print("Load factor before growing the hash table", self.count
/ self.size )
            self.growth()
        else:
            print("Load factor after growing the hash table", self.count /
self.size )
            
    def growth(self):
        New_Hash_Table=HashTable()
        New_Hash_Table.size =2*self.size
        New_Hash_Table.slots= [None for i in range(New_Hash_Table.size)]
        
        for i in range(self.size):
            if self.slots[i]!=None:
                New_Hash_Table.put(self.slots[i].key, self.slots[i].value)
                
        self.size=New_Hash_Table.size
        self.slots=New_Hash_Table.slots
    
    def get(self,key):
        h=self._hash(key)
        
        while self.slots[h] !=None:
            if self.slots[h].key ==key:
                return self.slots[h].value
            else:
                h=(h+1)% self.size
        return None
    
    def get_quadratic(self,key):
        h=self._hash(key)
        j =1
        while self.slots[h]!=Node:
            if self.slots[h].key==key:
                return self.slots[h].value
            h=(h+j*j) %self.size
            j +=1
        return Node
    
    def __setitem__(self,key,value):
        self.put(key,value)
        
    def __getitem__(self,key):
        return self.get(key)
    
    def h2(self,key):
        mult=1
        hv=0
        for ch in key:
            hv +=mult*ord(ch)
            mult +=1
        return hv
    
    def put_double_hashing(self,key,value):
        item =HashItem(key,value)
        h=self._hash(key)
        j=1
        while self.slots[h]!=None:
            if self.slots[h].key==key:
                break
            h=(h+j*(self.prime_num) -(self.h2(key) %self.prime_num)) %self.size
            j=j+1
        if self.slots[h]==None:
            self.count +=1
        self.slots[h]=item
        self.check_growth()
    
    def get_double_hashing(self,key):
        h=self._hash(key)
        j=1
        while self.slots[h]!=None:
            if self.slots[h].key==key:
                return self.slots[h].value
            h=(h+j*(self.prime_num) -(self.h2(key) %self.prime_num)) %self.size
            j=j+1
        return None
    
        
    
    
        
            
ht=HashTable()
ht.put_double_hashing("good","eggs")
ht.put_double_hashing("better","spam")
ht.put_double_hashing("best","cool")
ht.put_double_hashing("ad","donot")
ht.put_double_hashing("ga","collide")
ht.put_double_hashing("awd","hello")
ht.put_double_hashing("add","ok")
ht.check_growth()

#for key in ("good","better","best","worst","ad","ga"):
#    v= ht.get(key)
#    print(v)
    
for key in ("good","better","best","worst","ad","ga"):
    #v=ht[key]
    v=ht.get_double_hashing(key)
    print(v)
print("The Number of element is: {}".format(ht.count))


    

class Map:
    def __init__(self):
        self._entryList=list()
    def __len__(self):
        return len(self._entryList)
    def __contains__(self,key):
        ndx=self._findPosition(key)
        return ndx is not None
    def add(self,key,value):
        ndx=self._findPosition(key)
        if ndx is not None:
            self._entryList[ndx].value=value
            return False
        else :
            entry=_MapEntry(key,value)
            self._entryList.append(entry)
            return True
    def valueOf(self,key):
        ndx=self._findPosition(key)
        assert ndx is not None,"Invalid map of key"
        return self._entryList[ndx].value
    def remove(self,jey):
         ndx=self._fincPosirtion(key)
         assert ndx is not None, "Invalid map key"
         self._entryList.pop(ndx)
    def __iter__(self):
        return _MapIterator(self._entryList)
    def _findPosition(self,key):
        for i in range(len(self)):
            if self._entryList[i].key==key:
                return i
        return None
        
class _MapEntry:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        
        
M=Map()
M.add("1",10)
M.add("2",20)

print(M.valueOf("1"))


        
        

from qUeue import *

class LRU:
    def __init__(self, elements):
        self.lru = queue(elements)
        self.length = elements
        

    def put(self,key, value):
        elements, track = self.lru.getter()
        flag = False
        if track > -1:
                for k, instance in elements:
                        if key == k:
                            self.lru.delete([k,instance])
                            flag = True
                            break
                if not flag and track == self.length-1:
                            self.lru.pop()
                            
        self.lru.push([key, value])

    def get(self, key):
         elements, track = self.lru.getter()
         flag = False
         if track >-1:
            for k, val in elements:
                if k == key:
                    flag = True
                    #ind = elements.index([k,val])
                    instance = [k,val]
                    self.lru.delete(instance)      
            if flag:
                 self.lru.push(instance)
                 return instance[1]
            else:
                 return -1
    def __str__(self):
        elements, track = self.lru.getter()
        return str(elements)
    

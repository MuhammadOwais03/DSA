from LRUcahe import *

l = LRU(2)
l.put(1,1)
l.put(2,2)
l.put(1,6)
print("Value Of key 1: ", l.get(1))
l.put(3,3)
l.put(4,4)
print("Value of Key 3: ", l.get(3))
print("Value Of Key 4: ", l.get(4))
print("Value Of Key 5: ", l.get(5))



print(l)

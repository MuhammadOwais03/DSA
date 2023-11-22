from classDLL import *

head = doubleNode(1)

head.append(90)

head.append(6)
head.append(7)

head.append(9)
head.append(3)
head.append(11)
head.append(2)
head.insertBefore(11, 10)
head.insertBefore(2, 100)
head.inserHead(0)



# Maximum Number In DLL

def MaxDList(head):
    h = head
    max_ = 0
    while h is not None:
        if h.data > max_:
            max_ = h.data
        h = h.next
    return max_

# Bubble Sort In DLL

def sortDLL(head):
    h = head
    count = h.len()
    while h.prev is not None:
        h = h.prev
    for i in range(count-1):
        h = head
        for j in range(0, count-i-1):
            if h.next is not None and h.data > h.next.data:
                h.data, h.next.data = h.next.data, h.data
            if h.next is not None:
                h = h.next
            else:
                break
                 
    return head





print("Original: ", head)

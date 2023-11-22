from classSLL import *

def deleteNode(head, target):
    res = head.search(target)
    if res[0]:
        if res[2] is head:
            print("E1")
            head=head.next
        else:
            print("E2")
            res[1].delete()
    return head

def insertBefore(head, value, where):
    res = head.search(where)
    if res[0]:  
        if res[2] == head:
            newHead = listNode(value)
            newHead.next = head
            head = newHead
        else:
            res[1].insert(value)
    return head

def buildListNode(val):
    assert len(val) > 0
    head = listNode(val[0])
    for i in range(1, len(val)):
        head.append(val[i])
    return head

def circularLinkList(head):
    a = head
    while a.next is not None:
        a = a.next
    a.next = head
    

def traverseCircular(head):
    a = head
    while a.next is not head:
        print(a.data)
        a = a.next
    print(a.data)
    



# Assignment Question 1 !
def deleteAllInstance(head, value):
    a = head
    while a is not None and a.data == value:
        a = a.next
    b = a
    while b is not None:
        if b.next is not None and b.next.data == value:
            b = deleteNode(b, value)
        else:
            b = b.next
    return a

# Assignment Question 2 !

def count_x(head, target):
    a = head
    i = 0
    while a is not None:
        if a.data == target:
            i += 1
        a = a.next
    return i

# Assignment Question 3 !
def del_tail(head):
    a = head
    while a.next is not None:
        a = a.next
    res = head.search(a.data)
    if res[0]:
        res[1].delete()

# Assignment Question 4 !
def combine(head1, head2):
    a = head1
    b = head2
    while a.next is not None:
        a = a.next
    a.next = b
    return head1

# Assignment Question 5 !
def splitList(head):
    a = head
    b = None
    while a is not None and a.data > 0:
        a = a.next
    if a is not None and a.data < 0:
        b = a.next
        a.next = None
    return head, b

# Assignment Question 6 !
def insB4Tail(head, value):
    a = head
    new = listNode(value)
    while a.next is not None:
        b = a
        a = a.next
    b.next = new
    new.next = a
    return head

# Assignment Question 7 !

def newHead(head, value):
    a = head
    new = listNode(value)
    new.next = a
    return new

def insClist(head, x, y):
    a = head
    n1 = listNode(x)
    n2 = listNode(y)

    while a.next is not head:
        a = a.next
    b = a
    n1.next = a
    n2.next = b.next
    return head

# Question 9
# # Maximum Number In DLL

def MaxDList(head):
    h = head
    max_ = 0
    while h is not None:
        if h.data > max_:
            max_ = h.data
        h = h.next
    return max_

# Question 11 
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

def sortSLL(head):
    h = head
    count = h.len()

    for i in range(count-1):
        h = head
        for j in range(0, count-i-1):
            if h.next is not None and h.data > h.next.data:
                h.data, h.next.data = h.next.data, h.data
            h = h.next


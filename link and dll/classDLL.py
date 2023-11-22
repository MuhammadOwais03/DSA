
class doubleNode:
    def __init__(self, value):
        self.prev = None
        self.data = value
        self.next = None

    def search(self, target):
        head = self
        while head.prev is not None:
            head = head.prev
        while head is not None and head.data != target:
            head = head.next
        return [head is not None, head]

    def insertAfter(self, target, data):
        # p q r
        head = self
        newNode = doubleNode(data)
        q = newNode
        status, targetNode = self.search(target)
        if status and targetNode.next != None:
            p = targetNode
            r = targetNode.next
            p.next = q
            q.prev = p
            r.prev = q
            q.next = r
        else:
            targetNode.next = q
            q.prev = targetNode
        return head
    
    def insertBefore(self, target, data):
        # p q r
        head = self
        status, targetNode = head.search(target=target)
        r = targetNode
        newNode = doubleNode(data)
        q = newNode
        if status and targetNode.prev is not None:
            p = r.prev
            p.next = q
            q.prev = p
            q.next = r
            r.prev = q
        else:
            q.next = r
            r.prev = q
        return head
    
    def inserHead(self, data):
        head = self
        newNode = doubleNode(data)
        p = newNode

        while head.prev is not None:
            head = head.prev
        q = head
        q.prev = p
        p.next = q
        return head
    
    def append(self, data):
        newNode = doubleNode(data)
        q = newNode
        head = self
        while head is not None:
            prev = head
            head = head.next
        prev.next = q
        q.prev = prev

    def delete(self, target):
        head = self
        status, targetNode = self.search(target)
        
        if status and targetNode.prev != None and targetNode.next != None:
            p = targetNode.prev
            r = targetNode.next
            p.next = r
            r.prev = p
            del p
        else:
            if targetNode.prev == None:
                return targetNode.next
            elif targetNode.next == None:
                prev = targetNode.prev
                prev.next = None
                del targetNode

        return head
    
    def len(self):
        count = 0
        head = self
        while head is not None:
            count += 1
            head = head.next
        return count

    
    def __repr__(self):
        head = self
        nodes = []
        while head.prev is not None:
            head = head.prev
        while head is not None:
            nodes.append(str(head.data))
            head = head.next
        nodes.append("None")
        return "<->".join(nodes)


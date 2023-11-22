class listNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def insert(self, value):
        newNode = listNode(value)
        newNode.next = self.next
        self.next = newNode

    def append(self, value):
        newNode = listNode(value)
        a = self
        while a is not None:
            b = a
            a = a.next
        if a is None:
            b.next = newNode
            

    def delete(self):
        item=None
        if self.next is not None:
            tmp=self.next
            item=tmp.data
            self.next=tmp.next
        return item
    
    def deleteHead(self):
        if self is not None:
            a = self.next
            self.next = None  # Disconnect the current head
            return a
        return None

    
    def len(self):
        i = 0
        while self is not None:
            self = self.next
            i += 1
        return i
    def __repr__(self):
        a = self
        nodes = []
        while a is not None:
            nodes.append(str(a.data))
            a = a.next
        nodes.append("None")
        return "->".join(nodes)
            

    def search(self, target):
        a=self
        if a.data==target:
            return [True, None, a]
        b=a.next
        while b is not None and b.data!=target:
            a=a.next
            b=b.next
        return [b is not None, a, b]

        
class queue:
    def __init__(self, elements):
        self.elements = [None]*elements
        self.track = -1
        self.length = elements
    
    def push(self, value):
        self.track += 1
        assert self.track <= self.length-1, "Queue Is Not Empty"
        self.elements[self.track] = value

    def pop(self):
        assert self.track > -1 and self.track <= self.length, "Queue Is Empty"
        
        value = self.elements[0]
        for i in range(0, self.length-1):
            self.elements[i] = self.elements[i+1]
        self.track -= 1
        self.elements[self.length-1] = None
        return value
    
    def delete(self, ins):
        ind = self.elements.index(ins)
        for i in range(ind, self.length-1):
            self.elements[i] = self.elements[i+1]
        self.elements[self.length-1] = None
        self.track -= 1
    
    def __str__(self):
        String = ""
        for i in range(self.length-1, -1, -1):
            String += f"{str(self.elements[i])} "
        return String
    
    def getter(self):
        return [i for i in self.elements if i != None], self.track
    
    

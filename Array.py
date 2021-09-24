class Array():
    def __init__(self, length):
        self.length = length
        self.values = list()
        for i in range(self.length):
            self.values.append(None)
        
    def __getitem__(self, index):
        return self.values[index]
        
    def __setitem__(self, index, value):
        self.values[index] = value
        
        
a = Array(10)
print(a.length)
print(a[2])
a[2] = 3
print(a[2])

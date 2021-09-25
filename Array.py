from typing import Any

class Array(object):
    """
    Defines an array with length. Indexing is donw through magic method
    __getitem__ to return value at indexed location in the array.  
    """

    def __init__(self, length: int):
        self.length: int = length
        self.values: list  = []
        for i in range(self.length):
            self.values.append(None)
        
    def __getitem__(self, index: int) -> Any:
        if index <= len(self.values):
            return self.values[index]
        else:
            raise IndexError
        
    def __setitem__(self, index, value):
        if index <= len(self.values):
            self.values[index] = value
        else:
            raise IndexError

if __name__ == "__main__":
    a = Array(10)
    print(a.length)
    print(a[2])
    a[2] = 3
    assert a[2] == 3

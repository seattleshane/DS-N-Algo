from typing import Any

class Array(object):
    """
    Defines an array with length. Indexing is done through magic method
    __getitem__ to return value at indexed location in the array.

    Parameters
    ----------
    legnth : int
        length of the array as determined at initialization.
    values : list[Any]
        Values of the array, any type.
    """

    def __init__(self, length: int):
        """
        Initialization of the class, creates length based on int.

        Initialization of length is done by property.setter.

        Parameters
        ----------
        legnth : int
            length of the array as determined at initialization.

        """
        self._length: int = length
        self.values: list  = []
        for i in range(self.length):
            self.values.append(None)

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        if isinstance(length, int):
            self._length = length
        else:
            raise TypeError(f"Length must be type int")

    def __getitem__(self, index: int) -> Any:
        """
        Returns value at given index.

        Parameters
        ----------
        index : int
            Index of value location.
        """
        if isinstance(index,int):
            if index <= len(self.values):
                return self.values[index]
            else:
                raise IndexError(f"Index {index} out of range, legnth of array is {self.length}.")
        else:
            raise TypeError(f"Index must by type int, got {type(index)}")

    def __setitem__(self, index, value):
        """
        Sets value at given index.

        Parameters
        ----------
        index : int
            Index of value location.
        value : any
            Value to set at index.
        """
        if isinstance(index,int):
            if index <= len(self.values):
                self.values[index] = value
            else:
                raise IndexError(
                    f"Index {index} out of range, legnth of array is {self.length}.") #Technically this is out of PEP8 Standard because it's too long, but it's a special case because it's a string
        else:
            raise TypeError(f"Index must by type int, got {type(index)}")

if __name__ == "__main__":
    a = Array(10)
    print(a.length)
    print(a[2])
    a[2] = 3
    assert a[2] == 3
    assert a[40] == 0

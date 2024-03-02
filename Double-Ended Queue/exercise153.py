class Deque:
    """The simplest version of deque."""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add_first(self, item):
        self._data.insert(0, item)

    def add_last(self, item):
        self._data.append(item)

    def delete_first(self):
        if self.is_empty():
            raise IndexError('The deque is empty.')
        return self._data.pop(0)

    def delete_last(self):
        if self.is_empty():
            raise IndexError('The deque is empty.')
        return self._data.pop()

    def is_empty(self):
        return len(self._data) == 0

    def first(self):
        if self.is_empty():
            raise IndexError('The deque is empty.')
        return self._data[0]

    def last(self):
        if self.is_empty():
            raise IndexError('The deque is empty.')
        return self._data[-1]
        
cities = Deque()

cities.add_first('London')

cities.add_last('Madrid')

cities.first()

cities.add_last('Vienna')

cities.add_first('Rome')

cities.delete_last()

cities.last()

cities.delete_first()

print(cities.delete_last())
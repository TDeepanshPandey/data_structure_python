class Deque():
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def add_first(self, element):
        return self._data.insert(0, element)
    
    def add_last(self, element):
        return self._data.append(element)
    
    def delete_first(self):
        if self.__len__() == 0:
            raise(IndexError,'The deque is empty')
        return self._data.pop(0)
        
    def delete_last(self):
        if self.__len__() == 0:
            raise(IndexError,'The deque is empty')
        return self._data.pop()

class EmptyStackError(Exception):
    pass


class Stack:
    """The simplest stack."""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError('The stack is empty.')
        return self._data.pop()

    def is_empty(self):
        return len(self._data) == 0

    def top(self):
        if self.is_empty():
            raise EmptyStackError('The stack is empty.')
        return self._data[-1]
    
    """     
    def clear(self):
        while not self.is_empty():
            self.pop() """

    def clear(self):
        self._data.clear()

techs = Stack()
techs.push('python')
techs.push('django')
print(len(techs))
 
techs.clear()
print(len(techs))

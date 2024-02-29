class EmptyStackError(Exception):
    pass

class Stack():
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)
    
    def push(self, item):
        self._data.append(item)
    
    def pop(self):
        if self.__len__() > 0:
            return self._data.pop()
        else:
            raise EmptyStackError('The stack is empty.')

techs = Stack()
techs.push('python')
techs.push('sql')
len(techs)

techs.pop()
len(techs)

techs.pop()
techs.pop()
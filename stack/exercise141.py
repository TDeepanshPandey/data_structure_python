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

def is_palindrome(a):
    techs = Stack()
    chk_paladrome = True

    for i in a:        
        techs.push(i)
    
    for i in a:
        if i != techs.pop():
            chk_paladrome = False
    
    return chk_paladrome


class Stack:
    """The simplest stack."""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if len(self._data) == 0:
            raise IndexError('Pop from empty stack.')
        return self._data.pop()

    def is_empty(self):
        return len(self._data) == 0
    

websites = Stack()

websites.push('bloomberg.com')
websites.push('bloomberg.com/europe')
websites.push('bloomberg.com/markets/stocks')
websites.pop()
websites.push('bloomberg.com/markets/currencies')


while(not websites.is_empty()):
    print(websites.pop())
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

def is_palindrome(string):
    deq = Deque()
    is_palindrome_flag = True
 
    for char in string:
        deq.add_last(char)
 
    while len(deq) > 1 and is_palindrome_flag:
        first = deq.delete_first()
        last = deq.delete_last()
        if first != last:
            is_palindrome_flag = False
 
    return is_palindrome_flag
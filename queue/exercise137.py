class Queue():
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)
    
    def enqueue(self,item):
        self._data.append(item)
    
    def dequeue(self):
        try:
            return self._data.pop(0)
            
        except IndexError:
            return IndexError('The queue is empty')

    def is_empty(self):
        return self.__len__() < 0

    def first(self):
        try: 
            return self._data[0]
        except IndexError:
            return IndexError('The queue is empty')

que = Queue()
que.enqueue('529')
que.enqueue('512')
len(que)

que.enqueue('844')
que.first()

len(que)

que.is_empty()

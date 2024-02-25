class Node:
    """Simple Node class."""

    def __init__(self, data, next_node=None):
        self._data = data
        self._next_node = next_node

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next_node

    def set_next(self, new):
        self._next_node = new


nodes = (Node('Warsaw'), Node('Berlin'), Node('London'))
node1, node2, node3 = nodes

node1.set_next(node2)
node2.set_next(node3)

for i in nodes:
    if i.get_next():
        print(i.get_data(), '->', i.get_next().get_data())
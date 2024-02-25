class Node:
    """Simple Node class."""

    def __init__(self, data, prev_node=None, next_node=None):
        self._data = data
        self._prev_node = prev_node
        self._next_node = next_node

    def get_data(self):
        return self._data

nodes = (Node("Warsaw"), Node("Berlin"), Node("London"))

print(nodes[1].get_data())
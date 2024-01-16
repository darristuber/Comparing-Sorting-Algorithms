# This is the Node class that your linked list will use
# You may not change anything in this file
# L. Jacques Feb '23

class Node:
    def __init__(self, d=None, l=None):
        self._data = d
        self._link = l
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, d):
        self._data = d
    @property
    def link(self):
        return self._link
    @link.setter
    def link(self, l):
        self._link = l
    '''def __lt__(self, other):
        return (self._data > other._data)'''



from Chapter05_BST.bst import BST
from Chapter06_Set_Map.base import SetBase

class Set(SetBase):
    """二分搜索树实现集合"""
    def __init__(self):
        self._bst = BST()

    def add(self,e):
        self._bst.add(e)

    def remove(self, e):
        self._bst.remove(e)

    def contains(self, e):
        return self._bst.contains(e)

    def get_Size(self):
        return self._bst.get_Size()

    def is_Empty(self):
        if self._bst.is_Empty():
            return True
        return False

if __name__ == "__main__":
    with open('shakes.txt') as f:
        words = f.read()
    words = words.split()

    import time
    start_time = time.time()
    bst_set = BST()
    for word in words:
        bst_set.add(word)
    print('Total words: ', len(words))
    print('Unique words: ', bst_set.get_Size())
    print('Contains word "to": %s ' % bst_set.contains('to'))
    print('Total Time： %s' % str(time.time() - start_time))
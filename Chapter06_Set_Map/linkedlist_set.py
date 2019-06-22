from Chapter04_LinkedList.linkedlist import LinkList
from Chapter06_Set_Map.base import SetBase

class LinkedListSet(SetBase):
    """链表实现集合"""
    def __init__(self):
        self._list = LinkList()

    def get_Size(self):
        return self._list.get_Size()

    def is_Empty(self):
        return self._list.is_Empty()

    def contains(self, e):
        return self._list.contains(e)

    def add(self,e):
        if not self._list.contains(e):
            self._list.add_First(e)

    def remove(self, e):
        self._list.remove_Element(e)

if __name__ == "__main__":
    with open('shakes.txt') as f:
        words = f.read()
    words = words.split()

    import time
    start_time = time.time()
    linked_list_set = LinkedListSet()
    for word in words:
        linked_list_set.add(word)
    print('Total words: ', len(words))
    print('Unique words: ', linked_list_set.get_Size())
    print('Contains word "to": %s ' % linked_list_set.contains('to'))
    print('Total Time： %s' % str(time.time() - start_time))
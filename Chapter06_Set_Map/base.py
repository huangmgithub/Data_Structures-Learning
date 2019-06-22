class SetBase:
    def add(self,e):
        raise NotImplementedError

    def remove(self, e):
        raise NotImplementedError

    def contains(self, e):
        raise NotImplementedError

    def get_Size(self):
        raise NotImplementedError

    def is_Empty(self):
        raise NotImplementedError

class MapBase:
    def add(self, key, value):
        raise NotImplementedError

    def remove(self, key):
        raise NotImplementedError

    def contains(self, key):
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError

    def get_Size(self):
        raise NotImplementedError

        raise NotImplementedError

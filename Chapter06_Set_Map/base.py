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

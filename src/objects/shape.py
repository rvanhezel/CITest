

class square:

    def __init__(self, _length):
        self.len = _length

    def area(self):
        return self.len**2

    def who_am_i(self):
        print("I'm a square.")


class cube:

    def __init__(self, _length):
        self.len = _length

    def area(self):
        return self.len**3

    def who_am_i(self):
        print("I'm a cube.")
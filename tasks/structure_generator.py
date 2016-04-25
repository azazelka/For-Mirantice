import random
import string


class structure_generator(object):
    def __init__(self, size, depth):
        self._size = size
        self._depth = depth
        self.structure = self._get_structure()

    def _num_creator(self):
        return random.randint(0, 100)

    def _str_creator(self):
        a = string.ascii_letters + string.digits
        return ''.join([random.choice(a) for i in range(5)])

    def _list_creator(self, size, depth):
        res = []
        for i in range(size):
            if depth:
                res.append(self._rec_generator(size, depth))
        return res or 1

    def _dict_creator(self, size, depth):
        res = {}
        for i in range(size):
            if depth:
                res[self._str_creator()] = self._rec_generator(size, depth)
        return res or 1

    def _rec_generator(self, size, depth):
        case = random.randint(0, 3)
        depth -= 1
        size -= size * depth / self._depth
        if case == 0:
            return self._list_creator(size, depth)
        if case == 1:
            return self._dict_creator(size, depth)
        if case == 2:
            return self._str_creator()
        if case == 3:
            return self._num_creator()

    def _get_structure(self):
        case = random.randint(0, 1)
        res = []
        if case:
            res = {}
            for i in range(self._size):
                res[self._str_creator()] = self._rec_generator(self._size, self._depth)
        else:
            for i in range(self._size):
                res.append(self._rec_generator(self._size, self._depth))
        return res
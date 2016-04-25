import random
import string


class structure_generator(object):
    def __init__(self, size, depth, seed):
        self._size = size
        self._depth = depth
        self._seed = seed
        self._structure = self._get_structure()

    @property
    def structure(self):
        return self._structure

    def _num_creator(self):
        return random.randint(0, 100)

    def _str_creator(self):
        a = string.ascii_letters + string.digits #+ ":" + "'"
        c = random.randint(5, 10)
        random.seed(self._seed)
        return ''.join([random.choice(a) for i in range(c)])

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
        sd = size + depth
        case = random.randint(0, sd + 2)
        depth -= 1
        size -= size * depth / self._depth
        if case <= (sd)/2:
            return self._list_creator(size, depth)
        if case <= sd:
            return self._dict_creator(size, depth)
        if case == sd + 1:
            return self._str_creator()
        if case == sd + 2:
            return self._num_creator()

    def _get_structure(self):
        random.seed(self._seed)
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

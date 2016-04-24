import random
import string


def num_creator():
    return random.randint(0, 100)


def str_creator():
    a = string.ascii_letters + string.digits
    return ''.join([random.choice(a) for i in range(5)])


def list_creator(depth):
    result = []
    if depth:
        result.append(rec_generator(depth))
        depth -= 1
    return result or 1


def dict_creator(depth):
    result = {}
    if depth:
        result[str_creator()] = rec_generator(depth)
        depth -= 1
    return result or 1


def rec_generator(depth):
    case = random.randint(0, 3)
    if case == 0:
        return list_creator(depth)
    if case == 1:
        return dict_creator(depth)
    if case == 2:
        return str_creator()
    if case == 3:
        return num_creator()


def structure_generator(size, depth):
    case = random.randint(0, 1)
    result = []
    if case:
        result = {}
        for i in range(size):
            result[str_creator()] = rec_generator(depth)
    else:
        for i in range(size):
            result.append(rec_generator(depth))
    return result

# print structure_generator(5)

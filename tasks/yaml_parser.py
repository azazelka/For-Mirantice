import yaml
from itertools import groupby


def st_parser(filename):
    with open(filename, 'r') as fd:
        print yaml.load(fd)


def load_file(filename):
    with open(filename, 'r') as fd:
        for item in fd:
            yield item


def count_space(lst):
    for i, c in enumerate(lst[0]):
        if c != ' ':
            return i
    return len(lst[0])


def processing_list(lst):
    yml_list = lst
    lst = []
    flag_list = False
    count = count_space(yml_list)
    start_str = "- "
    start_empty_str = "-"
    for i in range(count):
        start_str = " " + start_str
        start_empty_str = " " + start_empty_str
    for item in yml_list:
        if item.startswith(start_str):
            lst.append(item[count + 2: -1])
        elif item.startswith(start_empty_str):
            flag_list = True
            lst.append([])
        elif flag_list:
            lst[len(lst) - 1].append(item)
        else:
            raise IOError
    count += 1
    res = []
    for item in lst:
        res.append(rec_parser(item))
    return res


def rec_parser(lst):
    if isinstance(lst, list):
        return processing_list(lst)
    else:
        if lst.find(": ") >= 0:
            spl = lst.split(": ")
            return {spl[0]: spl[1]}
        if lst.startswith('\'') and lst.endswith('\''):
            return lst[1:-1]
        elif lst.isdigit():
            return int(lst)
        else:
            raise IOError


def yml_parser(file_name):
    str_list = list(load_file(file_name))
    print str_list
    return rec_parser(str_list)


print yml_parser('file2.yml')
st_parser('file2.yml')

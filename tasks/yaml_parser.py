import yaml


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
    yml_list = []
    count = count_space(lst)
    start_str = count * " " + "-"
    for item in lst:
        if item.startswith(start_str):
            yml_list.append(item[count + 2: -1]) if item[count + 2: -1] else yml_list.append([])
        else:
            yml_list[len(yml_list) - 1].append(item)
    count += 1
    res = []
    for item in yml_list:
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

import yaml


def st_parser(filename):
    with open(filename, 'r') as fd:
        return yaml.load(fd)


def load_file(filename):
    with open(filename, 'r') as fd:
        for item in fd:
            yield item


def count_space(s):
    for i, c in enumerate(s):
        if c != ' ':
            return i
    return len(s)


def is_dict_line(line, count):
    if len(line) <= count:
        return False

    spaces = count * " "
    if not line.startswith(spaces):
        return False

    if line[count] == " " or line[count] == "-":
        return False

    if line.find(":") < 0:
        return False

    return True


def add_item(str):
    str = str.strip()
    if str.startswith('\'') and str.endswith('\''):
        return str[1:]
    elif str.isdigit():
        return int(str)
    else:
        raise IOError


def processing_dict(lst):
    res = {}
    data_iter = iter(lst)

    line = next(data_iter)
    count = count_space(line)

    while line:
        if not is_dict_line(line, count):
            return {}

        items = line.split(":")
        key = items[0][count:]
        cur_value = items[1][1:]

        value = []
        if cur_value:
            value = cur_value

        line = next(data_iter, None)
        while line and not is_dict_line(line, count):
            value.append(line)
            line = next(data_iter, None)
        res[key] = rec_parser(value)

    return res


def processing_list(lst):
    yml_list = []
    count = count_space(lst[0])
    start_str = count * " " + "-"
    if not str(lst[0]).startswith(start_str):
        return []
    for item in lst:
        without_dash = (count + 1) * " " + item[count + 1:]
        if item.startswith(start_str) and item.find(":") >= 0:
            yml_list.append([])
            yml_list[-1].append(without_dash)
        elif item.startswith(start_str + " -"):
            yml_list.append([])
            yml_list[-1].append(without_dash)
        elif item.startswith(start_str):
            yml_list.append(item[count + 2:] or [])
        elif len(yml_list):
            yml_list[-1].append(item)
    res = []
    for item in yml_list:
        res.append(rec_parser(item))
    if not res:
        add_item(lst)
    return res


def rec_parser(lst):
    return processing_list(lst) or processing_dict(lst) or add_item(lst)


def yml_parser(file_name):
    str_list = list(load_file(file_name))
    return rec_parser(str_list)


print yml_parser('file1.yml')
print st_parser('file1.yml')

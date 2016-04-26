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

    if line[count] == " " or line[count:count + 2] == "- ":
        return False

    if line.find(":") < 0:
        return False

    if line.find(": ") < 0 and line[-2] != ":":
        return False

    return True


def is_list_line(line, count):
    start_str = count * " " + "-"

    if len(line) <= count:
        return False

    if not line.startswith(start_str):
        return False

    if line.startswith(start_str + " ") or line.startswith(start_str + "\n"):
        return True

    return False


def add_item(line):
    line = line[0]
    line = line.strip()
    if line.isdigit():
        if line.startswith('0') and len(line) > 1:
            return line
        return int(line)
    if line.startswith('\'') and line.endswith('\''):
        return line[1:-1]
    else:
        return line


def processing_dict(lst):
    res = {}
    data_iter = iter(lst)

    line = next(data_iter)
    count = count_space(line)

    while line:
        if not is_dict_line(line, count):
            return {}

        items = line.split(": ")

        if len(items) == 1:
            key = line[count:-2]
            cur_value = []
        else:
            key = items[0][count:]
            cur_value = items[1][0:]

        value = []
        if cur_value:
            value = [cur_value]

        if key.startswith('\'') and key.endswith('\''):
            key = key[1: -1]

        line = next(data_iter, None)
        while line and not is_dict_line(line, count):
            value.append(line)
            line = next(data_iter, None)
        res[key] = rec_parser(value)

    return res


def processing_list(lst):
    res = []
    data_iter = iter(lst)
    line = next(data_iter)
    count = count_space(line)

    while line:
        if not is_list_line(line, count):
            return []

        cur_value = line[count + 2:]

        if not cur_value:
            value = []
        else:
            value = [(count + 1) * " " + line[count + 1:]]
        line = next(data_iter, None)

        while line and not is_list_line(line, count):
            value.append(line)
            line = next(data_iter, None)
        res.append(rec_parser(value))
    return res


def rec_parser(lst):
    return processing_list(lst) or processing_dict(lst) or add_item(lst)


def yml_parser(file_name):
    str_list = list(load_file(file_name))
    return rec_parser(str_list)


# print yml_parser("res.yml")
# print st_parser("res.yml")

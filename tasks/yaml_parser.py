import yaml


def st_parser(filename):
    with open(filename, 'r') as fd:
        print yaml.load(fd)


def load_file(filename):
    yml_list = []
    with open(filename, 'r') as fd:
        for item in fd:
            yield item


def rec_parser(lst, count=0):
    count_spase = 3
    if type(lst) == list:
        yml_list = lst
        lst = []
        flag_list = False
        pattern1 = " - "
        pattern2 = " -"
        for i in range(count):
            pattern1 = "   " + pattern1
            pattern2 = "   " + pattern2

        for item in yml_list:
            slice = item[3 + count * count_spase: -1]
            if item.startswith(pattern1):
                lst.append(slice)

            elif item.startswith(pattern2):
                flag_list = True
                lst.append([])
            elif flag_list:
                lst[len(lst) - 1].append(item)
            else:
                raise IOError
        count += 1
        res = []
        for item in lst:
            res.append(rec_parser(item, count))
        return res
    else:
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

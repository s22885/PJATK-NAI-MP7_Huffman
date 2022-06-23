import os


def get_data(data: str, separator: str = " "):
    lines = data[1].splitlines(keepends=False)
    if len(lines) == 0:
        return
    size = int(lines[0])
    res = []
    for i in lines[1:size + 1]:
        tmp = i.split(sep=separator)
        res.append([tmp[0], int(tmp[1])])
    if len(res) != size:
        return
    res.sort(key=sort_fun)
    return res


def data_load(path: str):
    if os.path.isfile(path):
        return [True, open(path, encoding="utf-8").read()]
    return [False]


def sort_fun(e):
    return e[1]

def flatten(_list):
    flattened_list = []

    def loop(_list):
        for i in _list:
            if isinstance(i, list):
                loop(i)
            else:
                flattened_list.append(i)

    loop(_list)
    return flattened_list


list_ = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]

print(flatten(list_))

def reverse_list(_list):
    _list.reverse()
    for i in _list:
        if isinstance(i, list):
            i.reverse()
    return _list


listed = [[1, 2], [3, 4], [5, 6, 7]]
print(reverse_list(listed))
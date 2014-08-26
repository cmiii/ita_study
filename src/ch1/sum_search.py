
def _bin_search(in_data, p, q, value):
    if q <= p:
        return -1
    if q == p + 1:
        if in_data[p] == value:
            return p
        else:
            return -1
    m = int((p + q) / 2)
    if in_data[m] == value:
        return m
    elif in_data[m] > value:
        return _bin_search(in_data, p, m, value)
    else:
        return _bin_search(in_data, m+1, q, value)


def sum_search(in_data, sum_value):
    found = False
    tmp = in_data.copy()
    tmp.sort()
    length = len(tmp)
    for i in range(0, length - 1):
        target = sum_value - tmp[i]
        ret = _bin_search(tmp, i+1, length, target)
        if ret != -1:
            found = True
            print("found (", i, ")", tmp[i], " + (", ret, ")", tmp[ret], " = ", sum_value)
            break
    return found


def _merge(data, p, q, r):
    tmp1 = data[p:q+1]
    tmp2 = data[q+1:r+1]
    #l = r - p + 1
    count = 0
    i = p
    while len(tmp1) > 0 and len(tmp2) > 0:
        if tmp1[0] <= tmp2[0]:
            data[i] = tmp1.pop(0)
        else:
            data[i] = tmp2.pop(0)
            count += len(tmp1)
        i += 1

    if len(tmp1) > 0:
        data[i:r+1] = tmp1
    if len(tmp2) > 0:
        data[i:r+1] = tmp2

    return count

def _merge_sort(data, s, t):
    assert(s <= t)
    if s == t:
        return 0

    m = int((t - s + 1) / 2)
    p = s
    q = s + m - 1
    r = t
    count0 = _merge_sort(data, p, q)
    count1 = _merge_sort(data, q+1, r)
    count2 = _merge(data, p, q, r)
    print(data, p, q, r, count0, count1, count2)
    return (count0 + count1 + count2)


def inversion_count(in_data):
    out_data = in_data.copy()

    length = len(out_data)
    ret = _merge_sort(out_data, 0, length - 1)

    return ret


def bubble_sort(in_data):
    out_data = in_data.copy()

    length = len(out_data)
    for i in range(0, length-1):
        for j in range(0, length-1-i):
            if out_data[j] > out_data[j+1]:
                tmp = out_data[j+1]
                out_data[j+1] = out_data[j]
                out_data[j] = tmp

    return out_data

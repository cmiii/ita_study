

def selection_sort(in_data):
    out_data = in_data.copy()

    length = len(out_data)
    for i in range(0, length-1):
        temp = out_data[i]
        smallest = i
        flag = False
        for j in range(i+1, length):
            if out_data[j] < temp:
                temp = out_data[j]
                smallest = j
                flag = True
        if flag:
            out_data[smallest] = out_data[i]
            out_data[i] = temp

    return out_data

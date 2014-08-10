

def insert_sort(in_data):
    out_data = in_data.copy()

    length = len(out_data)
    for i in range(1, length):
        temp = out_data[i]
        smallest = True
        for j in range(i-1, -1, -1):
            if temp < out_data[j]:
                out_data[j+1] = out_data[j]

            else:
                out_data[j+1] = temp
                smallest = False
                break
        if smallest:
            out_data[0] = temp


    return out_data

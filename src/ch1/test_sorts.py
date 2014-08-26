import fileinput


def test_insert_sort():
    # get data from file
    print("test insert sort.")
    in_data = []
    for line in fileinput.input("../../data/sort1.dat"):
        in_data.append(int(line))
    print("in_data", in_data)

    target_data = in_data.copy()

    target_data.sort()
    print("target_data", target_data)

    from insert_sort import insert_sort

    out_data = insert_sort(in_data)
    print("out_data", out_data)

    assert (out_data == target_data)


def test_selection_sort():
    # get data from file
    print("test selection sort.")
    in_data = []
    for line in fileinput.input("../../data/sort1.dat"):
        in_data.append(int(line))
    print("in_data", in_data)

    target_data = in_data.copy()

    target_data.sort()
    print("target_data", target_data)

    from selection_sort import selection_sort

    out_data = selection_sort(in_data)
    print("out_data", out_data)

    assert (out_data == target_data)


def test_merge_sort():
    # get data from file
    print("test merge sort.")
    in_data = []
    for line in fileinput.input("../../data/sort1.dat"):
        in_data.append(int(line))
    print("in_data", in_data)

    target_data = in_data.copy()

    target_data.sort()
    print("target_data", target_data)

    from merge_sort import merge_sort

    out_data = merge_sort(in_data)
    print("out_data", out_data)

    assert (out_data == target_data)


def test_bubble_sort():
    # get data from file
    print("test bubble sort.")
    in_data = []
    for line in fileinput.input("../../data/sort1.dat"):
        in_data.append(int(line))
    print("in_data", in_data)

    target_data = in_data.copy()

    target_data.sort()
    print("target_data", target_data)

    from bubble_sort import bubble_sort

    out_data = bubble_sort(in_data)
    print("out_data", out_data)

    assert (out_data == target_data)
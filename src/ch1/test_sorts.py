import fileinput


def test_insert_sort():
    # get data from file
    in_data = []
    for line in fileinput.input("../../data/sort1.dat"):
        in_data.append(int(line))
    print("in_data", in_data, "\n")

    target_data = in_data.copy()

    target_data.sort()
    print("target_data", target_data, "\n")

    from insert_sort import insert_sort

    out_data = insert_sort(in_data)
    print("out_data", out_data, "\n")

    assert (out_data == target_data)


def test_selection_sort():
    # get data from file
    in_data = []
    for line in fileinput.input("../../data/sort1.dat"):
        in_data.append(int(line))
    print("in_data", in_data, "\n")

    target_data = in_data.copy()

    target_data.sort()
    print("target_data", target_data, "\n")

    from selection_sort import selection_sort

    out_data = selection_sort(in_data)
    print("out_data", out_data, "\n")

    assert (out_data == target_data)
import fileinput


def test_sum_search():
    # get data from file
    print("test sum search.")
    in_data = []
    for line in fileinput.input("../../data/sort1.dat"):
        in_data.append(int(line))
    sum_value = 128
    print("in_data", in_data)
    print("sum_value=", sum_value)

    from sum_search import sum_search

    ret = sum_search(in_data, sum_value)
    print("ret = ", ret)

    assert ret

def test_inversion_count():
    # get data from file
    print("test inversion count.")
    in_data = []
    for line in fileinput.input("../../data/sort1.dat"):
        in_data.append(int(line))
    print("in_data", in_data)

    from inversion_count import inversion_count

    ret = inversion_count(in_data)
    print("ret = ", ret)

    assert (ret == 16)

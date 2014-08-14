__author__ = 'dinggp'


def change(in_data):
    tmp = in_data[0]
    in_data[0] = in_data[1]
    in_data[1] = tmp


a = [1, 2]
change(a)
print(a)



def _changeint(val):
    val = 1


def _change(in_data):
    tmp = in_data[0]
    in_data[0] = in_data[1]
    in_data[1] = tmp


a = [1, 2]
_change(a)
print(a)

b = 2
_changeint(b)
print(b)
import math


def main(o):
    h = {curr_o ** 3 + math.ceil(curr_o / 2) for curr_o in o if -53 < curr_o <= 68}
    p = h | o
    n = h | p
    return sum(p) + sum(curr_p - curr_v for curr_p in p for curr_v in n)


print(main({-62, 99, -87, -21, 81, -14, -2, -9, -69, -66}))
print(main({5, 70, -24, 13, -47, -15, -13, -39, 30, -65}))

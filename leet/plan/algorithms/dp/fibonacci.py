"""
0 1 1 2 3 5 ...
"""


def fib(n):
    if n in [0, 1]:
        return n
    prev_num = 1
    prev_prev_num = 0
    for i in range(1, n):
        curr_num = prev_num + prev_prev_num

        prev_prev_num = prev_num
        prev_num = curr_num
    return curr_num

print(fib(4))
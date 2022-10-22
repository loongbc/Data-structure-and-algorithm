# _*_coding:utf-8_*_
# created by Amuu on 2021/10/20

t = [100, 50, 20, 5, 1]


def change(t, n):
    m = [0 for _ in range(len(t))]
    for i, money in enumerate(t):
        m[i] = n // money
        n = n % money
    return m, n


print(change(t, 376))

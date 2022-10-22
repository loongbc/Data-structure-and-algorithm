# _*_coding:utf-8_*_
# created by Amuu on 2022/8/31


def Linear_Search(li, val):
    for ind, v in enumerate(li):
        print(ind, v)
        if v == val:
            return ind
    else:
        return None


li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(Linear_Search(li, 3))

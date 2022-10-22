# _*_coding:utf-8_*_
# created by Amuu on 2021/9/27

# 顺序查找
def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
        else:
            return None

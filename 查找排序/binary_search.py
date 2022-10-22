# _*_coding:utf-8_*_
# created by Amuu on 2021/9/27

# 二分查找
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None

# print(binary_search([1, 2, 3, 4, 5, 6, 7], 3))

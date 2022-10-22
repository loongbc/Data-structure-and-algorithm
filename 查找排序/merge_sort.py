# _*_coding:utf-8_*_
# created by Amuu on 2021/9/27

# 归并排序
def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:  # 只要左右都有数 就比较
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    # while 执行完，肯定有一部分没数了
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high + 1] = ltmp


# li = [2, 4, 5, 7, 1, 3, 6, 8, 9, 10, 11, 12, 13]
# merge(li, 0, 3, 12)
# print((li))


def merge_sort(li, low, high):
    if low < high:  # 至少有两个元素，递归
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)

# li = list(range(1000))
# import random
# random.shuffle(li)
# print(li)
# merge_sort(li,0,len(li)-1)
# print(li)

# def merge_sort_test(li, low, high):
#     if low < high:  # 至少有两个元素，递归
#         mid = (low + high) // 2
#         merge_sort_test(li, low, mid)
#         merge_sort_test(li, mid + 1, high)
#         merge(li,low,mid,high)
# li = list(range(10))
# import random
# random.shuffle(li)
# print(li)
# merge_sort_test(li,0,len(li)-1)
# print(li)

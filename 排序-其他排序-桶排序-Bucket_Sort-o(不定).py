# _*_coding:utf-8_*_
# created by Amuu on 2022/9/1


def bucket_sort(li, n=100, max_num=10000):
    buckets = [[] for _ in range(n)]  # 创建 n 个桶
    for var in li:
        i = min(var // (max_num // n), n - 1)  # i表示var放到几号桶里
        buckets[i].append(var)  # 把var 加到桶内
        # 保持桶内的顺序
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)
    return sorted_li

import random

li = [random.randint(0, 1000000000) for i in range(10)]
print(bucket_sort(li))

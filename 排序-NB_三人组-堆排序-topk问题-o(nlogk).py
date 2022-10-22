# _*_coding:utf-8_*_
# created by Amuu on 2022/9/1

# 比较排序,榜单问题
def sift(li, low, high):  # 列表 堆的根节点位置 堆的最后一个元素的位置
    i = low  # i最开始指向根节点
    j = 2 * i + 1  # j 开始是左孩子
    tmp = li[low]  # 把堆顶存起来
    while j <= high:  # 只要j位置有数
        if j + 1 <= high and li[j + 1] < li[j]:  # 如果右孩子有并且比较大
            j = j + 1  # j 指向右孩子
        if li[j] < tmp:
            li[i] = li[j]
            i = j  # 往下看一层
            j = 2 * i + 1  # 新的左孩子
        else:  # tmp 更大 ，把 tmp 放到 i 的位置
            li[i] = tmp
            break
    else:
        li[i] = tmp  # 把 tmp 放到叶子节点上

def topk(li,k):
    heap = li[0:k]
    for i in range((k-2)//2,-1,-1):
        sift(heap,i,k-1)
    # 1.建堆
    for i in range(k,len(li)):
        if li[i]>heap[0]:
            heap[0]=li[i]
            sift(heap,0,k-1)
    # 2.遍历
    for i in range(k-1,-1,-1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    # 3.出数
    return heap

import random

li = list(range(100))
random.shuffle(li)
print(li)
print(topk(li,5))

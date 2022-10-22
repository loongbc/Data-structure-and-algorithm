# _*_coding:utf-8_*_
# created by Amuu on 2022/9/1


def insert_sort(li):
    for i in range(1, len(li)):  # 表示摸到牌的下标
        tmp = li[i]
        j = i - 1  # 手里牌的下标
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp
        print(li)

li = [3,2,4,1,5,7,9,6,8]
print(li)
insert_sort(li)


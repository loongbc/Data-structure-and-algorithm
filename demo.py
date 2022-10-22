# _*_coding:utf-8_*_
# created by Amuu on 2022/9/9

#
# a = int(input())
# b = []
# c = []
# for i in range(a):
#     d = list(map(int, input().split()))
#     if d[1] == 0:
#         b.append(d)
#     elif d[1] == 1:
#         c.append(d)
#     else:
#         raise ValueError("输入错误")
#
#
# def sert_maopao(A):
#     for i in range(len(A) - 1):
#         exchange = False  # 标志位
#         for j in range(len(A) - i - 1):
#             if A[j][0] < A[j + 1][0]:
#                 A[j], A[j + 1] = A[j + 1], A[j]
#                 exchange = True
#         if not exchange:
#             return
#
#
# def tot(B, C):
#     sert_maopao(C)
#     print(B, C)
#     tot1 = 0
#     for i in B:
#         tot1 += i[0]
#     for j in C:
#         if tot1 >= j[0]:
#             tot1 = 2 * tot1
#         else:
#             tot1 += j[0]
#     return tot1
#
#
# num = tot(b, c)
# print(num)

# st = "00:00:00", et = "00:00:52"
import re

st_et = input()
oo = []
aa = st_et
for i in range(6):
    pattern = re.compile(r'([0-5][0-9])')
    oo.append(st_et[pattern.search(st_et).span()[0]:pattern.search(st_et).span()[1]])
    st_et = st_et[pattern.search(st_et).span()[1] + 1:]
shi = int(oo[3]) - int(oo[0])
fen = int(oo[4]) - int(oo[1])
miao = int(oo[5]) - int(oo[3])
cha = miao + fen * 60 + shi * 60 * 60
print(cha)

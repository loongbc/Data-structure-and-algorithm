# _*_coding:utf-8_*_
# created by Amuu on 2022/9/8

"""

c[i,j] 表示Xi和Yj的LCS长度

c[i,j] ={0,若i=0或j=0；c[i-1,j-1]+1,若i,j＞0且xi=yj；max(c[i,j-1],c[i-1,j]),若i,j＞0且xi!=yj.}

"""


def Lcs_Length(x, y):  # 求最优解
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i][j - 1], c[i - 1][j])
    for _ in c:
        print(_)
    return c[m][n]


def Lcs(x, y):  # 过程记录
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    b = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 1
            elif c[i][j - 1] <= c[i - 1][j]:
                c[i][j] = c[i - 1][j]
                b[i][j] = 2
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = 3

    return c[m][n], b


def Lcs_Trackback(x, y):  # 回溯法
    c, b = Lcs(x, y)
    i = len(x)
    j = len(y)
    res = []
    while i > 0 and j > 0:
        if b[i][j] == 1:
            res.append(x[i - 1])
            i -= 1
            j -= 1
        elif b[i][j] == 2:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(res))


# print(Lcs_Length("ABCBDAB", "BDCABA"))
print(Lcs_Trackback("ABCBDAB", "BDCABA"))

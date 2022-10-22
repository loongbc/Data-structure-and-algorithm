# _*_coding:utf-8_*_
# created by Amuu on 2022/9/4

class Solution:
    def BYF(self):
        q = []
        for i in range(2):
            q.append(list(map(int, input().strip().split())))
        n = q[0][0]
        m = q[0][1]
        k = q[0][2]
        li = q[1]
        for i in range(m):
            li2 = reversed(li)
            li.extend(li2)
        return li[k - 1]


if __name__ == '__main__':
    solution = Solution()
    result = solution.BYF()
    print(result)

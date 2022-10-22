# _*_coding:utf-8_*_
# created by Amuu on 2022/9/4


class Solution:
    def BYF(self):
        q = []
        for i in range(2):
            q.append(list(map(int, input().split())))
        n = q[0][0]
        li = q[1]
        li.sort()
        tot = 0
        fushu = 0
        fushu2 = 0
        qi = 0
        for i in li:
            if i < 0:
                if abs(7 - abs(i)) > abs(1 - abs(i)):
                    tot += abs(1 - abs(i))
                else:
                    if qi == 0:
                        tot += abs(7 - abs(i))
                        qi += 0
                    else:
                        tot += abs(1 - abs(i))
                fushu += 1
            elif i == 0:
                tot += 1
                fushu2 += 0
            else:
                if abs(7 - i) > abs(1 - i):
                    tot += abs(1 - i)
                else:
                    if qi == 0:
                        tot += abs(7 - i)
                        qi += 0
                    else:
                        tot += abs(1 - i)
        if fushu % 2 == 0:
            return tot
        else:
            if fushu2 != 0:
                return tot
            else:
                return tot + 2


if __name__ == '__main__':
    solution = Solution()
    result = solution.BYF()
    print(result)

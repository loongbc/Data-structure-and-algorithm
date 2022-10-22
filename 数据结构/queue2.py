# _*_coding:utf-8_*_
# created by Amuu on 2021/10/10

# 内置队列模块
from collections import deque

# q = deque([1, 2, 3, 4, 5], 5)  # 队满 自动出队
# q.append(6)  # 队尾进队
# q.popleft()  # 队首出队
#
# # 用于双向队列
# q.appendleft(1)  # 队首进队
# q.pop()  # 队尾出队

def tail(n):
    with open("test.txt",'r') as f :
        q = deque(f, n)
        return q
print(tail(5))

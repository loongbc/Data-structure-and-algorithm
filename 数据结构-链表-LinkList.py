# _*_coding:utf-8_*_
# created by Amuu on 2022/9/5

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

print(a.item,a.next.item,a.next.next.item)

def create_linklist(li):  # 头插法
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head


def create_linklist_tail(li):  # 尾插法
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head


def print_linklist(lk):  # 链表的遍历
    while lk:
        print(lk.item, end=',')
        lk = lk.next


li = create_linklist([1, 2, 3, 4])
li1 = create_linklist_tail([1, 2, 3, 4])

print_linklist(li)
print_linklist(li1)

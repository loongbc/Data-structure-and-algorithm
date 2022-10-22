# _*_coding:utf-8_*_
# created by Amuu on 2021/10/20

from bst import BiTreeNode, BST


class AVLNode(BiTreeNode):
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0


class AVLTree(BST):
    def __init__(self, li=None):
        BST.__init__(self, li)

    def rotate_left(self, p, c):
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p

        c.lchild = p
        p.parent = c
        p.bf = 0
        c.bf = 0
        return c

    def rotate_right(self, li):
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s.parent = p

        c.rchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    def rotate_right_left(self, p, c):
        q = c.lchild

        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g

        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g

        # 更新bf
        if g.bf > 0:
            p.bf = -1
            c.bg = 0
        elif g.bg < 0:
            p.bg = 0
            c.bf = 1
        else:
            p.bf = 0
            c.bf = 0
        g.bf = 0
        return g

    def rotate_left_right(self, p, c):
        q = c.rchild

        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c
        g.lchild = c
        c.parent = g

        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g

        # 更新bf
        if g.bf > 0:
            p.bf = 0
            c.bf = -1
        elif g.bf < 0:
            p.bf = 1
            c.bf = 0
        else:
            p.bf = 0
            c.bf = 0
        g.bf = 0
        return g

    # def insert_no_rec(self, val):
    #     # 和BST一样，插入
    #     p = self.root
    #     if not p:  # 空树
    #         self.root = BiTreeNode(val)
    #         return
    #     while True:
    #         if val < p.data:
    #             if p.lchild:
    #                 p = p.lchild
    #             else:
    #                 p.lchild = BiTreeNode(val)
    #                 p.lchild.parent = p
    #                 node = p.lchild  # node 存储的就是插入的节点
    #                 break
    #         elif val > p.data:
    #             if p.rchild:
    #                 p = p.rchild
    #             else:
    #                 p.rchild = BiTreeNode(val)
    #                 p.rchild.parent = p
    #                 node = p.rchild
    #                 break
    #         else:  # val == p.data
    #             return
    #     # 更新 balance factor
    #     while node.parent:  # node.parent不空
    #         if node.parent.lchild == node:  # 传递是从左子树来的，左子树更沉了
    #             # 更新node.parent的bf -=1
    #             if node.parent.bf < 0:  # 原来node.parent.bf ==-1，更新后变-2
    #                 # 做旋转
    #                 # 看node哪边沉
    #                 g = node.parent.parent  # 为了连接旋转之后的子树
    #                 x = node.parent  # 旋转前的子树的根
    #                 if node.bf > 0:
    #                     m = self.rotate_left_right(node.parent, node)
    #                 else:
    #                     n = self.rotate_right(node.parent, node)
    #                 # 记得：把n和g连起来
    #             elif node.parent.bf > 0:  # 原来node.parent.bf = 1，更新之后变为0
    #                 node.parent.bf = 0
    #                 break
    #             else:  # 原来node.parent.bf = 0，更新之后变为-1
    #                 node.parent.bf = -1
    #                 node = node.parent
    #                 continue
    #         else:  # 传递是从右子树来的，右子树变沉了
    #             # 更新node.parent.bf +=1
    #             if node.parent.bf > 0:  # 原来node.parent.bf ==1，更新后变为2
    #                 # 做旋转
    #                 # 看node哪边沉
    #                 g = node.parent.parent  # 为了连接旋转之后的子树
    #                 x = node.parent  # 旋转前的子树的根
    #                 if node.bg < 0:
    #                     n = self.rotate_right_left(node.parent, node)
    #                 else:  # node.bf = -1
    #                     n = self.rotate_left(node.parent, node)
    #                 # 记得连起来
    #             elif node.parent.bf < 0:  # 原来node.parent.bf = -1，更新之后变为0
    #                 node.parent.bf = 0
    #                 break
    #             else:  # 原来node.parent.bf = 0 ，更新之后变为1
    #                 node.parent.bf = 1
    #                 node = node.parent
    #                 continue
    #         # 连接旋转后的子树
    #         n.parent = g
    #         if g:  # g不是空
    #             if node.parent == g.lchild:
    #                 g.lchild = n
    #             else:
    #                 g.rchild = n
    #             break
    #         else:
    #             self.root = n
    #             break


tree = AVLTree([9, 8, 7, 6, 5, 4, 3, 2, 1])
tree.pre_order(tree.root)
print("")
tree.in_order((tree.root))

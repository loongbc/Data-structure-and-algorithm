# _*_coding:utf-8_*_
# created by Amuu on 2021/10/13


#  二叉搜索树

class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子
        self.parent = None


class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)

    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:

            noda.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node

        elif val > node.data:

            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
            return node

    def insert_no_rec(self, val):
        p = self.root
        if not p:  # 空树
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
            else:
                return

    def query(self, node, val):
        if not node:
            return None
        if node.data < val:
            return self.query(node.rchild, val)
        elif node.data > val:
            return self.query(node.lchild, val)
        else:
            return node

    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None

    def __remove_node_1(self, node):
        # 情况1 node 是叶子节点
        if not node.parent:
            self.root = None
        if node == node.parent.lchild:  # node是他父亲的左孩子
            node.parent.lchild = None
            node.parent = None
        else:  # 右孩子
            node.parent.rchild = None

    def __remove_node_2_1(self, node):
        # 情况2 node只有一个左孩子
        if not node.parent:
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:  # node是他父亲的左孩子
            parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:  # 右孩子
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_2_2(self, node):
        # 情况2 node只有一个右孩子
        if not node.parent:
            self.root = node.rchild
            node.rchild.parent = None
        elif node == node.parent.lchild:  # node是他父亲的左孩子
            node.parent.lchild = node.rchild
            node.lchild.parent = node.parent
        else:  # 右孩子
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self,val):
        if self.root:
            node = self.query_no_rec(val)
            if not node:
                return False
            if not node.lchild and not node.rchild:  # 1. 叶子节点
                self.__remove_node_1(node)
            elif not node.rchild:  # 2.1  只有一个左孩子
                self.__remove_node_2_1(node)
            elif not node.lchild:  # 2.2  只有一个右孩子
                self.__remove_node_2_2(node)
            else:  # 3.  两个孩子都有
                min_node = node.rchild
                while min_node.lchild:
                    min_node =min_node.lchild
                node.data = min_node.data
                #  删除 min_node
                if min_node.rchild:
                    self.__remove_node_2_2(min_node)
                else:
                    self.__remove_node_2_1(min_node)


    #  前序遍历
    def pre_order(self, root):
        if root:
            print(root.data, end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    #  中序遍历
    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=',')
            self.in_order(root.rchild)

    #  后序遍历
    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=',')

import random

li = list(range(0, 10))
random.shuffle(li)
tree = BST(li)

tree.in_order(tree.root)
print('')
tree.delete(4)
tree.in_order(tree.root)

tree.pre_order(tree.root)
print('')
tree.in_order(tree.root)
print('')
tree.post_order(tree.root)

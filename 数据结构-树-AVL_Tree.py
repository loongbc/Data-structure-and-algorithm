# _*_coding:utf-8_*_
# created by Amuu on 2022/9/6


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子
        self.parent = None
        self.bf = 0


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

            node.lchild = self.insert(node.lchild, val)
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
            node.parent.lchild = node.lchild
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

    def delete(self, val):
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
                    min_node = min_node.lchild
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


class AVLNode(BiTreeNode):  # 类的继承
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0  # balance facter


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

    def rotate_right(self, p, c):
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p

        c.rchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    def rotate_right_left(self, p, c):
        g = c.lchild

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
            c.bf = 0
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else:  # 插入的是g
            p.bf = 0
            c.bf = 0
        g.bf = 0
        return g

    def rotate_left_right(self, p, c):
        g = c.rchild

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
        else:  # 插入的是g
            p.bf = 0
            c.bf = 0
        g.bf = 0
        return g

    def insert_no_rec(self, val):
        # 和BST一样，插入
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
                    node = p.lchild  # node 存储的就是插入的节点
                    break
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    node = p.rchild
                    break
            else:  # val == p.data
                return
        # 更新 balance factor
        while node.parent:  # node.parent不空
            if node.parent.lchild == node:  # 传递是从左子树来的，左子树更沉了
                # 更新node.parent的bf -=1
                if node.parent.bf < 0:  # 原来node.parent.bf ==-1，更新后变-2
                    # 做旋转
                    # 看node哪边沉
                    g = node.parent.parent  # 为了连接旋转之后的子树
                    x = node.parent  # 旋转前的子树的根
                    if node.bf > 0:
                        n = self.rotate_left_right(node.parent, node)
                    else:
                        n = self.rotate_right(node.parent, node)
                    # 记得：把n和g连起来
                elif node.parent.bf > 0:  # 原来node.parent.bf = 1，更新之后变为0
                    node.parent.bf = 0
                    break
                else:  # 原来node.parent.bf = 0，更新之后变为-1
                    node.parent.bf = -1
                    node = node.parent  # 不需要旋转 需要向上传递
                    continue
            else:  # 传递是从右子树来的，右子树变沉了
                # 更新node.parent.bf +=1
                if node.parent.bf > 0:  # 原来node.parent.bf ==1，更新后变为2
                    # 做旋转
                    # 看node哪边沉
                    g = node.parent.parent  # 为了连接旋转之后的子树
                    x = node.parent  # 旋转前的子树的根
                    if node.bg < 0:
                        n = self.rotate_right_left(node.parent, node)
                    else:  # node.bf = -1
                        n = self.rotate_left(node.parent, node)
                    # 记得连起来
                elif node.parent.bf < 0:  # 原来node.parent.bf = -1，更新之后变为0
                    node.parent.bf = 0
                    break
                else:  # 原来node.parent.bf = 0 ，更新之后变为1
                    node.parent.bf = 1
                    node = node.parent
                    continue
            # 连接旋转后的子树
            n.parent = g
            if g:  # g不是空
                if x == g.lchild:
                    g.lchild = n
                else:
                    g.rchild = n
                break
            else:
                self.root = n
                break


tree = AVLTree([9, 8, 7, 6, 5, 4, 3, 2, 1])
tree.pre_order(tree.root)
print("")
tree.in_order((tree.root))

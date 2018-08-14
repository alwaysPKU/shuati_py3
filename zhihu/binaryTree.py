'''
           A
         /  \
        B    C
       / \  / 
      D  E F 
'''

class BinaryTreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return self.root == None

    def preOrder(self,BinaryTreeNode):
        if BinaryTreeNode == None:
            return
        # 先打印根结点，再打印左结点，后打印右结点
        print(BinaryTreeNode.data)
        self.preOrder(BinaryTreeNode.left)
        self.preOrder(BinaryTreeNode.right)

    def inOrder(self,BinaryTreeNode ,list):
        if BinaryTreeNode == None:
            return
        # 先打印左结点，再打印根结点，后打印右结点
        self.inOrder(BinaryTreeNode.left,list)
        # print(BinaryTreeNode.data)
        list.data=BinaryTreeNode.data
        list=list.next
        self.inOrder(BinaryTreeNode.right,list)

    def postOrder(self,BinaryTreeNode):
        if BinaryTreeNode == None:
            return
        # 先打印左结点，再打印右结点，后打印根结点
        self.postOrder(BinaryTreeNode.left)
        self.postOrder(BinaryTreeNode.right)
        print(BinaryTreeNode.data)

class ListNode(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = ListNode


n1 = BinaryTreeNode(data="D")
n2 = BinaryTreeNode(data="E")
n3 = BinaryTreeNode(data="F")
n4 = BinaryTreeNode(data="B", left=n1, right=n2)
n5 = BinaryTreeNode(data="C", left=n3, right=None)
root = BinaryTreeNode(data="A", left=n4, right=n5)
bt = BinaryTree(root)

head = ListNode(data=1)
list = head.next
print(type(list))

bt.inOrder(bt.root,list)

while head:
    print(head.data)
    head=head.next

# print('先序遍历')
# bt.preOrder(bt.root)
# print('中序遍历')
# bt.inOrder(bt.root)
# print('后序遍历')
# bt.postOrder(bt.root)
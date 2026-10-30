# ============================================================
# 链表与二叉树 10 · 翻转二叉树
# ============================================================
# 【题目】把每个节点的左右子树互换（Homebrew 作者名题）。
# 【要求】实现 invert(root)。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert(root):
    if root is None:
        return None
    invert(root.left)
    invert(root.right)
    return root  # 没有交换左右

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
inverted = invert(root)

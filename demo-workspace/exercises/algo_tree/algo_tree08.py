# ============================================================
# 链表与二叉树 08 · 对称二叉树
# ============================================================
# 【题目】判断二叉树是否镜像对称。
# 【要求】实现 is_symmetric(root)，双指针递归。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
    def same(a, b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        return a.val == b.val  # 子树没继续比
    return same(root.left, root.right) if root else True

sym = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
asym = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(2, TreeNode(3)))

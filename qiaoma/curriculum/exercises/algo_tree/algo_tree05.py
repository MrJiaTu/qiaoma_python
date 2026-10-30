# ============================================================
# 链表与二叉树 05 · 二叉树最大深度
# ============================================================
# 【题目】求二叉树的深度：根 [3,9,20,None,None,15,7] → 3。
# 【要求】实现 max_depth(root)，递归。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    if root is None:
        return 0
    return max_depth(root.left)  # 只看左子树

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

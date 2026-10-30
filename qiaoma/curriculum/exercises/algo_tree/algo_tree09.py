# ============================================================
# 链表与二叉树 09 · 二叉树最近公共祖先
# ============================================================
# 【题目】给两个节点值 p、q，找最近公共祖先的值。
# 【要求】实现 lca(root, p, q)。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lca(root, p, q):
    if root is None or root.val == p or root.val == q:
        return root.val if root else None
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root.val
    return left if left else None  # 右侧结果丢了

root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2)), TreeNode(1, TreeNode(0), TreeNode(8)))

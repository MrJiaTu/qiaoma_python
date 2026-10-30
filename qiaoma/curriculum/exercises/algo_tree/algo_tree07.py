# ============================================================
# 链表与二叉树 07 · 验证二叉搜索树
# ============================================================
# 【题目】BST 要求左 < 根 < 右，且对所有子孙成立。
# 【要求】实现 is_bst(root)，传入上下界。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_bst(root):
    def check(node, low, high):
        if node is None:
            return True
        if node.val <= low or node.val >= high:
            return False
        return check(node.left, low, high)  # 边界没收紧
    return check(root, float("-inf"), float("inf"))

bad = TreeNode(5, TreeNode(1), TreeNode(6, TreeNode(3), TreeNode(7)))
good = TreeNode(5, TreeNode(1), TreeNode(6, None, TreeNode(7)))

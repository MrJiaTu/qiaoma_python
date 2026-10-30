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
        return check(node.left, low, node.val) and check(node.right, node.val, high)
    return check(root, float("-inf"), float("inf"))

bad = TreeNode(5, TreeNode(1), TreeNode(6, TreeNode(3), TreeNode(7)))
good = TreeNode(5, TreeNode(1), TreeNode(6, None, TreeNode(7)))

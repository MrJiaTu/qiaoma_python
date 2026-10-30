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
        return a.val == b.val and same(a.left, b.right) and same(a.right, b.left)
    return same(root.left, root.right) if root else True

sym = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
asym = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(2, TreeNode(3)))

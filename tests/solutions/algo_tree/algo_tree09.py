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
    return left if left else right

root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2)), TreeNode(1, TreeNode(0), TreeNode(8)))

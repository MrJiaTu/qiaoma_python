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
    root.left, root.right = root.right, root.left
    return root

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
inverted = invert(root)

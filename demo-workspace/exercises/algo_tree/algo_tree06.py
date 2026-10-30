# ============================================================
# 链表与二叉树 06 · 二叉树层序遍历
# ============================================================
# 【题目】按层输出：[3,9,20,None,None,15,7] → [[3],[9,20],[15,7]]。
# 【要求】实现 level_order(root)，用队列。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            # 子节点没入队
        result.append(level)
    return result

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

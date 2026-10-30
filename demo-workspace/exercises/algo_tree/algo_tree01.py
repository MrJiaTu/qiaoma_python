# ============================================================
# 链表与二叉树 01 · 反转链表
# ============================================================
# 【题目】1→2→3→4→5 反转成 5→4→3→2→1。
# 【要求】实现 reverse_list(head)，迭代法。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build(values):
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def reverse_list(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        # cur 忘了前进
    return prev

# ============================================================
# 链表与二叉树 04 · 删除倒数第 N 个节点
# ============================================================
# 【题目】1→2→3→4→5 删除倒数第 2 个 → 1→2→3→5。
# 【要求】实现 remove_nth(head, n)，快慢指针一趟完成。
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

def remove_nth(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next.next  # 多跳了一步
    return dummy.next

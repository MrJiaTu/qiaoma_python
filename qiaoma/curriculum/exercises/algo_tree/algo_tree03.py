# ============================================================
# 链表与二叉树 03 · 环形链表检测
# ============================================================
# 【题目】判断链表是否有环：快慢指针。
# 【要求】实现 has_cycle(head)。
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

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next  # 快指针要一次走两步
        if slow is fast:
            return True
    return False

# 构造带环链表：1→2→3→2
h = build([1, 2, 3])
h.next.next.next = h.next

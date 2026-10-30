# ============================================================
# 链表与二叉树 02 · 合并两个有序链表
# ============================================================
# 【题目】合并 1→3→5 与 2→4→6 为 1→2→3→4→5→6。
# 【要求】实现 merge_two(a, b)，用哨兵节点。
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

def merge_two(a, b):
    dummy = ListNode()
    tail = dummy
    while a and b:
        if a.val <= b.val:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        # tail 忘了前进
    tail.next = a or b
    return dummy.next

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# [3,2,0,-4]
        
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head


def hasCycle(head):
    print(head)
    slow = head
    fast = head.next

    while slow is not None and fast is not None:
        print(slow.val,fast.val)
        if slow.val == fast.val:
            print("value are equals")
            return True
        slow = slow.next
        fast = fast.next.next
    return False



print(hasCycle(head))

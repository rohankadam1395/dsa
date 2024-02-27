class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self,val):
        node = ListNode(val)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insertAtEnd(self,val):
        node = ListNode(val)
        if self.head is None:
            self.head = node
        else:
            lastNode = self.head
            while lastNode.next:
                lastNode = lastNode.next
            lastNode.next = node




list1 = [1]
linkeList1 = LinkedList()
for num in list1:
    linkeList1.insertAtEnd(num)

def removeNthFromEnd(head, n):
    # print(head,n)

    slow = head
    fast = head


    for i in range(0,n):
        fast  = fast.next

    prev = None

    while fast is not None:
        prev = slow
        slow = slow.next
        fast = fast.next

    if prev is None:
        head = head.next
    else:
        prev.next = slow.next

    # print(slow)
    return head



print(removeNthFromEnd(linkeList1.head,1))
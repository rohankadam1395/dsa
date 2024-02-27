import copy
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




list1 = [1,1,1,2,4]
list2 = [1,3,4,4,4,4,4,4]
linkeList1 = LinkedList()
linkeList2 = LinkedList()

for num in list1:
    linkeList1.insertAtEnd(num)
for num in list2:
    linkeList2.insertAtEnd(num)






def mergeTwoLists(list1, list2):
    print(list1.head.val,list2.head.val)

    head1  = list1.head
    head2 = list2.head

    newList  = LinkedList()

    while head1 is not None or head2 is not None:
        if head1 is not None and head2 is not None: 
            if head1.val <= head2.val:
                newList.insertAtEnd(head1.val)
                head1=head1.next
            else:
                newList.insertAtEnd(head2.val)
                head2=head2.next
        elif head1 is None:
            newList.insertAtEnd(head2.val)
            head2=head2.next
        else:
            newList.insertAtEnd(head1.val)
            head1=head1.next

    return newList.head









print(mergeTwoLists(linkeList1,linkeList2))
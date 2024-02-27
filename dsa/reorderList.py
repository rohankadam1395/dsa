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




list1 = [1,2,3,4,5]
linkeList1 = LinkedList()
for num in list1:
    linkeList1.insertAtEnd(num)

def reorderList(head):
    # print(head)
    slow = head
    fast = head

    while fast is not None and fast.next is not None :
        fast = fast.next.next
        slow = slow.next
    mid = slow

    # print(slow.val)
    # print(head.val)
    prevNode = None
    currentNode = mid

    while currentNode is not None:
        temp = currentNode.next
        currentNode.next =prevNode
        prevNode = currentNode
        currentNode = temp
    # print(prevNode)

    # head
    # prevNode
    # dummyNode = ListNode()
    # currentDummy= dummyNode

    # while True:
    #     if head == mid:
    #         break

    #     if prevNode is None:
    #         break 

    #     currentDummy.next = head
    #     head = head.next
    #     currentDummy = currentDummy.next

    #     currentDummy.next = prevNode
    #     prevNode = prevNode.next
    #     currentDummy=currentDummy.next
        
    # print(dummyNode)

    tail = head

    while True:
        if tail == mid:
            tail.next = None
            break
        if prevNode is None:
            break
        tempPrev = prevNode.next
        tempTail = tail.next

        prevNode.next = tail.next
        tail.next = prevNode
        prevNode = tempPrev
        tail = tempTail

       


        






    # print("top of stack",stack.pop().val)
    # print(stack)




    



reorderList(linkeList1.head)

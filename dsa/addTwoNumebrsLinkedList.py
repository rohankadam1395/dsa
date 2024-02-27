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




list1 = [0]
linkeList1 = LinkedList()
list2 = [0]
linkeList2 = LinkedList()
for num in list1:
    linkeList1.insertAtEnd(num)
for num in list2:
    linkeList2.insertAtEnd(num)

def addTwoNumbers(l1, l2):
    # print(l1,l2)
    headA = l1.head
    headB = l2.head
    ptA = headA
    ptB = headB

    lengthA = 0
    while ptA:
        lengthA = lengthA + 1
        ptA = ptA.next

    lengthB = 0
    while ptB:
        lengthB = lengthB + 1
        ptB = ptB.next

    # print(lengthA,lengthB)
    answer = ListNode()
    currentAnswer = answer
    if lengthA  == lengthB:
        remainder = 0
        while headA:
            sum = headA.val + headB.val + remainder
            remainder = sum // 10
            currentAnswer.next = ListNode(sum % 10)
            headA = headA.next
            headB = headB.next
            currentAnswer =  currentAnswer.next
        if remainder !=0:
            currentAnswer.next = ListNode(remainder)
    else:
        larger = None
        smaller = None
        if lengthA > lengthB:
            larger = headA
            smaller = headB
        else:
            larger = headB
            smaller = headA
        #
        # copyAsItis = abs(lengthA - lengthB)
        # while copyAsItis !=0:
        #     currentAnswer.next = larger
        #     currentAnswer = currentAnswer.next
        #     larger = larger.next
        #     copyAsItis = copyAsItis -1

        remainder = 0
        while larger:
            if smaller is None:
                smaller = ListNode(0)
            sum = larger.val + smaller.val + remainder
            remainder = sum // 10
            currentAnswer.next = ListNode(sum % 10)
            larger = larger.next
            smaller = smaller.next
            currentAnswer = currentAnswer.next
        if remainder != 0:
            currentAnswer.next = ListNode(remainder)

    # print(answer.next)
    return answer.next


# prevA = None
# currentA = headA
# lengthA = 0
# lengthB = 0

# while currentA is not None:
#     temp = currentA.next
#     currentA.next = prevA
#     prevA = currentA
#     currentA = temp
#     lengthA = lengthA + 1
# print(prevA)

# currentB = headB
# prevB = None
# while currentB is not None:
#     temp = currentB.next
#     currentB.next=prevB
#     prevB = currentB
#     currentB = temp
#     lengthB = lengthB + 1
# print(prevB)

# print(lengthA,lengthB)
# answer  = ListNode()
# currentAnswer = answer
# if lengthA == lengthB:
#     remainder = 0
#     while prevA is not None:
#         sum = prevA.val + prevB.val + remainder
#         remainder = sum // 10

#         currentAnswer.next = ListNode(sum%10)
#         currentAnswer = currentAnswer.next

#         prevA = prevA.next
#         prevB = prevB.next
# else:
#     larger = None
#     smaller = None
#     if lengthA > lengthB:
#         larger = prevA
#         smaller = prevB
#     else:
#         larger = prevB
#         smaller = prevA
#     extraLength = abs(lengthA - lengthB)
#     for i in range(0,extraLength):
#         currentAnswer.next = larger
#         larger = larger.next
#         currentAnswer = currentAnswer.next
#     remainder = 0
#     while larger is not None:
#         sum = larger.val + smaller.val + remainder
#         remainder = sum // 10

#         currentAnswer.next = ListNode(sum%10)
#         currentAnswer = currentAnswer.next

#         larger = larger.next
#         smaller = smaller.next


# while answer.val ==0:
#     answer = answer.next
# print(answer)
# return answer









    

print(addTwoNumbers(linkeList1,linkeList2))


#  427 803
# might not need to reverse



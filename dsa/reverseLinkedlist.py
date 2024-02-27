
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
    

        



data = [1,2,3,4,5]
listNodes = LinkedList()

for i in range(0,len(data)):
    listNodes.insertAtBegin(data[i])

print(listNodes)



orginalList=None
next = None



    


    
def reverseList(head):
    temp = head
    reversedList = None

    while temp:
        # print(temp.val)
        nextItem = temp.next
        temp.next = reversedList
        reversedList = temp
        temp = nextItem
    return reversedList



reverseList(listNodes.head)
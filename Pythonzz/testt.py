# Storing sum on the longer list
class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution:
    def reverse(self, head):
        if head is None or head.next is None:
            return head
        curr = head
        prev = None
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    def addTwoLists(self, head1, head2):
       
        head1 = self.reverse(head1)
        head2 = self.reverse(head2)
        
        carry = 0
        sumList = None

        # Loop until both lists and carry are exhausted
        while head1 is not None or head2 is not None or carry > 0:
            newVal = carry
            if head1 is not None:
                newVal += head1.data
                head1 = head1.next
            if head2 is not None:
                newVal += head2.data
                head2 = head2.next
            carry = newVal // 10
            newVal = newVal % 10

            # Create a newNode and link it to the front
            newNode = LinkedList(newVal)
            newNode.next = sumList
            sumList = newNode
        return sumList


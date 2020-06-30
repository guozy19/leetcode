# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        if head==None:
            return None
        length=1
        temp=head
        right=head
        while temp.next!=None:
            temp=temp.next
            length+=1
        if n==length:
            return head.next
        for i in range(length-n+1):
            right=right.next
        nodelist=[]
        temp=head
        for i in range(length-n):
            nodelist.append(temp)
            temp=temp.next
        ans=head
        for i in nodelist:
            head.next=i
            head=head.next
        head.next=right
        return ans
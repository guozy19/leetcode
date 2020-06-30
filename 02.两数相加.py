# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        begin=ListNode(0)
        l3=begin
        s=0
        t=0
        while l1!=None and l2!=None:
            s=l1.val+l2.val+t
            t=(s//10)
            l3.next=ListNode(s%10)
            l3=l3.next
            l1=l1.next
            l2=l2.next
        while l1!=None or l2!=None:
            if l1==None and l2!=None:
                s=l2.val+t
                t=(s//10)
                l3.next=ListNode(s%10)
                l3=l3.next
                l2=l2.next
            if l2==None and l1!=None:
                s=l1.val+t
                t=(s//10)
                l3.next=ListNode(s%10)
                l3=l3.next
                l1=l1.next
        if t==1:
            l3.next=ListNode(1)
        return begin.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2) :
        if l1==None:
            return l2
        if l2==None:
            return l1
        l1val=[]
        l2val=[]
        l1_1=l1
        l2_1=l2
        while l1_1!=None:
            l1val.append(l1_1.val)
            l1_1=l1_1.next
        while l2_1!=None:
            l2val.append(l2_1.val)
            l2_1=l2_1.next
        lval=l2val+l1val
        lval.sort()
        l3=[]
        for i in lval:
            l3.append(ListNode(i))
        for c in range(len(lval)):
            if c==len(lval)-1:
                l3[c].next=None
                break
            l3[c].next=l3[c+1]
        return l3[0]
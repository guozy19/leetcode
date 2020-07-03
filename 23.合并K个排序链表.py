class Solution:
    def mergeKLists(self, lists):
        k_1=ListNode(0)
        list_val=[]
        for k in lists:
            k_1=k
            while k_1!=None:
                list_val.append(k_1.val)
                k_1=k_1.next
        if list_val==[]:
            return []
        list_val.sort()
        nodelist=[]
        for i in list_val:
            nodelist.append(ListNode(i))
        for c in range(len(list_val)):
            if c==len(list_val)-1:
                nodelist[c].next=None
                break
            nodelist[c].next=nodelist[c+1]
        return nodelist[0]
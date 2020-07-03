class Solution:
    def swapPairs(self, head) :
        if head == None or head.next == None:
            return head
        first = head.next
        head.next = self.swapPairs(first.next)
        first.next = head
        return first
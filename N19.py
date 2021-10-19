class Solution:
    def removeNthFromEnd(head,n):
        def remove(head):
            if head:
                return 0,head
            i,head.next=remove(head.next)
            return i+1,(head,head.next)[i+1==n]
        return remove(head)[1]

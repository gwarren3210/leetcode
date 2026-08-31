# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            #print(curr.val)
            #self.printNode(prev)
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        #self.printNode(prev)
        return prev if prev else curr

    def printNode(self, n: ListNode):
        print("====Print Node====")
        while(n):
            print(n.val)
            n = n.next
        print()
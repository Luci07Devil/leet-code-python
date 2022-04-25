# Problem 2
#You are given two non-empty linked lists representing two non-negative integers.
#The digits are stored in reverse order, and each of their nodes contains a single digit.
#Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = ListNode()
        cur = sum
        
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0 # if val - present, else val1 = 0
            val2 = l2.val if l2 else 0
            
            val = val1 + val2 + carry # actual addition 
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val) # assginging node to carry
            
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if(carry>0):
            cur.next = ListNode(carry)
        return sum.next

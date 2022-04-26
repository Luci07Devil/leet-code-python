# Problem 9
'''
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

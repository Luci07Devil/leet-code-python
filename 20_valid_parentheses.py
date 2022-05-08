# Problem 20
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
'''

class Solution:
    def isValid(self, s: str) -> bool:
        leftSymbols = []
        # Loop for each character of the string
        for c in s:
            # If left symbol is encountered
            if c in ['(', '{', '[']:
                leftSymbols.append(c)
            # If right symbol is encountered
            elif c == ')' and len(leftSymbols) != 0 and leftSymbols[-1] == '(':
                leftSymbols.pop()
            elif c == '}' and len(leftSymbols) != 0 and leftSymbols[-1] == '{':
                leftSymbols.pop()
            elif c == ']' and len(leftSymbols) != 0 and leftSymbols[-1] == '[':
                leftSymbols.pop()
            # If none of the valid symbols is encountered
            else:
                return False
        return leftSymbols == []
        

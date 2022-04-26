# Problem 14
'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range (len (strs[0])):
            # loop through every charater of first string
            for s in strs:
                # loop through every string in strs
                if i == len(s) or s[i] != strs[0][i]:
                    # i == len(s) - to make sure i limit is in bound to lenght of string s
                    return res
            res += strs[0][i]
        return res

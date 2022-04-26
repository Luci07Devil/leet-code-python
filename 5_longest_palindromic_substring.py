# Problem 5
#Given a string s, return the longest palindromic substring in s.

#Input: s = "babad"
#Output: "bab"
#Explanation: "aba" is also a valid answer.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        pal = ""
        palLen = 0
        for i in range(len(s)):
            # odd length
            l, r = i, i
            # keep the limit inbound within string length limit
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > palLen:
                    pal = s[l:r+1]
                    palLen = r - l + 1
                l -= 1
                r += 1
            # even length
            l, r = i, i + 1
            # keep the limit inbound within string length limit
            while l >= 0 and r< len(s) and s[l] == s[r]:
                if (r - l + 1) > palLen:
                    pal = s[l:r+1]
                    palLen = r - l + 1
                l -= 1
                r += 1
        return pal

# Problem 3
#Given a string s, find the length of the longest substring without repeating characters.

#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        st = set()
        lp = 0
        res = 0
        
        for rp in range(len(s)):
            while(s[rp] in st):
                st.remove(s[lp])
                lp+=1
            st.add(s[rp])
            res = max(res,rp-lp+1)
        return res

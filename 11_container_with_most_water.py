# Problem 11
'''
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        
        while l <r:
            area = (r - l) * min(height[l],height[r])
            res = max(res,area)
            
            if (height[l] < height[r]):
                l +=1
            else:
                r -=1
        return res

'''
Time complexity: O(n)
Space complexity: O(n)
'''

# BRUTE FORCE METHOD
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        for l in range (len(height)):
          for r in range(l+1, len(height)):
            area = (r - l) * min(height[l],height[r])
            res = max(res,area)
        return res
'''

# Problem 18
'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Less than four elements in given numbers
        if len(nums) < 4:
            return []
        nums.sort()
        res = set([])
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                # Setting two pointers
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum == target:
                        new_res = (nums[i], nums[j], nums[k], nums[l])
                        # Checking for duplicates and adding four numbers into set
                        if new_res not in res:
                            res.add(new_res)
                        k += 1
                        l -= 1
                    elif sum < target:
                        k += 1
                    else:
                        l -= 1
        return res

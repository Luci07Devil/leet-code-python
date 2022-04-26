# Problem 7
'''
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Input: x = 123
Output: 321
'''

class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648 # -2^31,
        MAX = 2147483647 # 2^31 - 1
        res = 0
        y = x
        while y:
            digit = int(math.fmod(y, 10)) # normal % - returns different value incase of negative number, -1 % 10 = 9
            y = int(y / 10) # to get positive value -1 // 10 = -1
            if (res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10)):
                # for upper limit check - MAX
                # e.g. res = 214748365 > MAX // 10 or res = 214748364 == MAX // 10 and digit = 8 >= MAX % 10
                return 0
            if (res < MIN // 10 or (res == MIN // 10 and digit <= MIN % 10)):
                # for lower limit check - MIN
                # e.g. res = -214748365 < MIN // 10 or res = -214748364 == MIN // 10 and digit = 9 <= MIN % 10
                return 0
            res = (res * 10) + digit
        return res

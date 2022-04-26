# Problem 6
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res =""
        for r in range(numRows):
            #steps - to calculate the number of steps need to get the next charater in the zig-zag
            steps = (numRows - 1) * 2
            for i in range(r, len(s), steps):
                # step-wise looping to get intermediate characters in zig-zag
                res += s[i]
                if (r > 0 and r < numRows - 1 and i + steps - 2 *r < len(s)):
                    res += s[i + steps - 2 * r]
        return res

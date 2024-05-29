class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [''] * min(numRows, len(s))
        cur_row = 0
        going_down = False
        
        for c in s:
            rows[cur_row] += c
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            cur_row += 1 if going_down else -1
        
        return ''.join(rows)

# Example usage:
# solution = Solution()
# print(solution.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
# print(solution.convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"

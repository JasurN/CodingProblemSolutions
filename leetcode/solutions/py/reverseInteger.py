# Time complexity: O(log(n))
# Space complexity: O(1)
# Math (reminder) approach
class Solution:
    def reverse(self, x: int) -> int:
        divider = 10
        reversedInt = 0
        tempX = x
        x = abs(x)
        while x > 0:
            reversedInt = int(x % divider) + int(reversedInt * divider)
            x = int(x / 10)

        if pow(2, -31) > reversedInt or reversedInt > pow(2, 31) + 1:
            return 0
        if tempX >= 0:
            return reversedInt
        else:
            return reversedInt * -1


tempObj = Solution()
print(tempObj.reverse(1534236469))
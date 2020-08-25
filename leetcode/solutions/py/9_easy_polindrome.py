class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == reversed(x):
            return True
        return False

    def reverse(self, x: int) -> int:
        divider = 10
        reversedInt = 0
        tempX = x
        x = abs(x)
        while x > 0:
            reversedInt = int(x % divider) + int(reversedInt * divider)
            x = int(x / 10)
        return reversedInt


tempObj = Solution()
print(tempObj.isPalindrome(1534236469))

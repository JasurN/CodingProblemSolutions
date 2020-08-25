# Time complexity: O(log(n))
# Space complexity: O(1)
# Math (reverse) from 9th problem
def reverse(x: int) -> int:
    divider = 10
    reversedInt = 0
    x = abs(x)
    while x > 0:
        reversedInt = int(x % divider) + int(reversedInt * divider)
        x = int(x / 10)
    return reversedInt


class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == reverse(x):
            return True
        return False


tempObj = Solution()
print(tempObj.isPalindrome(1010))

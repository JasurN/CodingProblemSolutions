# Time complexity: O(n)
# Space complexity: O(1)
# Array manipulation approach
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastIndex = len(nums)
        index = 0
        for i in range(0, lastIndex):
            if nums[index] == 0:
                nums.pop(index)
                nums.insert(lastIndex - 1, 0)
            else:
                index += 1

        print(nums)


tempObj = Solution()
tempObj.moveZeroes([1, 0, 0, 3, 0])

# Time complexity: O(n^2)
# Space complexity: O(1)
# Brute force approach
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum = [0, 0]
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    two_sum[0] = i
                    two_sum[1] = j
                    return two_sum


# temp_obj = Solution()
# print(temp_obj.twoSum([2, 7, 11, 15], 9))
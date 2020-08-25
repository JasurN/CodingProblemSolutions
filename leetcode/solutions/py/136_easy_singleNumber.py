# Time complexity: O(n^2)
# Space complexity: O(1)
# Brut force approach
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i

# temp_obj = Solution()
#
# print(temp_obj.singleNumber([4, 1, 2, 1, 2]))

# Time complexity: O(n)
# Space complexity: O(n)
# Hash table approach
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = dict()
        for index, i in enumerate(nums):
            if i + hashTable.get(target - i, -9999) == target and index > 0:
                return [nums.index(hashTable[target - i]), index]
            else:
                hashTable[i] = i


temp_obj = Solution()
print(temp_obj.twoSum([0, 0], 0))

# Time complexity: O(n)
# Space complexity: O(n)
# Hash table approach
from collections import defaultdict
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashTable = defaultdict(int)
        for i in nums:
            hashTable[i] += 1

        for i in hashTable:
            if hashTable[i] == 1:
                return i


# temp_obj = Solution()
#
# print(temp_obj.singleNumber([4, 1, 2, 1, 2]))

# Time complexity: O(n)
# Space complexity: O(1)
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        counter = 0
        sum_temp = 0
        for j in range(0, k):
            sum_temp = sum_temp + arr[j]
        if sum_temp / k >= threshold:
            counter += 1
        h = 0
        for i in range(k, len(arr)):
            sum_temp = arr[i] + sum_temp - arr[h]
            h += 1
            if sum_temp / k >= threshold:
                counter += 1
        return counter

# temp_obj = Solution()
# print(temp_obj.numOfSubarrays([11,13,17,23,29,31,7,5,2,3], 3, 5))

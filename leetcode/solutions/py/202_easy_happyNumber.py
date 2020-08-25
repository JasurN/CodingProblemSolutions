# Time complexity: O(n)
# Space complexity: O(n^2)
# Hash table approach
from collections import defaultdict


class Solution:
    def isHappy(self, n: int) -> bool:
        sumArray = list(int(d) for d in str(n))
        hashTable = defaultdict(int)
        while True:
            temp_sum = 0
            for i in sumArray:
                temp_sum += pow(i, 2)

            if temp_sum == 1:
                return True
            elif temp_sum == hashTable[temp_sum]:
                return False
            else:
                hashTable[temp_sum] = temp_sum
            sumArray = list(int(d) for d in str(temp_sum))

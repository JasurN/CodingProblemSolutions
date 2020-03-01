# Time complexity: O(n^2)
# Space complexity: O(n^2)
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        temp_dictionary = {}
        for i in arr:
            if temp_dictionary.get(i) is None:
                temp_dictionary[i] = 1
            else:
                temp_dictionary[i] = temp_dictionary[i] + 1
        sorted_dict = {k: v for k, v in sorted(temp_dictionary.items(), key=lambda item: item[1], reverse=True)}
        # print(sorted_dict)
        # print("dictiorany length " + str(len(sorted_dict)))
        arr_len = len(arr)
        # print("list lenth " + str(arr_len))
        counter = 0
        sum_to_delete = 0

        for i in (iter(sorted_dict.values())):
            sum_to_delete = sum_to_delete + i
            counter = counter + 1
            if sum_to_delete >= arr_len / 2:
                break
        # print(counter)
        return counter


arr = [9, 77, 63, 22, 92, 9, 14, 54, 8, 38, 18, 19, 38, 68, 58, 19]
temp_obj = Solution()
temp_obj.minSetSize(arr)

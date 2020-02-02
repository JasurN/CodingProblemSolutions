from collections import OrderedDict
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dicts = OrderedDict([])
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if j == (len(mat[i]) - 1) and mat[i][j] == 0:
                    dicts[i] = j
                    break
                elif mat[i][j] == 0:
                    dicts[i] = j
                    break
                elif j == (len(mat[i]) - 1):
                    dicts[i] = j + 1
        # print(dicts)
        temp_dic = {k: v for k, v in sorted(dicts.items(), key=lambda item: item[1])}
        # print(temp_dic)
        temp_list = list(temp_dic.keys())
        # print(temp_list)
        return [temp_list[v] for v in range(0, k)]


a = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 1]]

ke = 3
objc = Solution()
objc.kWeakestRows(a, ke)

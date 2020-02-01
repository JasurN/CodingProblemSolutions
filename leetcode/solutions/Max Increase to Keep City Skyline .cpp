#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>> &grid) {
        vector<int> maxLeft, maxTop;
        int maximumHeigh = 0;
        for (int i = 0; i < grid.size(); i++) {
            maxLeft.push_back(grid[i][0]);
            maxTop.push_back(grid[0][i]);
            for (int j = 1; j < grid[i].size(); ++j) {
                if (maxLeft[i] < grid[i][j]) {
                    maxLeft[i] = grid[i][j];
                }
                if (maxTop[i] < grid[j][i]) {
                    maxTop[i] = grid[j][i];
                }
            }
        }

        int tempLeft = 0, tempTop = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[i].size(); j++) {
            tempLeft = maxLeft[i] - grid[i][j];
            if(tempLeft >= 0) {
                tempTop = maxTop[j] - (tempLeft + grid[i][j]);
                if (tempTop >= 0) {
                    grid[i][j] = tempLeft + grid[i][j];
                    maximumHeigh = maximumHeigh + tempLeft;
                } else {
                    grid[i][j] = tempTop + tempLeft + grid[i][j];
                    maximumHeigh = maximumHeigh + tempLeft + tempTop;
                }
            }

            }
        }
        cout << maximumHeigh << endl;
        return maximumHeigh;
    }
};

int main() {
    Solution solution;
    vector<vector<int>> grid = {{3, 0, 8, 4},
                                {2, 4, 5, 7},
                                {9, 2, 6, 3},
                                {0, 3, 1, 0}};
    solution.maxIncreaseKeepingSkyline(grid);
    return 0;
}
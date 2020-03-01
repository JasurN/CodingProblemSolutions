// Time complexity: O(n)
// Space complexity: O(1)
#include <iostream>
#include <cstring>
using namespace std;

class Solution {
public:
    string toLowerCase(string str) {
        for (char & i : str) {
            i = tolower(i);
        }
        return str;
    }
};
int main() {
    Solution solution;
    cout << solution.toLowerCase("JAsuRbEk");

    return 0;
}
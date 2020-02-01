#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int numberOfJewels = 0;
        for (char jChar: J) {
            for(char sChar: S) {
                if (jChar == sChar) {
                    numberOfJewels++;
                }
            }
        }
        return numberOfJewels;
    }
};

int main() {
    Solution solution;
    cout << solution.numJewelsInStones("aA","aAAbbbb");
}

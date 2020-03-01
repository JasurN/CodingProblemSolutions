// Time complexity: O(n)
// Space complexity: O(n)
#include <iostream>
#include <string>

using namespace std;
class Solution {
public:
    std::string defangIPaddr(std::string address) {
        std::string outputString;
        int counter = 0;
        int lastIndex = 0;
        for (char addres : address) {

            if (addres != '.') {
                outputString += addres;
            }else {
                outputString.append("[.]");
            }
        }
        return outputString;
    }
};

int main() {
    Solution solutionObj;
    std::cout << solutionObj.defangIPaddr("1.1.1.1");
    return 0;
}

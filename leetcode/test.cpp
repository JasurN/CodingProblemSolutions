#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int sum = 0;
    int current = 0;
    for (int i : a) {
        if(i == 1) {
            current++;
         }
        else {
                sum = max(current, sum);
                current = 0;
        }
    }
    sum = max(sum, current);
    cout << sum;
}
#include <iostream>

using namespace std;

int fibonacci_number(int n) {
    if (n == 0) {
        return 0;
    } else if (n == 1) {
        return n;
    } else {
        return fibonacci_number(n - 2) + fibonacci_number(n - 1);
    }
}

int main() {
    cout << fibonacci_number(50);
    return 0;
}
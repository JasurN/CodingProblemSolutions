#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int firstValue = 0;
    long secondValue = 0;
    char thirdValue = 0;
    float fourthValue = 0;
    double fifthValue = 0;
    scanf("%d %ld %c %f %lf", &firstValue, &secondValue, &thirdValue, &fourthValue, &fifthValue);
    printf("%d \n%ld \n%c \n%.3f \n%.9f", firstValue, secondValue, thirdValue, fourthValue, fifthValue);
    return 0;
}
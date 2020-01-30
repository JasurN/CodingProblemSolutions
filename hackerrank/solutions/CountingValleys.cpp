#include <bits/stdc++.h>

using namespace std;

// Complete the countingValleys function below.
int countingValleys(int n, string s) {
    bool alreadyValleyCounted = false;
    int valleyCount = 0;
    int seaLevel = 0;
    for (char i : s) {
        if(i == 'U'){
            seaLevel++;
        } else {
            seaLevel--;
        }
        if(seaLevel < 0 && !alreadyValleyCounted) {
            valleyCount++;
            alreadyValleyCounted = true;
            continue;
        }
        if (seaLevel >= 0 && alreadyValleyCounted) {
            alreadyValleyCounted = false;
        }
    }
    cout << valleyCount;
    return valleyCount;
}

int main() {
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string s;
    getline(cin, s);

    int result = countingValleys(n, s);

    fout << result << "\n";

    fout.close();

    return 0;
}

#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

// Complete the dayOfProgrammer function below.
string dayOfProgrammer(int year) {
    int february = 28;
    int sum = 215;
    if(year >= 1700 && year <=2700) {
        if(year == 1918) {
            february = february - 13;

        }
        else if(year > 1918) {
            if((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0)) {
                february++;
            }
        }
        else if(year % 4 == 0) {
            february++;
        }
        sum = sum + february;
        int dayOfProgrammer = 256 - sum;
        string day= to_string(dayOfProgrammer)+ "." + "09." + to_string(year);
        cout << day;
        return  day;
    } else {
        return "year is not valid";
    }
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string year_temp;
    getline(cin, year_temp);

    int year = stoi(ltrim(rtrim(year_temp)));

    string result = dayOfProgrammer(year);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
            s.begin(),
            find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
            find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
            s.end()
    );

    return s;
}


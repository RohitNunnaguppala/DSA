#include<bits/stdc++.h>
using namespace std;

string addBinary(string a, string b) {
        string result = "";
        int carry = 0;
        int i = a.size() - 1, j = b.size() - 1;
        
        while (i >= 0 || j >= 0 || carry) {
            int sum = carry;
            if (i >= 0) sum += a[i--] - '0';
            if (j >= 0) sum += b[j--] - '0';
            result += to_string(sum % 2);
            carry = sum / 2;
        }
        reverse(result.begin(), result.end());
        
        return result;
    }

int main() {
    string a = "11";
    string b = "1";
    cout << "Binary sum of " << a << " and " << b << " is " << addBinary(a, b) << endl;

    a = "1010";
    b = "1011";
    cout << "Binary sum of " << a << " and " << b << " is " << addBinary(a, b) << endl;

    a = "1101";
    b = "101";
    cout << "Binary sum of " << a << " and " << b << " is " << addBinary(a, b) << endl;

    a = "0";
    b = "0";
    cout << "Binary sum of " << a << " and " << b << " is " << addBinary(a, b) << endl;

    return 0;
}
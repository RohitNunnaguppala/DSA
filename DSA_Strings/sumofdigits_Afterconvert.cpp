#include <bits/stdc++.h>
using namespace std;


int getLucky(string s, int k) {
        string num_str = "";
        for (char c : s) {
            int position = c - 'a' + 1; 
            num_str += to_string(position);
        }

        int num = 0;
        for (char c : num_str) {
            num += c - '0';  
        }

        for (int i = 1; i < k; i++) {
            int temp_sum = 0;
            while (num > 0) {
                temp_sum += num % 10;  
                num /= 10;
            }
            num = temp_sum;
        }

        return num;
    }

int main(){
    string s="leetcode";
    int k=2;
    int num=getLucky(s,k);
    cout<<num<<endl;

}
#include<bits/stdc++.h>
using namespace std;

string add(string num1,string num2){
    string ans;
    int index1=num1.size()-1,index2=num2.size()-1; 
    int sum,carry=0;
        while (index1 >= 0 || index2 >= 0) {
            sum = carry;
            if (index1 >= 0) {
                sum += (num1[index1] - '0');
                index1--;
            }
            if (index2 >= 0) {
                sum += (num2[index2] - '0');
                index2--;
            }
            carry = sum / 10;
            char c = '0' + sum % 10;
            ans += c;
        }
        if(carry){
            ans+='1';
        }
        reverse(ans.begin(),ans.end());
            return ans;
     }


    string addStrings(string num1, string num2) {
        if(num1.size()<num2.size()){
            return add(num2,num1);
        }
        else{
            return add(num1,num2);
        }
    }

int main(){
    string num1="11";
    string num2="123";
    string sol=add(num1,num2);
    cout<<sol<<endl;

}
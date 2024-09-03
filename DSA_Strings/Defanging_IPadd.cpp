#include<bits/stdc++.h>
using namespace std;

string defangingipadd(string s){
    int index=0;
    string ans;
    while(index<s.size()){
        if(s[index]=='.'){
            ans+="[.]";
        }
        else{
            ans+=s[index];
        }
        index++;
    }
    return ans;
}

int main(){
    string s="1.1.1.1";
    string sol=defangingipadd(s);
    cout<<sol<<endl;
}
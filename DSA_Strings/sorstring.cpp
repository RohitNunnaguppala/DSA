#include <bits/stdc++.h>
using namespace std;

string sortstring(string s){
    vector<int> alpha(26,0);
    for(auto c:s){
        alpha[c-'a']++;
    }
    string ans;
     for(int i=0;i<26;i++){
        char c='a'+i;
        while(alpha[i]){
            ans+=c;
            alpha[i]--;
        }
     }
     return ans;
}
int main(){
    string s="bacbbda";
    string sol=sortstring(s);
    cout<<sol;
}
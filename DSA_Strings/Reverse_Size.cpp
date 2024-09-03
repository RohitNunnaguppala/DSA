#include<bits/stdc++.h>
using namespace std;

int main(){
    string s="rohit";
    int start=0,end=s.size()-1;
    while(start<end){
        swap(s[start],s[end]);
        start++,end--;
    }
    cout<<s;

    int size=0;
    while(s[size]!='\0'){
        size++;
    }
    cout<<endl;
    cout<<size<<" ";
    return 0;
}
#include<bits/stdc++.h>
using namespace std;

string sortSentence(string s) {
        string ans[10];
        string temp;
        int count=0,index=0;
        while(index<s.size()){
            if(s[index]==' '){
                int pos=temp[temp.size()-1]-'0';
                temp.pop_back();
                ans[pos]=temp;
                temp.clear();
                count++;
            }
            else{
                temp+=s[index];
            }
            index++;
        }

        int pos = temp[temp.size() - 1] - '0';
        temp.pop_back();
        ans[pos] = temp;
        count++;
        temp.clear();


        for(int i=1;i<=count;i++){
            temp+=ans[i];
            if(i<count){
            temp+=' ';}
        }
        return temp;
}

int main(){
    string s="is2 sentence4 This1 a3";
    string sol=sortSentence(s);
    cout<<sol<<endl;
    return 0;
}

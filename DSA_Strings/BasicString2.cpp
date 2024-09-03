#include<bits/stdc++.h>
using namespace std;


int main(){
   string s;
   getline(cin,s);
   cout<<s<<endl;
   cout<<s.size();

   string s1="rohit", s2="nunnaguppala";
   string s3=s1.append(s2);
   cout<<s3<<endl;

   s1.push_back('N');
   cout<<s1<<endl;
   
   s1.pop_back();
   cout<<s1<<endl;

   s1=s1+"N";
   cout<<s1;

    string s4="rohit is a \"good\" boy";
   cout<<s4;
     




}
#include<bits/stdc++.h>
using namespace std;


string reverseVowels(string s) {
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        int left = 0;
        int right = s.size() - 1;
        
        while (left < right) {
            while (left < right && vowels.find(s[left]) == vowels.end()) {
                left++;
            }
            while (left < right && vowels.find(s[right]) == vowels.end()) {
                right--;
            }
            if (left < right) {
                swap(s[left], s[right]);
                left++;
                right--;
            }
        }
        return s;
}

int main() {
    string s1 = "hello";
    string s2 = "leetcode";
    string s3 = "aA";
    
    cout << "Original: " << s1 << " -> Reversed Vowels: " << reverseVowels(s1) << endl;
    cout << "Original: " << s2 << " -> Reversed Vowels: " << reverseVowels(s2) << endl;
    cout << "Original: " << s3 << " -> Reversed Vowels: " << reverseVowels(s3) << endl;

    return 0;
}
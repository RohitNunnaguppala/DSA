#include<bits/stdc++.h>
using namespace std;

int thirdMax(vector<int>& nums) {
        long long first = LONG_MIN, second = LONG_MIN, third = LONG_MIN;

        for (int num : nums) {
            if (num == first || num == second || num == third) {
                continue;
            }
            if (num > first) {
                third = second;
                second = first;
                first = num;
            } else if (num > second) {
                third = second;
                second = num;
            } else if (num > third) {
                third = num;
            }
        }
        return third == LONG_MIN ? first : third;
}

int main() {
    vector<int> nums1 = {3, 2, 1};
    cout << "Third max of {3, 2, 1} is " << thirdMax(nums1) << endl;

    vector<int> nums2 = {1, 2};
    cout << "Third max of {1, 2} is " << thirdMax(nums2) << endl;

    vector<int> nums3 = {2, 2, 3, 1};
    cout << "Third max of {2, 2, 3, 1} is " << thirdMax(nums3) << endl;

    return 0;
}
//
// Created by charles on 12/22/2023.
//
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeElement(vector<int> &nums, int val) {
        int l = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val) {
                nums[l] = nums[i];
                l++;
            }
        }
        return l;
    }
};

int main() {
    Solution sol;

    vector<int> case1 = {3, 2, 2, 3};
    int val1 = 3;
    cout << sol.removeElement(case1, val1) << "--";
    for (int num: case1) {
        cout << num << " ";
    }
    cout << endl;

    vector<int> case2 = {0, 1, 2, 2, 3, 0, 4, 2};
    int val2 = 2;
    cout << sol.removeElement(case2, val2) << "--";
    for (int num: case2) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}

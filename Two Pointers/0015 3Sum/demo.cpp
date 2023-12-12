// #include <algorithm>
// #include <iostream>
// #include <vector>
//
// using namespace std;
//
// vector<vector<int>> threeSum(vector<int> &nums) {
//     vector<vector<int>> result;
//     sort(nums.begin(), nums.end());
//     int length = nums.size();
//
//     for (int index = 0; index < length - 2; index++) {
//         if (index > 0 && nums[index] == nums[index - 1]) {
//             continue;
//         }
//
//         int start = index + 1, end = length - 1;
//
//         while (start < end) {
//             int sum = nums[index] + nums[start] + nums[end];
//             if (sum == 0) {
//                 result.push_back({nums[index], nums[start], nums[end]});
//                 while (start < end && nums[start] == nums[start + 1]) {
//                     start++;
//                 }
//                 while (start < end && nums[end] == nums[end - 1]) {
//                     end--;
//                 }
//                 start++;
//                 end--;
//             } else if (sum < 0) {
//                 start++;
//             } else {
//                 end--;
//             }
//         }
//     }
//
//     return result;
// }
//
// int main() {
//     vector<int> arr = {-1, 0, 1, 2, -1, -4};
//     vector<vector<int>> arr1 = threeSum(arr);
//
//     for (const auto &triplet : arr1) {
//         for (int num : triplet) {
//             cout << num << " ";
//         }
//         cout << endl;
//     }
//
//     return 0;
// }
//

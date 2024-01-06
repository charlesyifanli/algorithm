//
// Created by charles on 12/14/2023.
//

#include "iostream"
#include "vector"
#include "unordered_map"

class Solution {
public:
    std::vector<int> twoSum(std::vector<int> &nums, int target) {
        std::unordered_map<int, int> map;

        for (int i = 0; i < nums.size(); ++i) {
            int diff = target - nums[i];

            if (map.find(diff) != map.end()) {
                return {i, map[diff]};
            }

            map[nums[i]] = i;
        }

        return {};
    }
};

int main() {
    std::vector<int> nums = {2, 7, 11, 15};
    int target = 9;

    Solution solution;

    std::vector<int> result = solution.twoSum(nums, target);

    if (!result.empty()) {
        std::cout << "add up to " << result[0] << " and " << result[1] << std::endl;
    } else {
        std::cout << "No such pair found." << std::endl;
    }
}

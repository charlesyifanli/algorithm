#include <stdio.h>

struct Pair {
    int first;
    int second;
};

struct Pair twoSum(int nums[], int length, int target) {
    struct Pair result = {-1, -1};
    int hash[100000] = {0}; // Assuming maximum size of nums array is 100000

    for (int i = 0; i < length; i++) {
        int another = target - nums[i];
        if (another >= 0 && hash[another] != 0) {
            result.first = hash[another];
            result.second = i;
            return result;
        }
        hash[nums[i]] = i;
    }
    return result;
}

int main() {
    int nums[] = {2, 7, 11, 15};
    int length = sizeof(nums) / sizeof(nums[0]);
    int target = 9;

    struct Pair result = twoSum(nums, length, target);
    if (result.first != -1 && result.second != -1) {
        printf("Indices of the two numbers that add up to %d: %d and %d\n",
               target, result.first, result.second);
    } else {
        printf("No such pair found.\n");
    }

    return 0;
}

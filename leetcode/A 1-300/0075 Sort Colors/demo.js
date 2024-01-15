/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    nums.sort(function(a, b) {
        return a - b;
    });
};

// Example usage:
var nums = [2, 0, 2, 1, 1, 0];
sortColors(nums);
console.log(nums);

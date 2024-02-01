/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
let twoSum = function (nums, target) {
    let dict_ = {}
    for (let i = 0; i < nums.length; i++) {
        if (target - nums[i] in dict_) {
            return [i, dict_[target - nums[i]]]
        }
        dict_[nums[i]] = i
    }
}
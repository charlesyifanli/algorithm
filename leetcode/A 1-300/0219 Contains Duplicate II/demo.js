/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function (nums, k) {
    let res = false
    let dict_ = {}
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] in dict_ && Math.abs(i - dict_[nums[i]]) <= k) {
            res = true
        }
        dict_[nums[i]] = i
    }
    return res
}
/**
 * @param nums {number[]}
 * @return {number}
 */
var distinctAverages = function (nums) {
    nums.sort((a, b) => a - b)
    let set_ = new Set()
    while (nums.length > 1) {
        let average = (nums.shift() + nums.pop()) / 2
        set_.add(average)
    }
    return set_.size
}
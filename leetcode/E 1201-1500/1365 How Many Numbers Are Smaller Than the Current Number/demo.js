/**
 *
 * @param nums {number[]}
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function (nums) {
    let res = []
    let sortedArray = [...nums].sort((a, b) => a - b)
    for (let i = 0; i < nums.length; i++) {
        res.push(sortedArray.indexOf(nums[i]))
    }
    return res
}

// case
nums = [8, 1, 2, 2, 3]
console.log(smallerNumbersThanCurrent(nums)) //Output: [4, 0, 1, 1, 3]
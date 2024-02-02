/**
 * @param {number[]} nums
 * @param {number} original
 * @return {number}
 */
let findFinalValue = function (nums, original) {
    nums.sort((a, b) => a - b)
    while (nums.includes(original)) original *= 2
    return original
}

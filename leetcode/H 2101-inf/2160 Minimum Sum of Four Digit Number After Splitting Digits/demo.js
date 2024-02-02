/**
 * @param {number} num
 * @return {number}
 */
let minimumSum = function (num) {
    let sortedArray = Array.from(String(num), Number).sort()
    return parseInt(sortedArray[0].toString() + sortedArray[3].toString()) + parseInt(sortedArray[1].toString() + sortedArray[2].toString())
}

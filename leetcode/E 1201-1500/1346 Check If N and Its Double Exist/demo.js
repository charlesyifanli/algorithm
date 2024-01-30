/**
 * @param arr {number[]}
 * @return {boolean}
 */
var checkIfExist = function (arr) {
    let set_ = new Set()
    for (let i = 0; i < arr.length; i++) {
        if (set_.has(arr[i] * 2) || set_.has(arr[i] / 2)) {
            return true
        } else {
            set_.add(arr[i])
        }
    }
    return false

}

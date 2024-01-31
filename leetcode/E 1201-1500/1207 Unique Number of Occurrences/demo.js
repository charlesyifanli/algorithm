/**
 * @param arr {number[]}
 * @return {boolean}
 */2
var uniqueOccurrences = function (arr) {
    var counts = arr.reduce(function (acc, num) {
        acc[num] = (acc[num] || 0) + 1
        return acc
    }, {})
    var values = Object.values(counts)
    return new Set(values).size === values.length
}
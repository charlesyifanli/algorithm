/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function (n) {
    let res = []
    for (let val = 0; val <= n; val++) {
        let binary = val.toString(2)
        let count = 0
        for (let i = 0; i < binary.length; i++) {
            if (binary[i] === '1') {
                count++
            }
        }
        res.push(count)
    }
    return res
}

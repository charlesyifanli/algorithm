/**
 * @param {number} x
 * @return {number}
 */
let reverse = function (x) {
    let temp = parseInt(Math.abs(x).toString().split('').reverse().join(''));
    if (temp > Math.pow(2, 31) - 1) {
        return 0;
    } else {
        if (x < 0) {
            temp = -temp;
        }
        return temp;
    }
}

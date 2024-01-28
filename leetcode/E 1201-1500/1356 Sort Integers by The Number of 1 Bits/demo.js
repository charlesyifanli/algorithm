/**
 * @param {number[]} arr
 * @return {number[]}
 */
var sortByBits = function (arr) {
    arr.sort((a, b) => a - b);
    let dict = {};
    for (let val of arr) {
        let count = val.toString(2).split('0').join('').length;
        if (!(count in dict)) {
            dict[count] = [val];
        } else {
            dict[count].push(val);
        }
    }
    let sortedKeys = Object.keys(dict).sort((a, b) => a - b);
    let res = [];
    for (let key of sortedKeys) {
        res = res.concat(dict[key]);
    }
    return res;
};

function test() {
    // case
    let arr = [0, 1, 2, 3, 4, 5, 6, 7, 8];
    console.assert(JSON.stringify(sortByBits(arr)) === JSON.stringify([0, 1, 2, 4, 8, 3, 5, 6, 7]), "Test case failed!");

    console.log('Succeed');
}

test();
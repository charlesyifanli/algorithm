var arrayRankTransform = function(arr) {
    let sortedArray = Array.from(new Set(arr)).sort((a, b) => a - b);
    let dict = {};
    for (let i = 0; i < sortedArray.length; i++) {
        dict[sortedArray[i]] = i + 1;
    }
    for (let i = 0; i < arr.length; i++) {
        arr[i] = dict[arr[i]];
    }
    return arr;
};

// Test
let arr = [40, 10, 20, 30];
console.log(arrayRankTransform(arr)); // Output: [4, 1, 2, 3]
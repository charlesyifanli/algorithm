var sortArrayByParity = function(nums) {
        const even = [];
        const odd = [];
        for (const val of nums) {
            if (val % 2 === 0) {
                even.push(val);
            } else {
                odd.push(val);
            }
        }
        return even.concat(odd);
};

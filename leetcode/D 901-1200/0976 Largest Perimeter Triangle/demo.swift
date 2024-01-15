class Solution {
    func largestPerimeter(_ nums: [Int]) -> Int {
        var numsCopy = nums.sorted()
        while numsCopy.count >= 3 {
            if isTriangle(Array(numsCopy.suffix(3))) {
                return numsCopy[numsCopy.count - 1] + numsCopy[numsCopy.count - 2] + numsCopy[numsCopy.count - 3]
            } else {
                numsCopy.removeLast()
            }
        }
        return 0
    }

    private func isTriangle(_ tri: [Int]) -> Bool {
        let sortedTri = tri.sorted()
        return sortedTri[0] + sortedTri[1] > sortedTri[2]
    }
}

let solution = Solution()
let nums = [2, 1, 2]
let result = solution.largestPerimeter(nums)
print(result) // 输出结果

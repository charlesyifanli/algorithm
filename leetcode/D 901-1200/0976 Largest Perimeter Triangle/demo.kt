import java.util.Arrays

class Solution {
    fun largestPerimeter(nums: IntArray): Int {
        nums.sort()
        var numsCopy = nums.copyOf()
        while (numsCopy.size >= 3) {
            if (isTriangle(numsCopy.copyOfRange(numsCopy.size - 3, numsCopy.size))) {
                return numsCopy[numsCopy.size - 1] + numsCopy[numsCopy.size - 2] + numsCopy[numsCopy.size - 3]
            } else {
                numsCopy = numsCopy.copyOfRange(0, numsCopy.size - 1)
            }
        }
        return 0
    }

    private fun isTriangle(tri: IntArray): Boolean {
        Arrays.sort(tri)
        return tri[0] + tri[1] > tri[2]
    }
}

fun main() {
    val solution = Solution()
    val nums = intArrayOf(2, 1, 2)
    val result = solution.largestPerimeter(nums)
    println(result) // 输出结果
}

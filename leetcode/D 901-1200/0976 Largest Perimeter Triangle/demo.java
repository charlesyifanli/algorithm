import java.util.Arrays;

class Solution {
    int largestPerimeter(int[] nums) {
        Arrays.sort(nums);
        while (nums.length >= 3) {
            if (isTriangle(Arrays.copyOfRange(nums, nums.length - 3, nums.length))) {
                return nums[nums.length - 1] + nums[nums.length - 2] + nums[nums.length - 3];
            } else {
                nums = Arrays.copyOf(nums, nums.length - 1);
            }
        }
        return 0;
    }

    private boolean isTriangle(int[] tri) {
        Arrays.sort(tri);
        return tri[0] + tri[1] > tri[2];
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {2, 1, 2};
        int result = solution.largestPerimeter(nums);
        System.out.println(result);
    }
}

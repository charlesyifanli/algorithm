using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] Intersection(int[] nums1, int[] nums2) {
        HashSet<int> set1 = new HashSet<int>(nums1);
        HashSet<int> set2 = new HashSet<int>(nums2);
        return set1.Intersect(set2).ToArray();
    }
}

public class Program {
    public static void Main() {
        Solution solution = new Solution();
        int[] nums1 = {1, 2, 2, 1};
        int[] nums2 = {2, 2};
        Console.WriteLine(string.Join(", ", solution.Intersection(nums1, nums2)));

        nums1 = new int[]{4, 9, 5};
        nums2 = new int[]{9, 4, 9, 8, 4};
        Console.WriteLine(string.Join(", ", solution.Intersection(nums1, nums2)));
    }
}

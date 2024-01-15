class Solution {
    function largestPerimeter($nums) {
        sort($nums);
        $numsCopy = $nums;
        while (count($numsCopy) >= 3) {
            if ($this->isTriangle(array_slice($numsCopy, -3))) {
                return $numsCopy[count($numsCopy) - 1] + $numsCopy[count($numsCopy) - 2] + $numsCopy[count($numsCopy) - 3];
            } else {
                array_pop($numsCopy);
            }
        }
        return 0;
    }

    private function isTriangle($tri) {
        sort($tri);
        return $tri[0] + $tri[1] > $tri[2];
    }
}

$solution = new Solution();
$nums = [2, 1, 2];
$result = $solution->largestPerimeter($nums);
echo $result; // 输出结果

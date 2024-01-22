package main

func arraySign(nums []int) int {
    cnt := 0
    for _, s := range nums {
        if (s == 0) {
            return 0
        } else if (s < 0) {
            cnt++
        }
    }
    if (cnt % 2 == 0) {
        return 1
    }
    return -1
}

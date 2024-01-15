package main

import "fmt"

func removeElement(nums []int, val int) int {
	l := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != val {
			nums[l] = nums[i]
			l++
		}
	}
	return l
}

func main() {
	case1 := []int{3, 2, 2, 3}
	val1 := 3
	fmt.Print(removeElement(case1, val1), "--")
	fmt.Println(case1)

	case2 := []int{0, 1, 2, 2, 3, 0, 4, 2}
	val2 := 2
	fmt.Print(removeElement(case2, val2), "--")
	fmt.Println(case2)
}

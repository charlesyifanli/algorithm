package main

import "fmt"

func main() {
	nums := []int{2, 7, 11, 15}
	target := 9

	result := twoSum(nums, target)
	if result != nil {
		fmt.Printf("Indices of the two numbers that add up to %d: %v and %v\n", target, result[0], result[1])
	} else {
		fmt.Println("No such pair found.")
	}
}

func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		diff := target - nums[i]
		if _, ok := m[diff]; ok {
			return []int{i, m[diff]}
		}
		m[nums[i]] = i
	}
	return nil
}

/*
func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		another := target - nums[i]
		if _, ok := m[another]; ok {
			return []int{m[another], i}
		}
		m[nums[i]] = i
	}
	return nil
}
*/

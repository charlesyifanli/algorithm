package main

import (
	"fmt"
)

func maxArea(height []int) int {
	//init
	maxArea := 0
	l, r := 0, len(height)-1

	//
	for l < r {
		length, high := r-l, 0
		if height[l] > height[r] {
			high = height[r] //bottleneck effect or weakest link effect
			r--
		} else {
			high = height[l]
			l++
		}
		if maxArea < high*length {
			maxArea = high * length
		}
	}

	//
	return maxArea
}

func main() {
	// test case
	testCases := [][]int{
		{1, 8, 6, 2, 5, 4, 8, 3, 7}, // expected output: 49
		{4, 3, 2, 1, 4},             // expected output: 16
		{1, 2, 1},                   // expected output: 2
	}

	for i, testCase := range testCases {
		result := maxArea(testCase)
		fmt.Printf("Test case %d: Input %v, Output %d\n", i+1, testCase, result)
	}
}

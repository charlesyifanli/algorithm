package main

//import (
//	"fmt"
//	"sort"
//)
//
//func threeSum(nums []int) [][]int {
//	sort.Ints(nums)
//	result, start, end, index, addNum, length := make([][]int, 0), 0, 0, 0, 0, len(nums)
//	for index = 1; index < length-1; index++ {
//		start, end = 0, length-1
//		if index > 1 && nums[index] == nums[index-1] {
//			start = index - 1
//		}
//		for start < index && end > index {
//			if start > 0 && nums[start] == nums[start-1] {
//				start++
//				continue
//			}
//			if end < length-1 && nums[end] == nums[end+1] {
//				end--
//				continue
//			}
//			addNum = nums[start] + nums[end] + nums[index]
//			if addNum == 0 {
//				result = append(result, []int{nums[start], nums[index], nums[end]})
//				start++
//				end--
//			} else if addNum > 0 {
//				end--
//			} else {
//				start++
//			}
//		}
//	}
//	return result
//}
//
//func main() {
//	arr := []int{-1, 0., 1, 2, -1, -4}
//	arr1 := threeSum(arr)
//	for i := 0; i < len(arr1); i++ {
//		fmt.Print(arr1[i])
//		fmt.Print(" ")
//	}
//}
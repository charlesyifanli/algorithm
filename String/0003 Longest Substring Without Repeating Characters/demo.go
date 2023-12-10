package main

import (
	"fmt"
)

func lengthOfLongestSubstring(s string) int {
	// Initialize left and right pointers, maxLength, and a map to store character indices
	l, r, maxLength := 0, 0, 0
	tempMap := make(map[byte]int, len(s))

	// Start iterating through the string
	for r < len(s) {
		tempLength := 0 // Temporary storage for the length of the current non-repeating substring

		// Check if the current character exists in tempMap and its index is greater than or equal to the left pointer
		if value, ok := tempMap[s[r]]; ok && value >= l {
			l = value + 1 // Move the left pointer to the next position after the repeating character
		}
		tempMap[s[r]] = r      // Update the index of the current character in the map
		tempLength = r - l + 1 // Calculate the length of the current non-repeating substring
		r++                    // Move the right pointer to the next character

		// Update the maximum length of non-repeating substring encountered so far
		if tempLength > maxLength {
			maxLength = tempLength
		}
	}

	return maxLength // Return the maximum length of non-repeating substring
}

func main() {
	testString := "pwwkew" // Change this string for different test cases
	result := lengthOfLongestSubstring(testString)
	fmt.Printf("%d", result)
}

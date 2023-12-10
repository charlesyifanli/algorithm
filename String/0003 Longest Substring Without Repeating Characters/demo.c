#include <stdio.h>
#include <string.h>

int lengthOfLongestSubstring(char *s) {
    // Initialize variables for left and right pointers, maxLength, and a character array to store character indices
    int l = 0, r = 0, maxLength = 0;
    int tempMap[256]; // Assuming ASCII characters, this array stores character indices
    memset(tempMap, -1, sizeof(tempMap)); // Initialize array with -1 (indicating character not encountered yet)

    // Start iterating through the string
    while (s[r] != '\0') {
        int tempLength = 0; // Temporary storage for the length of the current non-repeating substring

        // Check if the current character exists in tempMap and its index is greater than or equal to the left pointer
        if (tempMap[s[r]] != -1 && tempMap[s[r]] >= l) {
            l = tempMap[s[r]] + 1; // Move the left pointer to the next position after the repeating character
        }
        tempMap[s[r]] = r; // Update the index of the current character in the array
        tempLength = r - l + 1; // Calculate the length of the current non-repeating substring
        r++; // Move the right pointer to the next character

        // Update the maximum length of non-repeating substring encountered so far
        if (tempLength > maxLength) {
            maxLength = tempLength;
        }
    }

    return maxLength; // Return the maximum length of non-repeating substring
}

int main() {
    char testString[] = "pwwkew"; // Change this string for different test cases
    int result = lengthOfLongestSubstring(testString);
    printf("%d", result);
    return 0;
}

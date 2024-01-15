class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_length = 0
        temp_map = [-1] * 256  # Assuming ASCII characters, initialize array with -1

        # Start iterating through the string
        for r in range(len(s)):
            temp_length = 0  # Temporary storage for the length of the current non-repeating substring

            if temp_map[ord(s[r])] != -1 and temp_map[ord(s[r])] >= l:
                l = temp_map[ord(s[r])] + 1  # Move the left pointer to the next position after the repeating character
            temp_map[ord(s[r])] = r  # Update the index of the current character in the array
            temp_length = r - l + 1  # Calculate the length of the current non-repeating substring

            # Update the maximum length of non-repeating substring encountered so far
            max_length = max(max_length, temp_length)

        return max_length  # Return the maximum length of non-repeating substring

#include <stdio.h>

int maxArea(int *height, int heightSize) {
    int maxArea = 0;
    int l = 0;
    int r = heightSize - 1;

    //
    while (l < r) {
        int length = r - l;
        int high = 0;
        if (height[l] < height[r]) {
            high = height[l];
            l++;
        } else {
            high = height[r];
            r--;
        }

        //
        if (length * high > maxArea) {
            maxArea = length * high;
        }
    }

    //
    return maxArea;
}

int main() {
    // test case
    int testCases[3][9] = {
        {1, 8, 6, 2, 5, 4, 8, 3, 7}, // expected output: 49
        {4, 3, 2, 1, 4},             // expected output: 16
        {1, 2, 1},                   // expected output: 2
    };

    int i;
    for (i = 0; i < 3; i++) {
        int *testCase = testCases[i];
        int result =
            maxArea(testCase, sizeof(testCases[i]) / sizeof(testCases[i][0]));
        printf("Test case %d: Input [", i + 1);
        int j;
        for (j = 0; j < sizeof(testCases[i]) / sizeof(testCases[i][0]); j++) {
            printf("%d", testCase[j]);
            if (j != sizeof(testCases[i]) / sizeof(testCases[i][0]) - 1) {
                printf(", ");
            }
        }
        printf("], Output %d\n", result);
    }

    return 0;
}

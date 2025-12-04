/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int numsSize, int* returnSize) {
    int n, i, j, m;
    int* ans;

    n = numsSize;
    m = 2 * n;
    ans = (int*)malloc(m * sizeof(int));
    *returnSize = m;

    i = 0;

    while (i < n) {
        ans[i] = nums[i];
       
        i++;
    }
    j=0;
    while (i < m) {
        ans[i] = nums[j];
       
        i++;
        j++;
    }

    return ans;
}


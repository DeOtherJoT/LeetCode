/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* intersection(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    // initialise variables
    int *map = calloc(1000, sizeof(int));

    int minSize = nums1Size;
    if (minSize > nums2Size)
        minSize = nums2Size;

    int *res = calloc(minSize, sizeof(int));
    *returnSize = 0;

    for (int i = 0; i < nums1Size; i++) {
        if (map[nums1[i]] == 0)
            map[nums1[i]] = 1;
    }
    for (int j = 0; j < nums2Size; j++) {
        if (map[nums2[j]] == 1) {
            res[*returnSize] = nums2[j];
            *returnSize += 1;
            map[nums2[j]] = 0;
        }
    }
    free(map);
    return (res);
}
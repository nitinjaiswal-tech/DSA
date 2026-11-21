class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        n = len(nums)
        return nums[n//2] if n%2 else (nums[n//2-1] + nums[n//2])/2
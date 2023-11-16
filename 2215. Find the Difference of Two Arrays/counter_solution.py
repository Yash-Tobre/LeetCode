class Solution:
    def findDifference(self, nums1, nums2):
        # Count the occurrences of elements in nums1 and nums2
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        # Find elements in nums1 that have more occurrences than in nums2 or are not in nums2
        diff1 = [key for key in count1 if key not in count2]
        
        # Find elements in nums2 that have more occurrences than in nums1 or are not in nums1
        diff2 = [key for key in count2 if key not in count1]
        
        # Return the lists of differences between nums1 and nums2
        return [diff1, diff2]

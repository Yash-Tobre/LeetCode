class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer_list = []
        answer_list.append(list(set(nums1)-(set(nums1)&set(nums2))))
        answer_list.append(list(set(nums2)-(set(nums1)&set(nums2))))
        return answer_list
        

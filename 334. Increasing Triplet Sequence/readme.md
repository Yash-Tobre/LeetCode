class Solution:

    def increasingTriplet(self, nums: List[int]) -> bool:
        nums_i = nums_j = float('inf')

        for each in nums:
            if each <= nums_i:
                nums_i = each
            elif each <= nums_j:
                nums_j = each
            else:
                return True
        
        return False

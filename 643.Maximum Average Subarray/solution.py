class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average = current = sum(nums[:k])
        for each in range(k,len(nums)):
            current = current + nums[each] - nums[each-k]
            if current > max_average:
                max_average = current
        
        return max_average / k

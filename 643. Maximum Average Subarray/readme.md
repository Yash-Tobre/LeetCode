class Solution:

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Initial sum of the first 'k' elements
        current_sum = sum(nums[:k])
        max_sum = current_sum
        # Iterate through the array, updating the window sum
        for i in range(k,len(nums)):
            current_sum += nums[i] - nums[i-k]
            if current_sum > max_sum:
                max_sum = current_sum

        # Return the maximum average
        return max_sum/k

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        prefix_sum = 0
        for i in range(len(nums)):
            if prefix_sum == total_sum-prefix_sum-nums[i]:
                return i
            prefix_sum +=nums[i]

        return -1


'''
The idea here is to do it in minimum calculations as possiblle:
Step 1: Define variables for total_sum and prefix_sum where total_sum is the sum of all the elements in nums and prefix_sum will be a sum based on the current index pointer.
Step 2: Iterate through a for loop, over each element of the list.
Step 3: In the for loop check if the current prefix_sum is equal to the total_sum - prefix_sum - current element, which essentially gives us the right hand or the suffix sum.
Step 4: if the condition is not satisfied, we add the current element to the prefix_sum before moving on to the next element, so that prefix_sum now represents the sum of all elements before
the next element.
Step 5: Return -1 if none of the conditions are satisfied.
'''

        

        

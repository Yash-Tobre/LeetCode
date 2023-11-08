class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums)==0:
            return -1
        elif len(nums)==1:
            return 0
        else:
            for i in range(len(nums)):
                if i == 0 and sum(nums[1:])==0:
                    return 0
                elif i != len(nums)-1 and sum(nums[0:i])==sum(nums[i+1:]):
                    return i
                elif i == len(nums)-1 and sum(nums[0:len(nums)-1])==0:
                    return i
        return -1


'''
Algorithm:
Step 1: Check if the length is zero, return -1
Step 2: If the length is 1, return 0
Step 3: otherwise, iterate over a for loop for each element.
Step 4: If it is the first element, compare the right sum to zero, if true return 0
Step 5: If it is NOT the last element, compare the sum by slicing the list at the index position, if both the sum are equal, return the current position.
Step 6: If it is the last element, check if the sum to the left is equal to zero, if it is then return the last index.
Step 7: Return -1 if everything else fails.

Time complexity: O(n2) and Space Complexity O(1)
                    
                     

        

        

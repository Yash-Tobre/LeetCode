#Approach 1: The brute force approach, Time Complexity: O(n^2), Space Complexity: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

#Approach 2: Using Dictionary/Hashmap, Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}

        for i in range(0,len(nums)):
            hashmap[nums[i]]=i
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement]!=i:
                return [i, hashmap[complement]]


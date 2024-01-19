#using hashmap
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashmap = {}
        count = 0
        for each in nums:
            if each in hashmap:
                hashmap[each] += 1
            else:
                hashmap[each] = 1
        for each in nums:
            complement = k - each
            if complement in hashmap and (hashmap[each]>0 and hashmap[complement]>0):
                if each == complement and hashmap[complement] <2:
                    continue
                hashmap[each] -= 1
                hashmap[complement] -=1
                count +=1
        return count

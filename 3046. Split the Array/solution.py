class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter_dict = {}
        for each in nums:
            counter_dict[each] = counter_dict.get(each,0)+1
        for each in counter_dict.values():
            if each>2:
                return False
        return True



        

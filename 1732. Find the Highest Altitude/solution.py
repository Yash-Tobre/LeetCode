class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        max=0
        pointer = 0
        for each in gain:
            pointer += each
            if max < pointer:
                max = pointer
        
        return max

#Approach:
#Step 1: Declare variables for max and pointer
#Step 2: We will add each element to the pointer
#Step 3: If this element is greater than the initial element zero, update max value
#Step 4: return max value.

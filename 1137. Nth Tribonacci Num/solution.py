class Solution:
    def tribonacci(self, n: int) -> int:
        sequence = [0,1,1]
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        else:
            for each in range(3,n+1):
                
                sequence.append(sequence[each-3]+sequence[each-2]+sequence[each-1])
            return sequence[n]
#Time and Space complexity are both O(n)
#Optimized solution may include time and space complexity as O(logn) and O(1) respectively.
            

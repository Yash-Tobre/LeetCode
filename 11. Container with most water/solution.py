#Two pointer method
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height)-1
        for i in range(len(height)):
            dist = abs(right-left)
            high = min(height[left], height[right])
            area = dist*high
            if area > max_area:
                max_area = area
            if height[left] > height[right]:
                right -= 1
            else:
                left +=1
        return max_area
        
        


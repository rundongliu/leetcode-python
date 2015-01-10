class Solution:
    # @return an integer
    def maxArea(self, height):
        if len(height)<=1:
            return 0
        start = 0
        end = len(height)-1
        contain = 0
        while start<end:
            contain = max(contain,min(height[start],height[end])*(end-start))
            if height[start]>height[end]:
                end -= 1
            else:
                start += 1
        return contain
        
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights)-1
        store = 0
        while left < right:
            temp_store = min(heights[left],heights[right])*(right-left) 
            if temp_store > store:
                store = temp_store
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        return store
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
    
        right=len(heights)-1
        max_water=0

        while l<right:
            
            if heights[l]<heights[right]:
                lf=l
                l+=1
            else:
                lf=right
                right-=1
            total_water=(right-l+1)*heights[lf]
            max_water=max(max_water,total_water)
            


            
        return max_water

        
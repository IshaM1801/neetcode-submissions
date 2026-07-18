class Solution:
    def trap(self, height: List[int]) -> int:
        left, right=[0] * len(height), [0] * len(height)
        max_left, max_right, total_water,l = 0,0,0, len(height)
        for i in range (1,l+1):
            max_left=max(max_left,height[i-1])
            max_right=max(max_right,height[(-1)*i])
            right[(-1)*i]=max_right
            left[i-1]=max_left
        for ind,i in enumerate(height):
            lf=min(left[ind],right[ind])
            if i> left[ind]:
                lf=min(i,right[ind])
            if lf>0:
                total_water+=(lf-i)
                print(i,total_water)
        return total_water

        
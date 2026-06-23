class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        o=[]
        for i,n in enumerate(nums):
            if n in h:
                o.append(h[n])
                o.append(i)

            h[target-n]=i
        
        return o


        
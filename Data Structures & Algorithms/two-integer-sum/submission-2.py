class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i,n in enumerate(nums):
            if n in h:
                return[h[n],i]

            h[target-n]=i
        
        


        
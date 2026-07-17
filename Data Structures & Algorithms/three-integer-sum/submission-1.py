class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
 

        result=set()
        for i,l in enumerate(nums):
            # Optimization: skipping the same value for the first element avoids redundant work
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            temp=nums[i+1:] # Only look at elements after i to ensure distinct indices and reduce redundant work
            
            all_ts = self.twoSum(temp,0-l)
            for ts in all_ts:
                ts.append(l)
                result.add(tuple(sorted(ts)))
               

                
            
        return ( [list(t) for t in result])
                
                
    def twoSum(self, numbers: List[int], target: int) -> List[List[int]]:
        res = []
        right = len(numbers)-1
        left=0
        
        while left < right:
            summed=numbers[left] + numbers[right]
            if  summed > target:
                right-=1
            elif summed < target:
                left+=1
            elif summed == target:
                res.append([numbers[left],numbers[right]])
                # Continue searching for more pairs that satisfy target
                left += 1
                right -= 1
            
        return res
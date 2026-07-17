class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        right = len(numbers)-1
        left=0
        while left < right:
            summed=numbers[left] + numbers[right]
            if  summed > target:
                right-=1
            elif summed < target:
                left+=1
            elif summed == target:
                return [left+1,right+1]
            
        return []
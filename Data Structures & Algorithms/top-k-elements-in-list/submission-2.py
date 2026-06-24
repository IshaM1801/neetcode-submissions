class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
   
        kt=[]
        kt=sorted(d, key=d.get, reverse=True)[:k]
        return kt

        
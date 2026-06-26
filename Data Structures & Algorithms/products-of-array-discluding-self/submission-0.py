class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro=1
        pre=[1]
        suf=[1]
        s=1
        ans=[]
        l=len(nums)
        for i in range(l-1):
            pro=pro*nums[i]
            s=s*nums[-i-1]
            pre.append(pro)
            suf.append(s)
        print (pre,suf)
        for i in range(l):
            ans.append(suf[-i-1]*pre[i])
        return ans

        
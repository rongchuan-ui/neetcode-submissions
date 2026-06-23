class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        N=1
        lst=[]
        for i in range(0,len(nums)-1):
            if nums[i]==1 and nums[i]==nums[i+1]:
                N+=1
            elif nums[i]==1 and nums[i]!=nums[i+1]:
                lst.append(N)
            else:
                N=1
        if nums[-1] == 1:
            lst.append(N)
        if lst:
            return max(lst)
        else:
            return 0
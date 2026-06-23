class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # n=0
        # for i in range(len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         n+=1
        #         break
        #     else:
        #         continue
        # if n==1:      
        #     return True 
        # else:
        #     return False
        
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False
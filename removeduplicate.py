class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:  
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:  
                i += 1
                nums[i] = nums[j]   
        
        return i + 1  


nums = [1, 1, 2, 2, 3]
p = Solution()
result = p.removeDuplicates(nums)
print(result)  
print(nums[:result])  

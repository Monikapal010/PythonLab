class Solution(object):
    def searchInsert(self, nums, target):
        i = 0
        
        while i < len(nums) and target >= nums[i]:
            if nums[i] == target:
                return i
            i += 1
        return i
        
solution = Solution()
print(solution.searchInsert([1, 3, 5, 6], 5))  # Output: 2
print(solution.searchInsert([1, 3, 5, 6], 2))  # Output: 1
print(solution.searchInsert([1, 3, 5, 6], 7))  # Output: 4
print(solution.searchInsert([1, 3, 5, 6], 0))  # Output: 0

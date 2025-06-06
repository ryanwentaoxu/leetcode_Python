class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        largeIndex = len(nums) - 2
        while (largeIndex >= 0 and nums[largeIndex] >= nums[largeIndex + 1]):
            largeIndex -= 1
        if (largeIndex >= 0):
            smallIndex = len(nums) - 1
            while (nums[smallIndex] <= nums[largeIndex]):
                smallIndex -= 1
            tmp = nums[smallIndex]
            nums[smallIndex] = nums[largeIndex]
            nums[largeIndex] = tmp
        
        self.reverse(nums, largeIndex + 1)
    def reverse(self, nums, index):
        left = index
        right = len(nums) - 1
        while left < right:
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            left += 1
            right -= 1
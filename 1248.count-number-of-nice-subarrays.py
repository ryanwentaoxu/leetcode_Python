class Solution:
    def helper(self, nums, k):
        ans = 0
        count = 0
        left = 0
        right = 0
        while (right < len(nums)):
            if (nums[right] % 2 == 1):
                count += 1
            while count > k:
                if (nums[left] % 2 == 1):
                    count -= 1
                left += 1
            ans += right - left + 1
            right += 1
        return ans


    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.helper(nums, k) - self.helper(nums, k - 1)
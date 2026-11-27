class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Agar mid bada hai last element se, minimum right side hoga
            if nums[mid] > nums[right]:
                left = mid + 1

            # Warna minimum left side mein ho sakta hai, mid bhi include karo
            else:
                right = mid

        # Dono pointers same jagah aa gaye, yahi minimum hai
        return nums[left]
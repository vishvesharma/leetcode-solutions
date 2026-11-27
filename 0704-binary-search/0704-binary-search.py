
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # Dono side se range set kar li
        while left <= right:
            mid = (left + right) // 2

            # Agar middle wala hi target hai toh index return
            if nums[mid] == target:
                return mid

            # Target bada hai toh left side check karne ka fayda nahi
            elif nums[mid] < target:
                left = mid + 1

            # Target chhota hai toh right side hata do
            else:
                right = mid - 1

        # Puri range check ho gayi, target nahi mila
        return -1

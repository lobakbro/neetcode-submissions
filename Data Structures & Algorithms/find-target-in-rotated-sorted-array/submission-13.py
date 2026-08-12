class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1
        while l <= h:
            mid = (l+h)//2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l]> target or target>nums[mid]:
                    l= mid+1
                else:
                    h = mid-1
            else:
                if nums[mid]> target or target> nums[h]:
                    h= mid -1
                else:
                    l = mid+1
        return -1
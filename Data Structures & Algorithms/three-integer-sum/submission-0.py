class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort_nums = sorted(nums)
        output = []

        for i in range(len(sort_nums)-1):
            lo = i+1
            hi = len(sort_nums)-1
            diff = 0-sort_nums[i]
            while lo< hi:
                s = sort_nums[lo] + sort_nums[hi]
                if s == diff:
                    if [sort_nums[i],sort_nums[lo],sort_nums[hi]] not in output:
                        output.append([sort_nums[i],sort_nums[lo],sort_nums[hi]])
                    lo +=1
                if s < diff:
                    lo +=1
                if s > diff:
                    hi-=1
        return output
from collections import Counter
class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for item, freq in count.items():
            buckets[freq].append(item)

        result = []
        for i in range(len(buckets) - 1,0,-1):
            for item in buckets[i]:
                result.append(item)
                if len(result) ==k:
                    return result
        

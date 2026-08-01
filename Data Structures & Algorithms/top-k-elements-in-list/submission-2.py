from collections import Counter
class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # n : freq
        buckets = {} # freq : n
        top_k =[]
        for n in nums:
            count[n] = count.get(n,0)+1
        for n, freq  in count.items():
            bucket = buckets.get(freq, [])
            bucket.append(n)
            buckets[freq] = bucket
        for n in range(len(nums), 0, -1 ):
            if buckets.get(n, None):
                for x in buckets[n]:
                    k -=1
                    top_k.append(x)
                    if k ==0:
                        return top_k
            
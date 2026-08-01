import heapq
class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # n : freq
        buckets = [] # freq : n
        top_k =[]
        for n in nums:
            count[n] = count.get(n,0)+1
        for n, freq  in count.items():
            buckets.append((freq,n))
        
        return [y for (x,y) in heapq.nlargest(k,buckets)]
            
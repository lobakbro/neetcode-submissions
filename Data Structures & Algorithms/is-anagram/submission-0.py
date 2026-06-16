class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count={}
        if len(s) != len(t):
            return False
        for u, v in zip(s,t):
            s_count[u] = s_count.get(u,0) + 1
            t_count[v] = t_count.get(v,0) + 1
        if s_count != t_count:
            return False
        return True

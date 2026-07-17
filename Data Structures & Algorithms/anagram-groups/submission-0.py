from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        compare = {}

        for n in strs:
            if not tuple(sorted(n)) in compare.keys():
                compare[tuple(sorted(n))] = [n]
                continue
            compare[tuple(sorted(n))].append(n)
        for key in compare.keys():
            output.append(compare[key])
        return output


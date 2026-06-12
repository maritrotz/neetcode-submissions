class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list) #mapping character count of each str to the list of Anagrams
        for s in strs:
            count = [0]*26 #counts characters a - z...
            for c in s:
                count[ord(c) - ord("a")] += 1
            results[tuple(count)].append(s)

        return results.values()
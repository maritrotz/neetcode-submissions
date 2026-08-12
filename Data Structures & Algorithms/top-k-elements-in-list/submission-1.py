class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counts = {}
        freqarray = [[] * i for i in range(len(nums)+1)]

        for n in nums:
            counts[n] = 1 + counts.get(n,0)

        for num,cnt in counts.items():
            freqarray[cnt].append(num)

        for i in range(len(freqarray) - 1,0,-1):
            for n in freqarray[i]:
                res.append(n)
                if len(res) == k:
                    return res
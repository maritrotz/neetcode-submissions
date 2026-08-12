class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counts = {}
        freqArray = [[] for i in range(len(nums)+1)]

        for n in nums:
            counts[n] = 1 + counts.get(n,0)

        for num,cnt in counts.items():
            freqArray[cnt].append(num)
        

        for i in range(len(freqArray) - 1, 0 , -1):
            for num in freqArray[i]:
                res.append(num)
                if len(res) == k:
                    return res

        
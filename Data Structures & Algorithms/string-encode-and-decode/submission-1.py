class Solution:

    def encode(self, strs: List[str]) -> str:
        self.string = ''
        self.delimeter = '#'
        for s in strs:
            self.string+=str(len(s))+self.delimeter+s
        return self.string



    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j=i
            while s[j] != self.delimeter:
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i + length

            res.append(s[i:j])
            i=j
            
                
        return res




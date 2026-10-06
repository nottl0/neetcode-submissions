class Solution:

    def encode(self, strs: List[str]) -> str:
        self.lens = []
        alls = ""
        for s in strs:
            alls += s
            self.lens.append(len(s))
        return alls
    def decode(self, s: str) -> List[str]:
        words = []
        t = 0
        for l in self.lens:
            words.append(s[t:t+l])
            print(s[t:t+l])
            t += l
        return words
            
            
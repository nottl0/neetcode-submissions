class Solution:
    def countBits(self, n: int) -> List[int]:
        #### Every time we pass a power of 2 # of bits is increm-d 
        #### and ones start again from the right (minus the leftmost bit)

        # 0       -> [0]
        # 1       -> [1]
        # 2, 3    -> [1, 2]
        # 4, 5, 6, 7 -> [1, 2, 2, 3]
        # 8, ...  -> [1, 2, 2, 3, 2, 3, 3, 4]
        counts = [0]
        i = 1
        bits = 1 

        while i <= n:
            for j in range(min(bits, n - i + 1)):
                counts.append(counts[j] + 1)
                i += 1

            bits *= 2

        return counts

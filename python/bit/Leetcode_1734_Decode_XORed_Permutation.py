




class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        x, n = 0, len(encoded)+1
        for i in range(1,n+1):
            x = x ^ i
        # perm[0] = x XOR encoded[1] XOR encoded[3] XOR encoded[5]
        for i in range(1, len(encoded), 2):
            x = x ^ encoded[i]
        res = [0] * n
        res[0] = x
        for i in range(len(encoded)):
            res[i+1] = res[i] ^ encoded[i]
        return res
        
        

'''
710. Random Pick with Blacklist

https://leetcode.com/problems/random-pick-with-blacklist/solution/



'''

# virtual whitelist (my version)
class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        #[0,....N-1]; blacklist(2)
        # hash table: replace blacklist element before k with valid element
        # --O-|0-
        # random with first | elements, if element in 0 then replace with after | element
        blacklist.sort()
        self.pick_range = N - len(blacklist)
        self.hash = {}
        i, j, k = 0, len(blacklist)-1, N-1
        while i <= j:
            while blacklist[j] == k:
                j -= 1
                k -= 1
            if i <= j:
                self.hash[blacklist[i]] = k
                # print(self.hash, k)
                i += 1
                k -= 1
        # print(self.hash)
        

    def pick(self) -> int:
        num = random.randint(0, self.pick_range-1)
        # print(num)
        if num in self.hash:
            return self.hash[num]
        return num
      

# -------------------------------------------------
# O(B)
# virtual whitelist
class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.hash = {}
        blacklist = set(blacklist)
        self.wlen = N - len(blacklist)
        w = [i for i in range(self.wlen, N) if i not in blacklist]
        i = 0
        for x in blacklist:
            if x < self.wlen:
                self.hash[x] = w[i]
                i += 1
        

    def pick(self) -> int:
        num = random.randint(0, self.wlen-1)
        if num in self.hash:
            return self.hash[num]
        return num
      
# test_keys = ["Rash", "Kil", "Varsha"]
# test_values = [1, 4, 5]
  
# # Printing original keys-value lists
# print ("Original key list is : " + str(test_keys))
# print ("Original value list is : " + str(test_values))
  
# # using zip() to tuple list [('rash', 1), ...]
# # to convert lists to dictionary
# res = dict(zip(test_keys, test_values))

      
# -----------------------------------
# O(BlogB); B is len of blacklist
# binary search: convert to find k-th missing element
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start, end = 0,len(arr)-1
        while start + 1 < end:
            mid = (start+end) // 2
            missing = arr[mid] - (mid+1)
            if missing < k:
                start = mid
            else:
                end = mid
        # print(start, end)
        missing = arr[end] - (end+1)
        # print(missing)
        if missing < k:
            return arr[end] + k-missing
        missing = arr[start] - (start+1)
        # print(missing)
        if missing < k:
            return arr[start] + k-missing
        return k

      
# ------------------------------
# white list: O(N)
# class Solution {
# public:

#     vector<int> w;

#     Solution(int n, vector<int> blacklist) {
#         unordered_set<int> W;
#         for (int i = 0; i < n; i++) W.insert(i);
#         for (int x : blacklist) W.erase(x);
#         for (auto it = W.begin(); it != W.end(); it++) w.push_back(*it);
#     }

#     int pick() {
#         return w[rand() % w.size()];
#     }
# };


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()

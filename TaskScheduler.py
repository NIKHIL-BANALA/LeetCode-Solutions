class Solution:
    def leastInterval(self, arr: List[str], n: int) -> int:
        d = {x:0 for x in arr}
        for i in arr:
            d[i]+=1
        max_freq = max(d.values())
        max_freq_count = len([x for x in d if d[x] == max_freq])
        ans = (max_freq - 1)*(n+1)+max_freq_count
        return max(ans,len(arr))

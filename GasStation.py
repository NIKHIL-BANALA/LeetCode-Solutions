class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        available = 0
        ans = 0
        for i in range(len(gas)):
            req = gas[i]-cost[i]
            available+=req
            if available<0:
                available = 0
                ans = i+1
        return ans
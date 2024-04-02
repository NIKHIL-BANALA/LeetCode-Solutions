class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = []
        rightmax = []
        n = len(height)
        lm = height[0]
        for i in range(n):
            leftmax.append(max(height[i],lm))
            lm = max(height[i],lm)
        rm = height[-1]
        for j in range(n-1,-1,-1):
            rightmax.append(max(height[j],rm))
            rm = max(height[j],rm)
        rightmax = rightmax[::-1]
        ans = 0
        for k in range(n):
            curr = min(leftmax[k],rightmax[k])-height[k]
            ans+=curr
        return ans

        
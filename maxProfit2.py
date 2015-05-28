class Solution:
    # @param {integer[]} prices
    # @return {integer}
    # oN
    # 在每个拐角处改变值
    # 直接 if (prices[i]>=prices[i-1]) profit+=prices[i]-prices[i-1]; 一重循环即可！
    # scarlett Chen
    # 5/28/2015 Thu 11:04 AM
    # 122Best Time to Buy and Sell Stock II
    def maxProfit(self, prices):
        n = len(prices)
        maxV=0
        for idx, ele in enumerate(prices):
            if ((idx>=1 and ele <= prices[idx-1]) or (idx==0)) and idx<n-1 and ele < prices[idx+1]:
                maxV -=ele
            if ((idx <n-1 and ele >= prices[idx+1])or idx==n-1) and idx>=1 and ele > prices[idx-1] :
                maxV +=ele
        return maxV
            
                
        

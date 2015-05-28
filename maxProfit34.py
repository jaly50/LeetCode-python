    # @param {integer[]} prices
    # @return {integer}
    # O(n) O(1)的方法可以解决，永远维护 buy1 sell1 buy2 sell2 (逆序维护)的最大值就好了
    # dp可以发展成k次交易
    # SCARLETT chen
    # 5/28/2015 Thu 12:11 pm
    # 123 Best Time to Buy and Sell Stock III
def maxProfit(prices):
    	k =2
    	n = len(prices)
    	if n<2:
    		return 0
    	profit = [[0 for i in range(n)] for j in range(k)]
    	for i in range(k):
    		afterbuy = -prices[0]
    		for day in range(1,n):
   				profit[i][day] = max(prices[day]+afterbuy,profit[i][day-1])
   				if i>0:
   					afterbuy = max(afterbuy, profit[i-1][day]-prices[day])
   				else:
   					afterbuy = max(afterbuy, -prices[day])
    				#print afterbuy
    	#print profit
    	return profit[k-1][n-1]
if __name__ == '__main__':
	maxProfit([2,1,2,0,1])

        

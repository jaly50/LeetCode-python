
    # @param {integer[]} prices
    # @return {integer}
    # Jiali Chen
    # 5/28/2015 Thu 14:42 am
    # 121   Best Time to Buy and Sell Stock
    # 维护一个最小值，最大值是减去到当前为止最小值

def maxProfit(prices):
        n = len(prices)
        if n<2:
            return 0
        minV = None
        maxV = 0
        for ele in prices:
            if minV==None:
                minV = ele
            else:
                minV = min(minV,ele)
            maxV=max(maxV, ele-minV)
        # print maxV
        return maxV
if __name__ == '__main__':
    maxProfit([1,8])

class Solution:
    # @param {string} digits
    # @return {string[]}
    # 还是迭代法
    # 初始化情况要注意
    # Scarlett Chen
    # 5/28/2015 Thu 1:58 am
    # 17	Letter Combinations of a Phone Number
    def letterCombinations(digits):
        phone =["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        n= len(digits)
        ans=[]
        for i in range(n):
        	cur = []
        	for j in phone[int(digits[i])]:
        		# intialize situation
        		if len(ans)==0:
        			cur.append(j)
        		for x in ans:
        			cur.append(x+j)
        	ans = cur
        #print ans
        return ans
    if __name__ == '__main__':
    	letterCombinations("22")

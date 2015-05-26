# @param {string} s
# @return {integer}
# 原来的方法是 存pair[][]再s
# 节省space的方法，以i为中心，直接判断s[i][j]是否是pair,直接计算 不再存
# scarlett chen
# 5/26/2015 Tue 11:12 am
# 132	Palindrome Partitioning II
def minCut(s):
    	n = len(s)
        if n<=1:
            return 0
    	# record min cuts
    	result = [n for i in range(n)]
    	for i in range(n):
    		# cannot be n/2, since 1/2=0, but actually wen can set j=1, when i=1
    		for j in range(n):
    			# match from s[i]=s[i]
    			# 最妙的地方！以i为center,j为半径，一旦不匹配，就退出循环 to avoid redundency
    			if i-j <0 or i+j>=n or s[i-j]!=s[i+j]:
    				break
    			if i-j==0:
    				result[i+j]=0
    			else:
    				result[i+j]= min(result[i+j],result[i-j-1]+1)
    			print i+j, result[i+j]
    		for j in range(1,n):
    			# match from s[i-1]==s[i]
    			if i-j <0 or i+j-1>=n or s[i-j]!=s[i+j-1]:
    				break
    			if i-j==0:
    				result[i+j-1]=0
    			else:
    				result[i+j-1]=min(result[i+j-1],result[i-j-1]+1)
    			print i+j-1, result[i+j-1]
    	return result[n-1]

if __name__ == '__main__':
    minCut("efe") 



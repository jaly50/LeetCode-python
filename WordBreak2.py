# https://leetcode.com/problems/word-break-ii/
# Word Break 2
# Scarlett Chen
# 6/3/2015
# 好久没有自己debug那么久的代码了，这个故事告诉我。以后还是看vote抄一抄就好吧＝ ＝
# 我的方法还是挺好的。最开始在result里直接存 到现在为止的string有哪些，这样会memory exceed
# 然后从n downto 0, result[i]存下一次词的位置。再backtracking. 懒得用dfs，就用了数组迭代..
# 遇到了数字转字符再转数字的问题 怒而用str(unichr()) 和 ord()
def wordBreakMemoryExceed(s, wordDict):
        result = [[] for i in range(len(s))]
        for i in range(len(s)):
            if s[0:i+1] in wordDict:
                result[i].append(s[0:i+1])
            for j in range(1,i+1):
                if s[j:i+1] in wordDict and result[j-1]:
                    for st in result[j-1]:
                        result[i].append(st+" "+s[j:i+1])
        #print result[-1]
        return result[-1]

def wordBreak(s, wordDict):
        result = [[] for i in range(len(s))]
        n = len(s)
        # print n
        for i in range(n-1,-1,-1):
            if s[i:n] in wordDict:
                result[i].append(n)
            for j in range(i,n-1):
                if s[i:j+1] in wordDict and result[j+1]:
                    result[i].append(j+1)
        # print result[0]

        i=0
        stg = [""+s[0:res]+str(unichr(res)) for res in result[0]]
        still = True
        while still:
            cur=[]
            
            still = False
            for prev in stg:
                #print "i: ",i," prev:", prev
                pos=ord(prev[-1])
                if pos==n:
                    cur.append(prev)
                else:
                    still = True
                    for nexpos in result[pos]:
                        cur.append(prev[:-1]+" "+s[pos:nexpos]+str(unichr(nexpos)))
            stg = cur
            #print "i: ", i," ",cur
        for idx in range(len(stg)):
            stg[idx] = stg[idx][:-1]
        #print stg
        return stg


if __name__ == '__main__':
    wordBreak("catsanddog",["cat","cats","and","sand","dog"])

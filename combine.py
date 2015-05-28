# nice recursive method: https://leetcode.com/discuss/36535/fast-%26-simple-python-code-recursive
# two situation, n used in k, n not used in k. so x= combine(n-1,k-1)+[k] + combine(n-1,k)
# 77    Combinations
# Scarlett Chen
# 5/27/2015 Wed 10:55 pm
def combine(n, k):
        cur = result = [[]]
        if k>n:
            return result
        for i in range(1,k+1):
            cur=[]
            # print len(cur)
            for part in result:
                if part:
                    begin = part[-1]+1
                else:
                    begin = 1
                    print part
                for j in range(begin, n+1):
                    newPart = part+[j]
                    #print j,newPart
                    cur.append(newPart)
            result = cur
        #print result
        return result
if __name__ == '__main__':
    combine(2,2)

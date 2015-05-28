# @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    # iteractive
    # 一次过
    # 秘诀是遍历的时候，在尾巴存入当前总和
    # 迭代
    # Scarlett Chen
    # 5/28/2015 Thu 1:40 AM
    # 216 Combination Sum III 
def combinationSum3(self, k, n):
        # initialize value
        ans=[[0]]
        for i in range(k):
            cur=[]
            for x in ans:
                total = x.pop()
                start = x[-1] if x else 0
                for j in range(start+1, 10):
                    if total + (k-i)*j >n:
                        break
                    if i==k-1 and total+j==n:
                        cur.append(x+[j])
                    if i<k-1:
                        cur.append(x+[j,total+j])
                        
            ans=cur
        return ans

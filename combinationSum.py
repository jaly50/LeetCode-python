#Scarlett Chen
# 5/28/2015 Thu 1:09 AM
#39 Combination Sum
# recursive; not search
def combinationSum(candidates, target):
        #print candidates, target
        if target < candidates[0]:
            return []
        ans =[]
        for i in range(len(candidates)):
            if target == candidates[i]:
                ans.append([candidates[i]])
                break
            elif target >candidates[i]:
                    #print i,candidates[i], target
                    for com in self.combinationSum(candidates[i:], target-candidates[i]):
                        ans.append([candidates[i]] + com)
        #print ans
        return ans
if __name__ == '__main__':
    combinationSum([1,2,3],3)
        

   # 40 Combination Sum II
   # Scarlett Chen
   # 5/28/2015 Thu 1:19 AM
   # similar to combination 1; 
   # be careful search from next index, and mark the same value wouldn't be set in the same position
   def combinationSum2(self, candidates, target):
        ans =[]
        candidates.sort()
        for i,ele in enumerate(candidates):
            if i>0 and candidates[i-1]==candidates[i]:
                continue
            if target == candidates[i]:
                ans.append([candidates[i]])
                break
            elif target >candidates[i]:
                    # print i,candidates[i], target
                    for com in self.combinationSum2(candidates[i+1:], target-candidates[i]):
                        ans.append([candidates[i]] + com)
            else:
                break
        #print ans
        return ans
        

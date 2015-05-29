import string
import collections
import string
class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    # Scarlett Chen
    # 5/29/2015 Fri 7:32
    # 一次过，也是不容易
    # 双向队列，用集合维护是否出现过
    # 127Word Ladder
    def ladderLength(self, beginWord, endWord, wordDict):
        startSet = {beginWord}
        endSet = {endWord}
        if beginWord == endWord:
            return 1
        # All words contain only lowercase alphabetic characters.
        chars = string.ascii_lowercase
        queue1 = collections.deque([beginWord])
        queue2 = collections.deque([endWord])
        len1,len2=1,1
        while queue1 and queue2:
            for i in range(len(queue1)):
                left = queue1.popleft()
                for idx in range(len(left)):
                    for c in chars:
                        newWord =left[:idx]+c+left[idx+1:]
                        if newWord in endSet:
                            return len1+len2
                        if newWord in wordDict and newWord not in startSet:
                            startSet.add(newWord)
                            queue1.append(newWord)
            len1+=1
            
            for i in range(len(queue2)):
                left = queue2.popleft()
                for idx in range(len(left)):
                    for c in chars:
                        newWord =left[:idx]+c+left[idx+1:]
                        if newWord in startSet:
                            return len1+len2
                        if newWord in wordDict and newWord not in endSet:
                            endSet.add(newWord)
                            queue2.append(newWord)
            len1+=1
        return 0
                    
                
if __name__ == '__main__':
    print ladderLength("abe", "bcd", ["abc","acd","bce","abd"])

                

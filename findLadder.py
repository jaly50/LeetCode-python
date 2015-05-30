import string
import collections
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    # bfs + 更新hashmap <String, Set>每多走一步的时候； 更新完一层再加入这些map
    # Scarlett Chen
    # 5/29/2015 fri 8:35
    #  126  Word Ladder II
    def findLadders(self, start, end, dict):
        dict.add(end)
        parents = collections.defaultdict(set)
        char = string.ascii_lowercase
        level={start}
        while level and end not in parents:
            nextlevel = collections.defaultdict(set)
            for node in level:
                for idx in range(len(node)):
                    for c in char:
                        w = node[:idx]+c+node[idx+1:]
                        if w in dict and w not in parents:
                            nextlevel[w].add(node)
            level = nextlevel
            parents.update(nextlevel)
        res=[[end]]
        while res and res[0][0]!=start:
            res=[[p]+r for r in res for p in parents[r[0]]]
        return res
                            
                    
        

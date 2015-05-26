class Solution:
    # @param s, a string
    # @return a list of lists of string
    # leetcode 131  Palindrome Partitioning
    # Scarlett Chen
    # 5/26/2015 Tue 1:02 AM
    # using pair to get palindrome
    # using result as dp to get all partitions
    def partition(self, s):
        n = len(s)
        pair = [[False for i in range(n)] for j in range(n)]
        result =[[] for i in range(n)]
        for i in range(n):
            pair[i][i] = True
            for j in range(i):
                if s[j]==s[i]:
                    if j==i-1:
                        pair[j][i] = True
                    else:
                        pair[j][i] = pair[j+1][i-1]
            if pair[0][i]:
                result[i].append([s[0:i+1]])
            
            for j in range(i):
                if pair[j+1][i]:
                    for prev in result[j]:
                        # when no value, it becomes None?
                        if prev:
                            # list add an element to another list!!! Be watch!!!!
                            # can not use append, append will add in the list itself
                            result[i].append(prev+[s[j+1:i+1]])
        return result[n-1]


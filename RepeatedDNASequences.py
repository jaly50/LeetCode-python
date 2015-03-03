#Repeated DNA Sequences
#2015.03.03
class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        sequence = collections.defaultdict(int)
        for x in range(len(s)-9):
            sub=s[x:x+10]
            sequence[sub]+=1
        return [key for key, value in sequence.iteritems() if value>1]
        
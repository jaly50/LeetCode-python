class Solution:
    # @param A, a list of integers
    # @return an integer
    # 左边一道墙，右边一道墙！我们走矮的〜往中间走！遇到更高的就更新墙的值...然后看看哪道墙矮，从哪边往中间走！
    def trap(self, A):
        a=0
        b=len(A)-1
        leftmost=0
        rightmost=0
        ans=0
        while a<b:
            leftmost=max(leftmost,A[a])
            rightmost=max(rightmost,A[b])
            if leftmost<rightmost:
                ans+=leftmost-A[a]
                a+=1
            else:
                ans+=rightmost-A[b]
                b-=1
        return ans
        

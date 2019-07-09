class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        '''dp:using dp[i][j] to remember the max length of subarr end with letter A[i] if
            A[i] == B[j],of course dp[i][j] = 0 if A[i]!=B[j] because subarr is not exist
           complexity:time O(n*m) , space: O(n*m)
        '''
        dp = [[0]*(len(B)+1) for i in range(len(A)+1)]
        for i in range(1,len(A)+1):
            for j in range(1,len(B)+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
        return max([max(dp[i]) for i in range(len(dp))])
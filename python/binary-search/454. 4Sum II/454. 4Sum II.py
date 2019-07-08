import collections
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        #TLE 22/48 pass,O(n^2) is not received
        # sumAB = []
        # sumCD = []
        # count = 0
        # for i in A:
        #     for j in B:
        #         sumAB.append(i+j)
        # sumAB.sort()
        # for i in C:
        #     for j in D:
        #         sumCD.append(i+j)
        # sumCD.sort()
        # havepairs = []
        # for ab in sumAB:
        #     if -1*ab in sumCD:
        #         havepairs.append(-1*ab)
        # for i in havepairs:
        #     #only one
        #     idxi = sumCD.index(i)
        #     idxrev = sumCD[::-1].index(i)
        #     if idxi == (len(sumCD) -  idxrev -1):
        #         count += 1
        #     else:
        #         #count += (len(sumCD)-sumCD[::-1].index(-1*ab)-sumCD.index(-1*ab))
        #         count += (len(sumCD)-idxrev - idxi )
        # return count

        #2 using couter to record the sum of ab and cd and the numbers
        #time:O(n^2) in calculating sum,space:O(
        sumAB = []
        sumCD = []
        count = 0
        for i in A:
            for j in B:
                sumAB.append(i+j)
        for i in C:
            for j in D:
                sumCD.append(i+j)
        sumAB_count = collections.Counter(sumAB)
        sumCD_count = collections.Counter(sumCD)
        for k , v in sumAB_count.items():
            if sumCD_count.get(-k,0)!=0:
                count += (v*sumCD_count[-k])
        return count

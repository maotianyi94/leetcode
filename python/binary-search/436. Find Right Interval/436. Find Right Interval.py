class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # brute force O(n^2) TLE 11/17
        # rightidx = [-1]*len(intervals)
        # for i in range(len(intervals)):
        #     min_dis = float('inf')
        #     for j in range(len(intervals)):
        #         if i!=j:
        #             dis  = intervals[j][0] - intervals[i][1]
        #             if  dis >= 0 and dis < min_dis:
        #                 min_dis = dis
        #                 rightidx[i] = j
        # return rightidx

        '''binary search:
          complexity:  time:O(nlogn) space:O(n)
          idea:using binary search to find the interval which end point is >= intervals[i]'s start point
        '''
        if not intervals: return []
        if len(intervals) == 1: return [-1]
        start = []
        end = []
        rightIdx = [-1] * len(intervals)
        for i in range(len(intervals)):
            start.append([intervals[i][0], i])
            end.append([intervals[i][1], i])
        start.sort(key=lambda x: x[0])
        end.sort(key=lambda x: x[0])
        for i in range(len(end)):
            bs_start = 0
            bs_end = len(start) - 1
            while bs_start <= bs_end:
                mid = (bs_start + bs_end) // 2
                if start[mid][0] == end[i][0]:
                    rightIdx[end[i][1]] = start[mid][1]
                    break
                elif start[mid][0] > end[i][0]:
                    # update but may not the minimun value so still go to find
                    rightIdx[end[i][1]] = start[mid][1]
                    bs_end = mid - 1
                else:
                    bs_start = mid + 1
        return rightIdx



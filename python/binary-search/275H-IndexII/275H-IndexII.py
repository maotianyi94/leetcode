class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:return 0
        if len(citations)==1:return min(1,citations[0])
        start = 0
        end = len(citations)-1
        h_max = 0
        while start <= end:
            mid = (start + end)//2
            papers_nums = len(citations)-mid
            if citations[mid] == papers_nums:
                #no need to search down because papers_nums increase but citations[] decrease
                h_max = papers_nums
                break
            elif citations[mid] >papers_nums:
                h_max = max(h_max,papers_nums)
                end = mid - 1
            else:
                #don't satisfy the requirement ,so it's no need to update h_max
                start = mid + 1
        return h_max
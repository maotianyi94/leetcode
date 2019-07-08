class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        house_r = []
        houses.sort()
        heaters.sort()
        if len(heaters) == 1:
            return max(abs(houses[0]-heaters[0]),abs(houses[-1]-heaters[0]))
        #TLE O(n*m) 20/30pass
        # for i in range(len(houses)):
        #     rmax = float('inf')
        #     for j in range(len(heaters)):
        #         rmax = min(rmax,abs(heaters[j]-houses[i]))
        #     house_r.append(rmax)
        # return max(house_r)

        #binary search the nearest position of heaters to the house[i]
        for i in range(len(houses)):
            rmax = float('inf')
            start = 0
            end = len(heaters)
            if heaters[0] >= houses[i]:rmax = heaters[0] - houses[i]
            elif heaters[-1] <= houses[i]:rmax = houses[i] - heaters[-1]
            else:
                while start <= end:
                    mid = (start + end) // 2
                    if heaters[mid] == houses[i]:
                        rmax = 0
                        break
                    elif heaters[mid] < houses[i]:
                        rmax = min(rmax,houses[i] - heaters[mid])
                        start = mid + 1
                    else:
                        rmax = min(rmax,heaters[mid] - houses[i])
                        end = mid - 1
            house_r.append(rmax)
        return max(house_r)
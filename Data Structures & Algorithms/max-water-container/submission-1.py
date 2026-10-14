class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def get_vol(data, left, right):
            return min(data[left],data[right]) * (right - left)

        data = heights
        left = 0
        right = len(data) -1

        max_vol = get_vol(data, left, right)
        while left < right:
            if data[left] <= data[right]:
                left +=1
            elif data[right] <= data[left]:
                right -=1
            max_vol = max(max_vol, get_vol(data,left,right))
        return max_vol



        # data= heights
        # left = 0
        # right = len(data) -1
        # best_left = 0
        # best_right = len(data) -1 
        # vol = get_vol(best_left, best_right)

        # while left<right:
        #     vol_0 = get_vol(data,best_left, right)
        #     vol_1 = get_vol(data,left, best_right)
        #     vol_2 = get_vol(data,left, right)
        #     if vol == max([vol,vol_0,vol_1,vol_2]):
        #         if data[left] > data[right]:
        #             right -= 1
        #         elif data[right] > data[left]:
        #             left += 1
        #         else:
        #             left +=1
        #             right -=1
        #     elif vol_2 == max([vol,vol_0,vol_1,vol_2]):
        #         best_left = left
        #         best_right = right
        #         left+=1
        #         right-=1
        #     elif vol_0 == max([vol,vol_0,vol_1,vol_2]):
        #         best_right = right
        #         right -=1
        #     elif vol_1 == max([vol,vol_0,vol_1,vol_2]):
        #         best_left = left
        #         left +=1
        #     vol = max([vol,vol_0,vol_1,vol_2])
        #     if left > right:
        #         return vol

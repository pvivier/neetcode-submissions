

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        left, right = 0, 1

        water = 0
        bar_volume = 0
        while right < len(height):
            print(right, water)
            if height[right] < height[left]:
                bar_volume += height[right]
                right+=1
            else:
                bar_volume += height[left]
                extra_water = height[left] * (right - left) - bar_volume
                water += extra_water
                bar_volume = 0
                left = right
                right+=1
        print(water, left, right)
        if left == len(height) -1:
            print('here')
            return water

        stop = left -1
        left, right = len(height) -2, len(height) -1
        bar_volume = 0
        while left != stop:
            if height[left] < height[right]:
                bar_volume += height[left]
                left -= 1
            else:
                bar_volume += height[right]
                extra_water = height[right] * (right-left) - bar_volume
                water += extra_water
                bar_volume = 0
                right = left
                left -=1
        return water



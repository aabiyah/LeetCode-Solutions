# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                # Check if the previous and next plots are empty or the current plot is at the edge
                empty_prev = (i == 0 or flowerbed[i - 1] == 0)
                empty_next = (i == length - 1 or flowerbed[i + 1] == 0)

                if empty_prev and empty_next:
                    flowerbed[i] = 1  # Plant a flower here
                    count += 1
                    if count >= n:
                        return True

        return count >= n
# Time O(1)
# Space O(1)
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        temp_dict = {0: 0, 1: 5, 2: 10, 3: 15, 4: 20, 5: 25, 6: 30, 7: 35, 8: 40, 9: 45, 10: 50, 11: 55, 12: 0}
        temp_hour = temp_dict.get(hour)
        temp_value = abs(((minutes - temp_hour) * 6) - (minutes * 0.5))
        if temp_value > 180:
            temp_value = 360 - temp_value
        return temp_value

# temp_obj = Solution()
# print(temp_obj.angleClock(12, 30))
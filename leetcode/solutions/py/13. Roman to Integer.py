# Time complexity: O(n)
# Space complexity: O(1)
# https://leetcode.com/problems/roman-to-integer/
class Solution:
    roman_number = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    roman_number_decrease = {
        'IV': 3,
        'IX': 8,
        'XL': 30,
        'XC': 80,
        'CD': 300,
        'CM': 800
    }
    roman_number_increase = {
        'VI': 1,
        'XI': 1,
        'LX': 10,
        'CX': 10,
        'DC': 100,
        'MC': 100
    }

    def decrease(self, first_letter, second_letter):
        value = self.roman_number_decrease.get(f'{second_letter}{first_letter}', 0)
        if value > 0:
            return value, True
        else:
            return value, False

    def increase(self, first_letter, second_letter):
        value = self.roman_number_increase.get(f'{second_letter}{first_letter}', 0)
        if value > 0:
            return value, True
        else:
            return value, False

    def romanToInt(self, s: str) -> int:
        integer_sum = 0
        prev_char = '0'
        for index, current_char in enumerate(s):
            decrease_value, decrease_continue = self.decrease(current_char, prev_char)
            if decrease_continue:
                integer_sum += decrease_value
                prev_char = '0'
                continue
            increase_value, increase_continue = self.increase(current_char, prev_char)
            if increase_continue:
                integer_sum += increase_value
                prev_char = current_char
                continue
            if current_char == prev_char:
                integer_sum += self.roman_number.get(current_char, 0)
                prev_char = current_char
                continue
            if index + 3 < len(s):
                if current_char == s[index + 2] and s[index + 2] != s[index + 1]:
                    integer_sum += self.roman_number.get(current_char)
                    continue
            prev_char = current_char
            integer_sum += self.roman_number.get(current_char)
        return integer_sum


tempObj = Solution()
print(tempObj.romanToInt('XXXIX'))

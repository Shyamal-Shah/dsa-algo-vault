class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        roman_map = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        decimal = 1
        while num > 0:
            digit = num % 10
            if digit == 4:
                ans = roman_map[1 * decimal] + roman_map[5 * decimal] + ans
            elif digit == 9:
                ans = roman_map[1 * decimal] + roman_map[10 * decimal] + ans
            elif digit == 5:
                ans = roman_map[5 * decimal] + ans
            elif digit < 4:
                ans = (roman_map[1 * decimal] * (digit)) + ans
            elif digit > 5:
                ans = (
                    roman_map[5 * decimal]
                    + (roman_map[1 * decimal] * (digit - 5))
                    + ans
                )
            decimal *= 10
            num //= 10
        return ans


if __name__ == "__main__":
    print(Solution().intToRoman(3749))
    print(Solution().intToRoman(58))
    print(Solution().intToRoman(1994))

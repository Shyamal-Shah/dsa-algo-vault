class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = -1 if x < 0 else 1
        max_int = 2**31
        x *= sign
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        rev *= sign
        if rev < -1 * max_int or rev > max_int - 1:
            rev = 0
        return rev


if __name__ == "__main__":
    print(Solution().reverse(-123))
    print(Solution().reverse(123))
    print(Solution().reverse(-2147483648))
    print(Solution().reverse(1534236469))

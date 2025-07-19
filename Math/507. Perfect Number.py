class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        n = int(num**0.5) + 1
        total = 1
        for i in range(2, n):
            if num % i == 0:
                total += i + num // i
        return total == num


if __name__ == "__main__":
    print(Solution().checkPerfectNumber(36))
    print(Solution().checkPerfectNumber(28))
    print(Solution().checkPerfectNumber(7))

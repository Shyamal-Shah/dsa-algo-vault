class Solution:
    def isPrime(self, n: int) -> bool:
        sqrt = int(n**0.5)
        for i in range(2, sqrt + 1):
            if n % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        primes_c = []
        for i in range(2, n):
            if any(i % p == 0 for p in primes_c):
                continue

            if self.isPrime(i):
                primes_c.append(i)
        return len(primes_c)

    def countPrimesV2(self, n: int) -> int:
        primes = [True] * (n)
        i = 2
        while i * i < n:
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False
            i += 1
        c = 0
        for i in range(2, n):
            if primes[i]:
                c += 1
        return c


if __name__ == "__main__":
    print(Solution().countPrimesV2(1))
    print(Solution().countPrimesV2(10))
    print(Solution().countPrimesV2(35))
    print(Solution().countPrimesV2(5000000))

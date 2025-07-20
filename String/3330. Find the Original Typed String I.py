class Solution:
    def possibleStringCount(self, word: str) -> int:
        total = 1
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                total +=1

        return total
        i, hm = 0, []
        while i < len(word):
            j = i
            hm.append(1)
            i += 1
            while i < len(word) and word[j] == word[i]:
                hm[-1] += 1
                i += 1
        return sum(hm) - len(hm) + 1


if __name__ == "__main__":
    print(Solution().possibleStringCount("abbcccc"))
    print(Solution().possibleStringCount("ere"))
    print(Solution().possibleStringCount("abcd"))
    print(Solution().possibleStringCount("aaaa"))

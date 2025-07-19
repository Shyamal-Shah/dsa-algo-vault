class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        v, c = 0, 0
        for x in word.upper():
            if x in ["@", "#", "$"]:
                return False
            elif x in ["A", "E", "I", "O", "U"]:
                v += 1
            elif x > "A" and x <= "Z":
                c += 1

        if v > 0 and c > 0:
            return True
        return False


if __name__ == "__main__":
    print(Solution().isValid("IS#"))

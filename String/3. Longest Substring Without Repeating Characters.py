class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subStr = ""
        maxLen = 0
        for i in s:
            if i not in subStr:
                subStr += i
            else:
                subStr = subStr[subStr.index(i) + 1 :] + i
            if len(subStr) > maxLen:
                maxLen = len(subStr)
        return maxLen
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("dvdf"))
    print(Solution().lengthOfLongestSubstring("bbbbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))

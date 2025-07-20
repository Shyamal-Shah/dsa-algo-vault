from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        inner_window = len(words[0])
        window = len(words) * inner_window
        counter = Counter(words)
        res = []
        for i in range(len(s) - window + 1):
            window_Counter = Counter(
                s[i + j : i + j + inner_window] for j in range(0, window, inner_window)
            )
            if counter == window_Counter:
                res.append(i)
        return res


if __name__ == "__main__":
    print(
        Solution().findSubstring(
            "wordgoodgoodgoodbestword", ["word", "good", "best", "good"]
        )
    )
    print(Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]))
    print(
        Solution().findSubstring(
            "wordgoodgoodgoodbestword", ["word", "good", "best", "word"]
        )
    )
    print(Solution().findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))

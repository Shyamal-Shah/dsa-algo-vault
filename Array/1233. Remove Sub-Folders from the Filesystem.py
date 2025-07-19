from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        n = len(folder)
        final = [True] * (n)
        for i in range(n):
            if final[i]:
                for j in range(i + 1, n):
                    if folder[j].startswith(f"{folder[i]}/"):
                        final[j] = False
        ans = []
        for i in range(n):
            if final[i]:
                ans.append(folder[i])
        return ans


if __name__ == "__main__":
    print(Solution().removeSubfolders(["/a", "/a/b", "/c/f", "/c/d", "/c/d/e"]))
    print(Solution().removeSubfolders(["/a", "/a/b/c", "/a/b/d"]))
    print(Solution().removeSubfolders(["/a/b/c", "/a/b/ca", "/a/b/d"]))

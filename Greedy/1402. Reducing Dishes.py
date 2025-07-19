from typing import List

## Brute Force
def maxSatisfaction(satisfaction: List[int]) -> int:
    sorted_satisfaction = sorted(satisfaction)
    total = []
    for j in range(len(satisfaction)):
        total.append(0)
        for i in range(1, len(satisfaction) + 1 - j):
            total[j] += i * sorted_satisfaction[j + i - 1]
    max_satisfaction = max(total)
    if max_satisfaction > 0:
        return max_satisfaction
    else:
        return 0


## Greedy Approach
def maxSatisfactionV2(satisfaction: List[int]) -> int:
    sorted_satisfaction = sorted(satisfaction)
    total, current_total = 0, 0
    for i in range(len(sorted_satisfaction) - 1, -1, -1):
        current_total += sorted_satisfaction[i]

        if current_total > 0:
            total += current_total
        else:
            break
    return total


if __name__ == "__main__":
    print(maxSatisfactionV2([-1, -8, 0, 5, -9]))
    print(maxSatisfactionV2([4, 3, 2]))
    print(maxSatisfactionV2([-1, -4, -5]))

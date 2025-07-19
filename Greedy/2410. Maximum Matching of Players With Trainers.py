from typing import List


def matchPlayersAndTrainers(players: List[int], trainers: List[int]) -> int:
    players.sort(reverse=True)
    trainers.sort(reverse=True)
    maxCount = 0
    j = 0
    for i in range(len(players)):
        if j >= len(trainers):
            break
        if players[i] <= trainers[j]:
            maxCount += 1
            j += 1

    return maxCount


if __name__ == "__main__":
    print(matchPlayersAndTrainers(players=[4, 7, 9], trainers=[8, 2, 5, 8]))
    print(matchPlayersAndTrainers(players=[1, 1, 1], trainers=[10]))

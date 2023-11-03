import math
from collections import defaultdict
from typing import List

def findWinners(matches: List[List[int]]) -> List[List[int]]:
    winners = set()
    winner_list = []
    losers = defaultdict(int)
    one_loss_list = []
    for winner, loser in matches:
        winners.add(winner)
        losers[loser] += 1

    for winner in winners:
        if winner not in losers:
            winner_list.append(winner)

    for loser in losers:
        if losers[loser] == 1:
            one_loss_list.append(loser)

    winner_list.sort()
    one_loss_list.sort()

    return [winner_list, one_loss_list]


def reverseWords(s: str) -> str:
    new = []
    word = []
    for i in s:
        if i == ' ':
            # do a thing
            new.append(''.join(word))
            word = []
        else:
            word.insert(0, i)
    new.append(''.join(word))
    return ' '.join(new)


def reverseWordsBetter(s: str) -> str:
    new = []
    words = s.split()
    for word in words:
        rev = word[::-1]
        new.append(rev)

    return ' '.join(new)


def reverseOnlyLetters(s: str) -> str:
    new = []
    non_letters = []
    for i in range(len(s)):
        if s[i].isalpha():
            new.insert(0, s[i])
        else:
            non_letters.append((i, s[i]))

    for j in non_letters:
        new.insert(j[0], j[1])

    return ''.join(new)


def moveZeroes(nums: List[int]) -> None:
    nums.sort(key=lambda x: x==0)
    print(nums)


def minSubArrayLen(target: int, nums: List[int]) -> int:
    right, left, sumz = 0, 0, 0
    minLength = math.inf
    for right in range(len(nums)):
        sumz += nums[right]
        while sumz >= target:
            minLength = min(minLength, right - left + 1)
            sumz -= nums[left]
            left += 1

    return minLength if minLength != math.inf else 0


def largestAltitude(gain: List[int]) -> int:
    prefix = [0]  # first element, could have been gain[0] and the range(1, len)
    for i in range(len(gain)):
        prefix.append(gain[i] + prefix[-1])  # add the gain to the sum
    print(prefix)
    return max(prefix)


def destCity(paths: List[List[str]]) -> str:
    sources = set()
    dests = set()
    for i in paths:
        sources.add(i[0])
        dests.add(i[1])

    only_dest = dests - sources
    return ''.join(only_dest)

def isPathCrossing(path: str) -> bool:
    cords = [0, 0]
    visits = set()
    visits.add(tuple(cords))
    print(visits)
    directions = {
        'N': [0, 1],
        'S': [0, -1],
        'E': [1, 0],
        'W': [-1, 0]
    }
    for i in path:
        cords[0] += directions[i][0]
        cords[1] += directions[i][1]
        myTuple = tuple(cords)
        if myTuple in visits:
            return True
        visits.add(myTuple)

    return False

def numIdenticalPairs(nums: List[int]) -> int:
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                count += 1

    return count


s = "ab-cd"
nums = [0,0,1]
k = 3
print(moveZeroes(nums))

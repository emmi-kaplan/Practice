# make a function for Fibonacci sequence 0,1,1,2,3,5,8 etc that returns the nth fibonacci number
from collections import defaultdict
from typing import List


def fib(n):
    if n <= 1:
        return n

    one_back = fib(n-1)
    two_back = fib(n-2)

    return one_back + two_back


def findMaxAverage(nums: List[int], k: int) -> float:
    # first constant window
    curr = 0
    for i in range(k):
        curr += nums[i]
        print(curr)

    # compare with other windows
    comp = curr
    for i in range(k, len(nums)):
        comp = comp + nums[i] - nums[i - k]
        print(comp)
        curr = max(comp, curr)
        print(curr)

    # return largest sum divided by size
    return curr / k


def longestOnes(nums: List[int], k: int) -> int:
    # count the number of zeros in the window. Cannot exceed k zeros
    num_zeros = 0
    j = 0  # index of left pointer
    max_length = 0 # length of the largest valid window

    # the first loop moves the first pointer
    for i in range(len(nums)):
        if nums[i] == 0:
            num_zeros += 1

        while num_zeros > k:
            if nums[j] == 0:
                num_zeros -= 1
            j += 1

        max_length = max(max_length, i-j+1)

    return max_length


def runningSum(nums: List[int]) -> List[int]:
    sum_array = [nums[0]]

    for i in range(1, len(nums)):
        sum_array.append(sum_array[-1] + nums[i])

    return sum_array


def minStartValue(nums: List[int]) -> int:
    # first calculate the prefix sum
    sum_array = [nums[0]]
    smallest_k = min(0, nums[0])
    for i in range(1, len(nums)):
        sum_array.append(sum_array[-1] + nums[i])
        smallest_k = min(smallest_k, sum_array[-1])
        print(sum_array)

    return abs(smallest_k) + 1


def getAverages(nums: List[int], k: int) -> List[int]:
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(prefix[-1]+nums[i])

    radius_array = []
    for i in range(len(nums)):
        if i < k or i+k >= len(nums):
            radius = -1
        elif i == k:
            radius = prefix[i + k]//(2*k + 1)
        else:
            radius_sum = prefix[i+k] - prefix[i-k-1]
            radius = radius_sum//(2*k + 1)

        radius_array.append(radius)

    return radius_array


def checkIfPangram(self, sentence: str) -> bool:
    alphabet = {sentence[0]}
    for i in sentence:
        alphabet.add(i)

    return len(alphabet) == 26


def missingNumber(nums: List[int]) -> int:
    included = set()
    for i in nums:
        included.add(i)

    for i in range(len(nums)+1):
        print(i)
        if i not in included:
            return i


def countElements(arr: List[int]) -> int:
    nums = {}
    count = 0

    for i in arr:
        nums[i] = i

    for i in arr:
        if i+1 in nums.values():
            count += 1

    return count


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


def largestUniqueNumber(self, nums: List[int]) -> int:
    counter = defaultdict(int)
    nums_occuring_once = [-1]
    for num in nums:
        counter[num] += 1

    for num, count in counter.items():
        if count == 1:
            nums_occuring_once.append(num)

    nums_occuring_once.sort()

    return nums_occuring_once[-1]


def maxNumberOfBalloons(self, text: str) -> int:
    balloons = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
    for t in text:
        if t in ['b', 'a', 'n']:
            balloons[t] += 2
        if t in ['l', 'o']:
            balloons[t] += 1

    return min(balloons.values()) // 2


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            # do something
            return
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    # target is not in arr, but left is at the insertion point
    return left

nums = [1,3,2,3,5,0]
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
k = 3
print(findWinners(matches))



# name, start, end
NamedRegion = tuple[str, int, int]
Gene = NamedRegion
Protein = NamedRegion

genes: list[Gene] = [
    ('cryIA', 7, 16),
    ('PEP', 4, 11),
    ('cry9C', 11, 22),
    ('PS', 22, 28),
    ('35S', 15, 22),
    ('35S', 0, 7),
    ('brca2', 7, 22)
]


def find_proteins(genes: list[Gene]) -> list[Protein]:
    """
    :param genes: List of (region_name, start_index, end_index)
    :returns proteins: List of (protein_name, start_index, end_index)
    """

    protein_list = []
    for gene in genes:
        protein_list.append(gene)

    for i in protein_list:
        end_index = i[2]

        for x in genes:
            start_index = x[1]

            if start_index == end_index:
                name = i[0] + "_" + x[0]
                new_protein = NamedRegion([name, i[1], x[2]])
                protein_list.append(new_protein)

    return protein_list


# print(sorted(find_proteins(genes)))
# print(len(find_proteins(genes)))
# print(sorted([
#     ('35S', 0, 7),
#     ('cryIA', 7, 16),
#     ('PEP', 4, 11),
#     ('35S', 15, 22),
#     ('brca2', 7, 22),
#     ('cry9C', 11, 22),
#     ('PS', 22, 28),
#     ('35S_cryIA', 0, 16),
#     ('PEP_cry9C', 4, 22),
#     ('PEP_cry9C_PS', 4, 28),
#     ('cry9C_PS', 11, 28),
#     ('35S_PS', 15, 28),
#     ('35S_brca2', 0, 22),
#     ('35S_brca2_PS', 0, 28),
#     ('brca2_PS', 7, 28),
# ]))
#
# assert sorted(find_proteins(genes)) == sorted([
#     ('35S', 0, 7),
#     ('cryIA', 7, 16),
#     ('PEP', 4, 11),
#     ('35S', 15, 22),
#     ('brca2', 7, 22),
#     ('cry9C', 11, 22),
#     ('PS', 22, 28),
#     ('35S_cryIA', 0, 16),
#     ('PEP_cry9C', 4, 22),
#     ('PEP_cry9C_PS', 4, 28),
#     ('cry9C_PS', 11, 28),
#     ('35S_PS', 15, 28),
#     ('35S_brca2', 0, 22),
#     ('35S_brca2_PS', 0, 28),
#     ('brca2_PS', 7, 28),
# ])
# print('Passed!')
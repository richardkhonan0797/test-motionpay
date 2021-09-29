from typing import List


def bilangan_kedua_terbesar(nums: List[int]) -> int:

    first_largest = second_largest = 0

    for num in nums:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num < first_largest:
            second_largest = num

    return second_largest

print(bilangan_kedua_terbesar(nums=[1, 12, 31, 5, 3, 23, 4, 5, 22]))     # 23
print(bilangan_kedua_terbesar(nums=[-0.5, -0.76, 0.45, -0.2, 4.5, 3.5])) # 3.5
print(bilangan_kedua_terbesar(nums=[98, 12, 42, 13, 13, 56, 100, 99]))   # 99
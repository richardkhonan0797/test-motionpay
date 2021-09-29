from typing import List, Union


def jumlah_pasangan_bilangan(nums: List[int], target: Union[int, bool]) -> bool:
    
    nums_sisa = []

    for num in nums:
        sisa = target - num

        if sisa in nums_sisa:
            return True

        nums_sisa.append(num)

    return False

print(jumlah_pasangan_bilangan(nums=[1, 2, 4, 4, 5, 6, 7, 7, 8, 8], target=12))   # True
print(jumlah_pasangan_bilangan(nums=[1, 2, 4, 4, 5, 8, 9, 9, 12, 19], target=4))  # False
print(jumlah_pasangan_bilangan(nums=[-9.3, -0.5, 0.25, 0.3, 1.34], target=-7.96)) # True
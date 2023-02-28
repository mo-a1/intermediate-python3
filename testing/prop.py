ls = [0,0,1,1,1,2,2,3,3,4]


def remove_duplicates(nums) -> int:
    without_duplicates = sorted(set(nums))
    l = len(without_duplicates)
    for i in range(l):
        nums[i] = without_duplicates[i]
    return l


print(remove_duplicates(ls))
print(ls)

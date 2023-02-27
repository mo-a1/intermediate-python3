from collections import Counter

l = [11, 25, 1, 2, 11, 6, 2, 18, 9, 1, 4, 15, 11, 3, 1, 2, 14, 15, 19, 9, 9, 9, 9, 8, 3, 11, 2, 58]

nums_count = Counter(l)
common_nums = nums_count.most_common(2)

print(nums_count)
print(common_nums)

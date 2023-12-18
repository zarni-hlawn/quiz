# 1. Two Sum
# https://leetcode.com/problems/two-sum/

def two_sum(nums, target):
    num_indices = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_indices:
            return [num_indices[complement], i]

        num_indices[num] = i

    return None


if __name__ == "__main__":
    # Case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(two_sum(nums1, target1))

    # Case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(two_sum(nums2, target2))

    # Case 3
    nums3 = [3, 3]
    target3 = 6
    print(two_sum(nums3, target3))

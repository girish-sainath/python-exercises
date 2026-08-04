class Solution:
    @staticmethod
    def check_sorted_rotated(nums:list[int]) -> bool:
        if not nums:
            return False
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
                if count > 1:
                    return False
        return True


def main() -> None:
    many_nums = [
        [3,4,5,1,2],
        [2,1,3,4],
        [1,2,3],
    ]
    for nums in many_nums:
        print(f'Check for sorted or rotated array `{nums}`:', Solution.check_sorted_rotated(nums))


if __name__ == '__main__':
    main()
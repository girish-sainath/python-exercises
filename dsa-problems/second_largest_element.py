class Solution:
    @staticmethod
    def second_largest_element(nums: list[int]) -> int:
        if len(nums) < 2:
            return -1
        first = float('-inf')
        second = float('-inf')
        for num in nums:
            if num > first:
                second = first
                first = num
            elif first > num > second:
                second = num
        if second == float('-inf'):
            second = -1
        return second


def main() -> None:
    many_nums = [
        [8, 8, 7, 6, 5],
        [10, 10, 10, 10, 10],
        [7, 7, 2, 2, 10, 10, 10],
        [],
        [2],
    ]
    for nums in many_nums:
        print(f'Second Largest Number of `{nums}`:', Solution.second_largest_element(nums))


if __name__ == '__main__':
    main()
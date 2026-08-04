class Solution:

    @staticmethod
    def largest_element(nums) -> int:
        # print('Largest Element For With Enumerate `for idx, num in enumerate(nums)`: ', Solution.largest_element_for_with_enumerate(nums))
        # print('Largest Element Built-in `max(list)`: ', Solution.largest_element_builtin(nums))
        # print('Largest Element For In List `for num in nums`:', Solution.largest_element_for_in_list(nums))
        # print('Largest Element For In Range `for i in range(len(nums))`:', Solution.largest_element_for_in_range(nums))
        return Solution.largest_element_for_in_list(nums)

    @staticmethod
    def largest_element_for_with_enumerate(nums) -> int:
        largest = nums[0]
        for idx, num in enumerate(nums):
            if num > largest:
                largest = num
        return largest

    @staticmethod
    def largest_element_builtin(nums) -> int:
        return max(nums)

    @staticmethod
    def largest_element_for_in_list(nums) -> int:
        largest = nums[0]
        for num in nums:
            if num > largest:
                largest = num
        return largest

    @staticmethod
    def largest_element_for_in_range(nums) -> int:
        largest = nums[0]
        for i in range(len(nums)):
            if nums[i] > largest:
                largest = nums[i]
        return largest


def main() -> None:
    many_nums = [
        [3, 3, 6, 1],
        [3, 3, 0, 99, -40],
        [-4, -3, 0, 1, -8],
    ]
    for nums in many_nums:
        print(f'Largest Number of `{nums}`:', Solution.largest_element(nums))


if __name__ == '__main__':
    main()
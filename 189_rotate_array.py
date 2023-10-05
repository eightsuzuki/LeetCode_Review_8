# Using buffer
# n = len(nums)
# time: O(n + k)
# space: O(k)

class Solution1:
    def rotate(self, nums: list[int], k: int) -> None:
        """Function to rotate the array to the right by k steps,
        where k is non-negative. The array is modified in-place.
        
        Args:
            nums (list[int]): Rotated array
            k (int): The number of steps for rotation
        """
        buf = []
        k %= len(nums)
        for i in reversed(range(1, k + 1)):
            buf.append(nums[-i])
        
        for i in reversed(range(len(nums) - k)):
            nums[i + k] = nums[i]

        for i in range(k):
            nums[i] = buf[i]

# Cyclic replacements
# time: 0(n)
# space: O(1)

class Solution2:
    def rotate(self, nums: list[int], k: int) -> None:
        k %= len(nums)
        n = len(nums)
        count = 0
        start = 0
        while count < n:
            current_idx = start
            prev = nums[start]

            while True:
                next_idx = (current_idx + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current_idx = next_idx
                count += 1

                if current_idx == start:
                    break
            
            start += 1

# Reverse array
# time: O(n)
# space: O(1)

class Solution3:
    def rotate(self, nums: list[int], k: int) -> None:
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums: list[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        
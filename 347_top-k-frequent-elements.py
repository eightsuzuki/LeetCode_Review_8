import heapq
from collections import Counter
from typing import List


class FrequentElements:
    def find_k_frequent_elements(self, nums: List[int], k: int) -> List[int]:
        """Function to find the k most frequent elements.

        Args:
            nums(list[int]): list of integer
            target(int): integer

        Returns:
            list[int]: the k most frequent elements in any order

        Raises:
            TypeError
        """
        # n := len(nums)
        # time: O(nlogk)
        # space: O(n)
        if type(nums) is not list:
            raise TypeError("The type of the input nums should be list")

        if type(k) is not int:
            raise TypeError("The type of the input k should be integer")

        if not nums or not k:
            return []

        if len(set(nums)) <= k:
            return list(set(nums))

        from_num_to_count = Counter(nums)
        count_heap = []
        for num, count in from_num_to_count.items():
            heapq.heappush(count_heap, (count, num))
            if len(count_heap) > k:
                heapq.heappop(count_heap)

        k_frequent_elements = []
        while count_heap:
            count, num = heapq.heappop(count_heap)
            k_frequent_elements.append(num)

        return k_frequent_elements

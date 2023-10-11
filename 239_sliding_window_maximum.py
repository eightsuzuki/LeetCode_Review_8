import heapq
from collections import defaultdict
from typing import List


class SlidingWindow:
    def find_max_elements(self, nums: List[int], k: int) -> List[int]:
        ans = []
        heap_list = []
        from_num_to_time = defaultdict(int)
        for idx, num in enumerate(nums):
            from_num_to_time[num] += 1
            heapq.heappush(heap_list, -nums[idx])

            if idx >= k:
                from_num_to_time[nums[idx - k]] -= 1
                while from_num_to_time[-heap_list[0]] == 0:
                    heapq.heappop(heap_list)

            if idx >= k - 1:
                ans.append(-heap_list[0])

        return ans
import heapq
from typing import List


class PairSum:
    def get_k_smallest_pairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        idx1, idx2 = 0, 0
        seen = set()
        heap = []
        heapq.heappush(heap, (nums1[idx1]+nums2[idx2], (idx1, idx2)))
        seen.add((idx1, idx2))
        ans = []
        while len(ans) < k and heap:
            _, cur_idx = heapq.heappop(heap)
            cur1, cur2 = cur_idx
            ans.append([nums1[cur1], nums2[cur2]])
            if cur1+1 < len(nums1) and (cur1+1, cur2) not in seen:
                heapq.heappush(heap, (nums1[cur1+1]+nums2[cur2], (cur1+1, cur2)))
                seen.add((cur1+1, cur2))
            if cur2+1 < len(nums2) and (cur1, cur2+1) not in seen:
                heapq.heappush(heap, (nums1[cur1]+nums2[cur2+1], (cur1, cur2+1)))
                seen.add((cur1, cur2+1))

        return ans
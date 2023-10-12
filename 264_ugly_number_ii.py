import heapq

# priority queue
# time: O(n * logn)
# space: O(n)

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        for _ in range(n - 1):
            num = heapq.heappop(heap)

            # Remove duplicates
            while heap and heap[0] == num:
                heapq.heappop(heap)
            
            heapq.heappush(heap, 2 * num)
            heapq.heappush(heap, 3 * num)
            heapq.heappush(heap, 5 * num)

        return heap[0]

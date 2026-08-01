class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        count = Counter(tasks)

        maxHeap = [-num for num in count.values()]

        heapq.heapify(maxHeap)

        intervals = 0
        q = collections.deque()

        while q or maxHeap:
            intervals += 1

            if maxHeap:
                num = heapq.heappop(maxHeap) + 1
                if (num != 0):
                    q.append([num, intervals + n])
            
            if q and q[0][1] == intervals:
                heapq.heappush(maxHeap, q.popleft()[0])
            
        return intervals


        
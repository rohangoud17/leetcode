class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        maxHeap = [-m for m in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = collections.deque()
        while maxHeap or q:
            time += 1

            if maxHeap:
                m = heapq.heappop(maxHeap) + 1
                if (m != 0):
                    q.append([m, time + n ])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
        

        return time


            
#I know the pattern of this question what it is asking, but I'm not able to figure out what data structure to use for this problem and how to recognize what to do for this particular question. 

        
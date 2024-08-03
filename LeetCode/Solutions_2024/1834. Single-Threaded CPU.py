from heapq import heappop, heappush


class Task(list):
    def __init__(self, enqueueTime: int, processingTime: int, orig_idx: int):
        super().__init__([enqueueTime, processingTime, orig_idx])
        self.orig_idx = orig_idx
        self.processingTime = processingTime
        self.enqueueTime = enqueueTime

    def __lt__(self, other):
        # first compare processing time then the orig_idx in case of equal processing time
        return self.processingTime < other.processingTime or (
            self.processingTime == other.processingTime and self.orig_idx < other.orig_idx
        )


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        answer = []
        n = len(tasks)

        # add the original index to each task so it will be  [enqueueTime, processingTime, original_index]
        tasks = [Task(*task, orig_index) for orig_index, task in enumerate(tasks)]

        # sort tasks by enqueueTime:
        tasks.sort(key=lambda task: task.enqueueTime)

        i_next_task = 0  # the next task to inspect

        # The starting time
        t_now = 0

        # min-heap that stores (processingTime, task index) of available tasks
        priority_heap = []
        while i_next_task < n or len(priority_heap) > 0:

            if len(priority_heap) == 0:
                # no tasks waiting - wait to take the next task
                cur_task = tasks[i_next_task]
                heappush(priority_heap, cur_task)
                t_now = max(t_now, cur_task.enqueueTime)
                i_next_task += 1

            # add also tasks that were enqueued before or at t_now to heap
            while i_next_task < n and tasks[i_next_task].enqueueTime <= t_now:
                cur_task = tasks[i_next_task]
                heappush(priority_heap, cur_task)
                i_next_task += 1

            # The CPU is idle now
            # process the highest priority task from the heap
            if priority_heap:
                cur_task = heappop(priority_heap)
                t_now = max(cur_task.enqueueTime, t_now) + cur_task.processingTime
                answer.append(cur_task.orig_idx)
        return answer


if __name__ == "__main__":
    sol = Solution()
    tasks = [[5, 6], [9, 4], [3, 9], [3, 7], [1, 1], [6, 9], [9, 1]]
    print(sol.getOrder(tasks))

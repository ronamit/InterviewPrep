from collections import Counter
from heapq import heapify, heappop, heappush


def add_to_dict_list(d, k, x):
    if k in d:
        d[k].append(x)
    else:
        d[k] = [x]


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        tasks_counts = Counter(tasks)
        n_task_names = len(tasks_counts)

        print("Task counts: ", tasks_counts)

        # or - direct compute
        # strategy: take the max_count task
        # spread it out such that each other task is done before we combe back to it
        # (and add idles if needed)
        # update the task counts and keep track of n_completed
        # then repeat until all are completed O(n log(MAX_TASK_TYPES)) with max-heap

        # use minus to get max-heap (task_name, minus count)
        h = [(t, -c) for (t, c) in tasks_counts.items()]
        heapify(h)

        # dict with (cycle index that the task can be used again): list of (task_name, task_count)
        tasks_on_cooldown = {}

        n_completed = 0
        i_cycle = 0

        while n_completed < n_task_names:
            print(f"----Cycle {i_cycle} ----")
            # check if there are tasks that go out of cooldown:
            if i_cycle in tasks_on_cooldown:
                for task_name, task_count in tasks_on_cooldown[i_cycle]:
                    print(f"Task {task_name} is out of cooldown")
                    heappush(h, (task_name, -task_count))
                del tasks_on_cooldown[i_cycle]

            # if there are no jobs that are not on cooldown - idle cycle
            #  otherwise, take the the task with most remain jobs (from non cooldown tasks)
            if len(h) > 0:
                item = heappop(h)
                task_name = item[0]
                task_count = -item[1]
                print("Do: ", task_name)

                # update remain job count for task:
                task_count -= 1

                if task_count > 0:
                    # add it to cooldown:
                    print(f"Task {task_name} is on cooldown until cycle {i_cycle + 1 + n}")
                    add_to_dict_list(tasks_on_cooldown, i_cycle + 1 + n, (task_name, task_count))
                else:
                    n_completed += 1
                    print(f"Completed {task_name} ({n_completed}/{n_task_names})")
            else:
                print("idle")
            # cycle finished
            i_cycle += 1

        return i_cycle


if __name__ == "__main__":
    sol = Solution()
    tasks = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"]
    n = 2
    print("\n  Answer: ", sol.leastInterval(tasks, n), " cycles")

from heapq import heappush, heappop
import itertools


# adapted from https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes
class PriorityQueue:
    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.REMOVED = '<removed-task>'
        self.counter = itertools.count()

    def add_task(self, task, priority=0):
        if task.state in self.entry_finder:
            # check if cost is lower than previous cost
            if priority < self.entry_finder[task.state][0]:
                self.remove_task(task)
                count = next(self.counter)
                entry = [priority, count, task]
                self.entry_finder[task.state] = entry
                heappush(self.pq, entry)
        else:
            count = next(self.counter)
            entry = [priority, count, task]
            self.entry_finder[task.state] = entry
            heappush(self.pq, entry)

    def remove_task(self, task):
        entry = self.entry_finder.pop(task.state)
        entry[-1] = self.REMOVED

    def pop_task(self):
        while self.pq:
            priority, count, task = heappop(self.pq)
            if task is not self.REMOVED:
                return task
        raise KeyError('pop from an empty priority queue')

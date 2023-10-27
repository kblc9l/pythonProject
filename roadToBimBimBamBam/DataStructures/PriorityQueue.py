from heapq import heappush, heappop
from dataclasses import dataclass
from itertools import count


@dataclass
class Message:
    event: str


class PriorityQueue:
    def __init__(self):
        self._elements = []
        self._counter = count()

    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value)
        heappush(self._elements, element)

    def dequeue(self):
        return heappop(self._elements)[-1]


CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1
message = PriorityQueue()
message.enqueue_with_priority(IMPORTANT, Message('Windshield wipers turned on'))
message.enqueue_with_priority(NEUTRAL, Message('Radio station tuned in'))
message.enqueue_with_priority(CRITICAL, Message('Brake pedal depressed'))
message.enqueue_with_priority(IMPORTANT, Message('Hazard lights turned on'))

print(message.dequeue())
print(message.dequeue())
print(message.dequeue())
print(message.dequeue())

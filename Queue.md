# Queue
A queue is a linear data structure that follows the First In First Out (FIFO) principle. It means that the first element added to the queue will be the first one to be removed. A queue can be implemented using arrays or linked lists.

Queues are commonly used in scenarios where **order matters**, such as in scheduling tasks, handling requests, or managing resources.

## Problem 1. [649. Dota2 Senate](https://leetcode.com/problems/dota2-senate/)
```python
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()

        # Step 1: Fill queues with initial indices
        for i, c in enumerate(senate):
            if c == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        # Step 2: Simulate the rounds
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                # R acts first, bans D
                radiant.append(r + n)
            else:
                # D acts first, bans R
                dire.append(d + n)

        # Step 3: Determine the winner
        return "Radiant" if radiant else "Dire"
```
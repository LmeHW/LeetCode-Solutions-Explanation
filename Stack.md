# Stack

## Situation when to use Stack
1. Last-In-First-Out (LIFO) Order is needed
   -  The most recently added item should be processed first.
2. Backtracking is involved
	- Examples: Undo operations, navigating browser history, or recursive parsing.
3. Matching and Balancing
	- Parentheses matching, HTML/XML tag validation, or expression evaluation.
4. Depth-First Search (DFS)
	- In graphs or trees (especially iterative implementations).
5. Function Call Management
	- The system call stack handles function execution and return.


## problems
### [394. Decode String](https://leetcode.com/problems/decode-string/)
```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = ""
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append((current_str, current_num))
                current_str, current_num = "", 0
            elif char == ']':
                last_str, num = stack.pop()
                current_str = last_str + num * current_str
            else:
                current_str += char
        
        return current_str
```

### [BrainFuck](https://esolangs.org/wiki/Brainfuck)

Please refer to `brain_fuck.py` for the implementation of BrainFuck interpreter.
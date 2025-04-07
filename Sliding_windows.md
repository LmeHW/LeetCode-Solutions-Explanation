# Sliding Windows
This is a collection of **sliding window** problems from LeetCode.

This algorithm is used to solve problems that require us to find a **subarray** or **substring** that meets certain criteria. The sliding window technique involves maintaining a window of elements and adjusting its size and position as needed.

---

*Comment:*

[Apr/6/2025] - The most important idea for similar problems is that the subarray is defined by **'consecutive'**.

---

## Fixed Size Sliding Window
### Problem 1. [643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)

The main idea here is **swap**. While moving the fixed size window, we can **subtract** the element that is going out of the window and **add** the new element that is coming into the window. This way, we can maintain the sum of the elements in the current window without having to recalculate it from scratch.

This can reduce the time complexity from $O(n*k)$ to $O(n)$, where `n` is the length of the array and `k` is the size of the window.
```python
def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avr = temp = sum(nums[:k])
        for i in range(len(nums) - k):
            temp = temp - nums[i] + nums[i+k]
            max_avr = max(max_avr, temp)
        return max_avr/k
### LmeHW [Apr/6/2025]
```

#### Similar Problems
- [1456. Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)

## Variable Size Sliding Window
### Problem 1. [1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)

The fundamental idea: while moving the right pointer, we can **expand** the window by adding the new element. If the number of `0`s in the window exceeds `k`, we need to **shrink** the window from the left until the number of `0`s is less than or equal to `k`.

However, you may confusing that we are not returning the such subarray (`i` and `j` are not the same as the left and right pointers of such subarray). Instead, we are returning the longest window size. 

Actually, we only keep track of the optimal window size by using `j - i + 1`, which is the length of the current Window. If `k` is now less than `0`, which means the window is invalid, we need to shrink the window from the left, rather than the right since we are exploring! 

In short, we are sliding the currently best window from left to right.

To check your understanding, you can try how to output the *longest subarray* instead of the length. 
```python
def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        for j in range(len(nums)):
            k -= 1 - nums[j]     # k = the remainning `flips`
            if k < 0:
                k += 1 - nums[i]
                i += 1
        return j - i + 1
```
> Copied from [Lee](https://leetcode.com/problems/max-consecutive-ones-iii/solutions/247564/java-c-python-sliding-window). To see more details, please click the link. Amazing solution!


### Similar Problems
- [1493. Longest Substring of 1's After Deleting One Elements](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element)



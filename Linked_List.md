# Linked List

## Compute the middle of a linked list
```python
def middleNode(self, head: ListNode) -> ListNode:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```
## Reverse a linked list
```python
def reverseList(self, head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev
```
## Merge two sorted linked lists
```python
def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(0)
    tail = dummy
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 if list1 else list2
    return dummy.next
```
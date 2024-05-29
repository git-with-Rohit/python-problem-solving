# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

## Approach
- Traverse both linked lists and add corresponding digits.
- Use a carry to handle sums greater than 10.
- Continue until both linked lists and carry are processed.

## Examples

**Example 1:**  
Input: l1 = [2,4,3], l2 = [5,6,4]  
Output: [7,0,8]  
Explanation: 342 + 465 = 807.

**Example 2:**  
Input: l1 = [0], l2 = [0]  
Output: [0]

**Example 3:**  
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]  
Output: [8,9,9,9,0,0,0,1]

## Constraints
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.

## Solution
See `solution.py` for the implementation.

## Running Tests
To run the tests for this problem, navigate to the problem directory and run the `tests.py` file.

1. Navigate to the problem directory:
   ```bash
   cd problem2_add_two_numbers
    ```

2. Run the tests using Python:
    ```bash
   python3 tests.py
    ```
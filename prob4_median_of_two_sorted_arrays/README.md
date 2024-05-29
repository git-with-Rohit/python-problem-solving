# Median of Two Sorted Arrays

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

## Examples

**Example 1:**  
Input: nums1 = [1,3], nums2 = [2]  
Output: 2.00000  
Explanation: merged array = [1,2,3] and median is 2.

**Example 2:**  
Input: nums1 = [1,2], nums2 = [3,4]  
Output: 2.50000  
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

## Constraints
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6

## Solution
See `solution.py` for the implementation.

## Running Tests
To run the tests for this problem, navigate to the problem directory and run the `tests.py` file.

1. Navigate to the problem directory:
   ```bash
   cd problem4_median_of_two_sorted_arrays

2. Run the tests using Python:
    ```bash
   python3 tests.py
    ```
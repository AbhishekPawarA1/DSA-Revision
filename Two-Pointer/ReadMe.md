 # Questions




## Basic Questions 


Find all pairs with a given sum


Problem: Find all pairs in a sorted array whose sum equals a target.
Example:
Input: arr = [1, 2, 3, 4, 5], target = 6
Output: [(1, 5), (2, 4)]
Remove duplicates from a sorted array

Problem: Remove duplicates in-place from a sorted array and return the new length.
Example:
Input: arr = [1, 1, 2, 2, 3]
Output: 3
Reverse a string

Problem: Reverse a string using two pointers.
Example:
Input: "hello"
Output: "olleh"
Find the middle of a linked list

Problem: Return the middle node of a linked list using two pointers.
Example:
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 3
Square and sort a sorted array

Problem: Return a sorted array of the squares of elements from a sorted array.
Example:
Input: arr = [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]
Move zeros to the end of the array

Problem: Rearrange an array so that all zeros are at the end.
Example:
Input: arr = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
Check if a string is a palindrome

Problem: Determine if a string reads the same backward as forward.
Example:
Input: "radar"
Output: True
Find the intersection of two sorted arrays

Problem: Return the intersection of two sorted arrays.
Example:
Input: arr1 = [1, 2, 4], arr2 = [2, 4, 6]
Output: [2, 4]
Partition array into even and odd elements

Problem: Partition the array such that even elements come first.
Example:
Input: arr = [3, 1, 2, 4]
Output: [2, 4, 3, 1]
Merge two sorted arrays

Problem: Merge two sorted arrays into one sorted array.
Example:
Input: arr1 = [1, 3], arr2 = [2, 4]
Output: [1, 2, 3, 4]
Remove all instances of a specific value

Problem: Remove all occurrences of a value from an array.
Example:
Input: arr = [3, 2, 2, 3], val = 3
Output: [2, 2]
Find the first missing positive integer

Problem: Find the smallest missing positive integer.
Example:
Input: [3, 4, -1, 1]
Output: 2
Count pairs with a given sum in an unsorted array

Problem: Count pairs with a given sum using two pointers.
Example:
Input: arr = [1, 5, 7, -1], target = 6
Output: 2
Sort an array of 0s, 1s, and 2s

Problem: Sort an array containing 0s, 1s, and 2s without using extra space.
Example:
Input: [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]
Find the closest pair to a target sum

Problem: Find the closest pair to a target sum in a sorted array.
Example:
Input: arr = [1, 3, 4, 7], target = 8
Output: (3, 4)
Remove characters to make a string palindrome

Problem: Find if a string can be converted into a palindrome by removing at most one character.
Example:
Input: "abca"
Output: True
Find subarray with maximum sum (Kadane’s Algorithm)

Problem: Find the subarray with the maximum sum.
Example:
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: [4, -1, 2, 1]
Longest substring with at most two distinct characters

Problem: Find the longest substring containing at most two distinct characters.
Example:
Input: "eceba"
Output: 3 (ece)
Rearrange array alternately

Problem: Rearrange an array such that the maximum and minimum elements alternate.
Example:
Input: [1, 2, 3, 4, 5, 6]
Output: [6, 1, 5, 2, 4, 3]
Find the minimum length subarray with a given sum

Problem: Find the smallest subarray with a sum >= target.
Example:
Input: arr = [2, 3, 1, 2, 4, 3], target = 7
Output: 2



## Medium Questions


Three Sum Problem

Problem: Find all unique triplets in the array that sum up to zero.
Space Complexity: O(1) (constant space if counting results)
Example:
Input: arr = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
Container With Most Water

Problem: Given an array of heights representing a histogram, find the maximum area of water that can be trapped between two lines.
Space Complexity: O(1) (constant space)
Example:
Input: heights = [1,8,6,2,5,4,8,3,7]
Output: 49
Longest Substring Without Repeating Characters

Problem: Given a string, find the length of the longest substring without repeating characters.
Space Complexity: O(n) (to store the visited characters)
Example:
Input: "abcabcbb"
Output: 3 (substring "abc")
Subarray Product Less Than K

Problem: Find the number of contiguous subarrays whose product is less than a given number k.
Space Complexity: O(1) (constant space for pointers)
Example:
Input: arr = [10, 5, 2, 6], k = 100
Output: 8
Find the Peak Element

Problem: Find a peak element in an array, where an element is greater than or equal to its neighbors.
Space Complexity: O(1) (constant space)
Example:
Input: arr = [1, 3, 20, 4, 1, 0]
Output: 20
Valid Palindrome II

Problem: Determine if a string can be a palindrome by removing at most one character.
Space Complexity: O(1) (constant space)
Example:
Input: "abca"
Output: True
Find the Minimum Window Substring

Problem: Given two strings s and t, find the minimum window in s which contains all characters of t.
Space Complexity: O(n) (to store the window characters)
Example:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Maximum Subarray (Kadane's Algorithm)

Problem: Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
Space Complexity: O(1) (constant space)
Example:
Input: arr = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6 (subarray [4, -1, 2, 1])
Trapping Rain Water

Problem: Given an array of non-negative integers representing heights of walls, compute how much water can be trapped after raining.
Space Complexity: O(1) (constant space)
Example:
Input: arr = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Sort Colors (Dutch National Flag Problem)

Problem: Sort an array containing only 0s, 1s, and 2s.
Space Complexity: O(1) (constant space)
Example:
Input: arr = [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]
Remove Duplicates from Sorted Array II

Problem: Remove duplicates from a sorted array such that each element appears at most twice.
Space Complexity: O(1) (constant space)
Example:
Input: arr = [1, 1, 1, 2, 2, 3]
Output: [1, 1, 2, 2, 3]
Find All Anagrams in a String

Problem: Given a string s and a string p, find all the start indices of p's anagrams in s.
Space Complexity: O(n) (to store frequency counts)
Example:
Input: s = "cbaebabacd", p = "abc"
Output: [0, 6]
Minimum Size Subarray Sum

Problem: Given an array of positive integers, find the minimal length of a contiguous subarray whose sum is greater than or equal to a given target.
Space Complexity: O(1) (constant space)
Example:
Input: arr = [2, 3, 1, 2, 4, 3], target = 7
Output: 2
Max Consecutive Ones III

Problem: Given a binary array, find the maximum number of consecutive 1s in the array by flipping at most k 0s.
Space Complexity: O(1) (constant space)
Example:
Input: arr = [1,1,0,0,1,1,1,0,1,1], k = 2
Output: 6
Shortest Subarray with Sum at Least K

Problem: Find the shortest subarray with a sum greater than or equal to a given integer k.
Space Complexity: O(n) (to store prefix sums)
Example:
Input: arr = [1, 2, 3, 4, 5], k = 11
Output: 3
Longest Repeating Character Replacement

Problem: Given a string, you can perform the operation of replacing one character with any other character. Find the length of the longest substring containing the same letter after at most k changes.
Space Complexity: O(1) (constant space)
Example:
Input: s = "AABABBA", k = 1
Output: 4
Find Duplicate in Array

Problem: Given an array containing n + 1 integers where each integer is between 1 and n, find the duplicate number.
Space Complexity: O(1) (constant space, using two pointers)
Example:
Input: arr = [1, 3, 4, 2, 2]
Output: 2
Find All Pairs with Sum Equal to a Target

Problem: Given an array, find all pairs of elements that sum up to a given target value.
Space Complexity: O(1) (constant space if modifying in-place)
Example:
Input: arr = [1, 2, 3, 4, 5], target = 6
Output: [(1, 5), (2, 4)]
Rotate Array

Problem: Rotate an array to the right by k steps.
Space Complexity: O(1) (constant space)
Example:
Input: arr = [1, 2, 3, 4, 5, 6, 7], k = 3
Output: [5, 6, 7, 1, 2, 3, 4]
Find the Longest Subarray with Sum at Most K

Problem: Find the longest subarray with a sum less than or equal to a given integer k.
Space Complexity: O(1) (constant space)
Example:
Input: arr = [1, 2, 3, 4, 5], k = 9
Output: 4



## Hard Questions 
 

Max Sum of 3 Non-Overlapping Subarrays

Problem: Given an array, find the maximum sum of three non-overlapping subarrays with lengths L, M, and N.
Space Complexity: O(n) (for storing prefix sums and results)
Example:
Input: arr = [1,2,1,2,6,7,5,1], L = 2, M = 2, N = 2
Output: [0, 3, 5] (subarrays [1, 2], [6, 7], [5, 1])
Shortest Subarray with Sum at Least K

Problem: Given an integer array A and an integer K, find the shortest subarray whose sum is greater than or equal to K.
Space Complexity: O(n) (for storing prefix sums)
Example:
Input: arr = [1, 2, 3, 4, 5], k = 11
Output: 3
Find the Smallest Range Covering Elements from K Lists

Problem: Given k sorted lists of numbers, find the smallest range that includes at least one number from each of the lists.
Space Complexity: O(k) (for storing pointers for each list)
Example:
Input: lists = [[1, 5, 9], [4, 6, 8], [7, 10, 12]]
Output: [4, 7]
Sort Colors (Dutch National Flag)

Problem: Sort an array containing 0s, 1s, and 2s.
Space Complexity: O(1) (constant space)
Example:
Input: arr = [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]
Largest Rectangle in Histogram

Problem: Given an array of integers representing heights of histogram bars, find the area of the largest rectangle in the histogram.
Space Complexity: O(n) (for storing indices in the stack)
Example:
Input: heights = [2, 1, 5, 6, 2, 3]
Output: 10
3Sum Closest

Problem: Given an array of integers and a target value, find three integers in the array such that their sum is closest to the target.
Space Complexity: O(1) (constant space)
Example:
Input: arr = [-1, 2, 1, -4], target = 1
Output: 2 (sum of -1 + 2 + 1)
Find the Peak Element

Problem: Find a peak element in the array where an element is greater than or equal to its neighbors.
Space Complexity: O(1) (constant space)
Example:
Input: arr = [1, 3, 20, 4, 1, 0]
Output: 20
Substring with Concatenation of All Words

Problem: Given a string s and an array of words words, find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once.
Space Complexity: O(n) (for storing word frequencies)
Example:
Input: s = "barfoothefoobarman", words = ["foo", "bar"]
Output: [0, 9]
Sliding Window Maximum

Problem: Given an array nums and an integer k, find the maximum value in every sliding window of size k.
Space Complexity: O(k) (for storing window elements)
Example:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3, 3, 5, 5, 6, 7]
Largest Number

Problem: Given a list of non-negative integers, arrange them such that they form the largest number possible.
Space Complexity: O(n) (for storing and sorting the numbers)
Example:
Input: nums = [3, 30, 34, 5, 9]
Output: "9534330"
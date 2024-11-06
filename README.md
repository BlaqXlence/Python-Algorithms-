The following are some of the basic  algorithms that must be at your fingure tips
1) Merge Sorting
   Merge Sort is a classic divide-and-conquer algorithm widely used for sorting arrays. It operates by recursively splitting the array into smaller subarrays until each subarray contains a single element. Then, it merges these subarrays back together in a sorted order. Below is a detailed explanation of the Merge Sort algorithm along with its implementation in Python.
2) Bubble sorting
   Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process is repeated until the list is sorted. Although it's not the most efficient sorting algorithm for large datasets, it's a great way to understand sorting concepts.
3) Insertion Sorting
   Insertion Sort is a simple and intuitive sorting algorithm that builds a sorted array one element at a time. It is particularly efficient for small datasets or partially sorted arrays. The algorithm works by iterating through the input list, taking one element at a time, and placing it in the correct position within the already sorted portion of the list.
4) Sort selection
   Selection sort is a straightforward sorting algorithm that operates by repeatedly selecting the smallest (or largest) element from an unsorted portion of the list and moving it to the front. Below is a detailed explanation of how selection sort works, along with a Python implementation.
5) Peseant Multiply
   To implement the Russian Peasant Multiplication algorithm in Python, follow these steps. This method involves repeatedly halving one number and doubling another until the first number becomes 1. During this process, you sum the values of the second number whenever the first number is odd.
6) Maximum product of 2 integers
   This approach involves scanning through the array to identify the two largest and two smallest integers. The maximum product can then be calculated from these values.

   Steps:
      Initialize four variables: max1, max2 for the two largest numbers, and min1, min2 for the two smallest numbers.
      Traverse the array:
      Update max1 and max2 if a larger number is found.
      Update min1 and min2 if a smaller number is found.
      The maximum product will be the greater of:
      The product of the two largest numbers: 
      max1
      ×
      max2
      max1×max2
      The product of the two smallest numbers (in case both are negative): 
      min1
      ×
      min2
      min1×min2

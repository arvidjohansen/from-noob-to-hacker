# Algorithms

## What are algorithms?


An algorithm is a set of instructions for solving a problem or accomplishing a task. Each step in an algorithm is precise and unambiguous.

For example, let's consider a simple problem: finding the maximum number in a list of numbers. Here's a simple algorithm in Python:

1. Assume the first number in the list is the maximum number (max_num).
2. For each number in the list:
   - If the current number is greater than max_num, update max_num with the current number.
3. When you've gone through all the numbers, max_num will be the maximum number in the list.

Here's how you can write this algorithm in Python:

```python
def find_max(numbers):
    max_num = numbers[0]  # Step 1
    for num in numbers:   # Step 2
        if num > max_num:
            max_num = num
    return max_num        # Step 3

print(find_max([1, 2, 3, 4, 5]))  # Output: 5
```

Similarly, you can create a min algorithm by replacing `>` with `<` in the if condition. This will find the minimum number in the list.

----

## More advanced

An algorithm is a step-by-step procedure to solve a specific problem or to perform a specific task. In programming, an algorithm is a sequence of instructions that a program follows to transform input data into the desired output.

Here are a few examples of algorithms in Python:

1. **Linear Search Algorithm**: This algorithm sequentially checks each element of the list until it finds an element that matches the target value.

```python
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return None

numbers = [1, 2, 3, 4, 5]
print(linear_search(numbers, 3))  # Output: 2
```

2. **Bubble Sort Algorithm**: This is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.

```python
def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

numbers = [5, 3, 2, 4, 1]
print(bubble_sort(numbers))  # Output: [1, 2, 3, 4, 5]
```

3. **Binary Search Algorithm**: This search algorithm works on the principle of divide and conquer. For this algorithm to work properly, the data collection should be in the sorted form.

```python
def binary_search(lst, target):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

numbers = [1, 2, 3, 4, 5]
print(binary_search(numbers, 3))  # Output: 2
```

Remember, these are just simple examples. Real-world algorithms can be much more complex and can involve multiple data structures and complex logic.

---

## Exercises

Here are some exercises to practice algorithms:

1. **Reverse a String**

   Write a Python function that takes a string as input and returns the string reversed.

2. **Palindrome Checker**

   Write a Python function that checks whether a passed string is palindrome or not. (A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., 'madam')

3. **Fibonacci Sequence**

   Write a Python function that generates the Fibonacci sequence up to n. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

4. **Prime Number Checker**

   Write a Python function that takes a number as a parameter and checks if the number is prime or not.

5. **Sorting Algorithm**

   Implement a sorting algorithm in Python. It could be bubble sort, selection sort, insertion sort, etc.

6. **Binary Search**

   Implement the binary search algorithm in Python. This algorithm is used to efficiently find a target value within a sorted list of values.

7. **Factorial Calculator**

   Write a Python function that calculates the factorial of a number. The factorial of a number is the product of all positive integers less than or equal to the number.

Remember, the key to learning algorithms is practice. Try to solve these exercises on your own, but don't hesitate to look up solutions if you get stuck.

---


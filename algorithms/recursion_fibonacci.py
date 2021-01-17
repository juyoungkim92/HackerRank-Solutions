"""
Solving Fibonacci sequence problem using recursion.

"""


# normal Recursive algorithm
def fib(n):
    """
    Recursive way of solving nth fibonacci number.
    Fn = F(n-1) + F(n-2)
    """
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result


"""

Above code is very inefficient. O(2^n)
Because recursively we have to compute for all the repetitions.
It's not a big deal when working with small n but if the n is big, it is problem

How to optimize? 

We can use technique called Dynamic programming -> Memoization.
Memoization is an optimization technique to improve performance of recursive algorithms. 
This involves rewriting of recursive algorithm so that the returned values are stored in an array.
Recursive calls can look up results in the array rather than computing.
"""


# Recursion using memoization (dynamic programming)
def fib_memo(n, memo):
    """
    :param n: nth fibonacci number
    :param memo: an empty array
    """
    # if the array is not Null, means something is already computed, so just return
    if memo[n] is not None:
        return memo[n]

    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1, memo) + fib(n-2, memo)

    # store the computed value in a memo array
    memo[n] = result
    return result


def fib_wrap(n):
    """
    Wrapper function for fib
    """
    # len(memo) is always n + 1
    memo = [None] * (n + 1)
    return fib(n, memo)


"""
Now the time complexity T(n) = # of function calls * time for each call
No. of times Fib is called is at most (2n, in recursion) + 1 (first call)
(2n + 1) * O(1)
T(n) = (2n + 1) * O(1)
T(n) = (2n + 1)
T(n) = O(n) which is much better than normal recursive algorithm.

We can also use bottom_up approach, why don't we just build up the array instead of using recursion.
This is also useful because Python will throw recursive error due to too many recursion calls if the n is big.

Time complexity is again O(n) because define array and we are going through only once. 
  
"""


def fib_bottom_up(n):
    """
    Bottom up approach
    """
    if n == 1 or n == 2:
        return 1
    arr_bottom_up = [None] * (n + 1)
    arr_bottom_up[1] = 1
    arr_bottom_up[2] = 1

    # loop through from 3 to n+1
    for i in range(3, n+1):
        arr_bottom_up[i] = arr_bottom_up[i-1] + arr_bottom_up[i-2]

    return arr_bottom_up[n]

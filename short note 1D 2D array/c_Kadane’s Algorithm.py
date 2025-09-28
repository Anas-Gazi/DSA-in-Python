def maxSubarraySum(arr):
    """
    Finds the maximum sum of a contiguous subarray using Kadane's Algorithm.

    :param arr: List[int] - input array of integers
    :return: int - maximum subarray sum
    """
    if not arr:
        return 0  # handle empty array case

    res = arr[0]            # Maximum sum found so far
    maxEnding = arr[0]      # Max sum ending at current index

    for i in range(1, len(arr)):
        # Either extend the previous subarray or start a new one at arr[i]
        maxEnding = max(maxEnding + arr[i], arr[i])
        
        # Update result if current subarray sum is greater
        res = max(res, maxEnding)
        

    return res


# ✅ Example usage
if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    print("Input array:", arr)

    max_sum = maxSubarraySum(arr)

    print("Maximum subarray sum:", max_sum)

def rotateclockwise(arr, k):
    """
    Rotates the array 'arr' to the right by 'k' steps in-place.
    
    :param arr: List of elements to rotate
    :param k: Number of steps to rotate the array
    """
    n = len(arr)
    if n == 0:
        return

    # Handle cases where k > n
    k = k % n

    # Step 1: Reverse last k elements
    arr[n - k:] = reversed(arr[n - k:])

    # Step 2: Reverse first n - k elements
    arr[:n - k] = reversed(arr[:n - k])

    # Step 3: Reverse the entire array
    arr[:] = reversed(arr)

    # The original array is modified in-place


# ✅ Example usage
if __name__ == "__main__":
    # Input array and rotation count
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    print("Original array:", arr)
    
    rotateclockwise(arr, k)
    
    print(f"Array after rotating {k} steps to the right:", arr)

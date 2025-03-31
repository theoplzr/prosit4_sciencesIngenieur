def find_pair_hash_map(data, target):
    seen = set()  # Initialize a set to store numbers we've already seen

    # Iterate through each number in the list
    for num in data:
        complement = target - num  # Calculate the value needed to reach the target

        # If the complement is already in the set, we've found a valid pair
        if complement in seen:
            return (complement, num)

        # Otherwise, store the current number for future comparisons
        seen.add(num)

    # If no valid pair is found, return None
    return None

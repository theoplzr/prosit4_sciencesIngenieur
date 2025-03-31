def find_pair_brute_force(data, target):
    n = len(data)  # Get the total length of the input list

    # Iterate through each element in the list
    for i in range(n):

        # For each element data[i], check the following elements data[j]
        for j in range(i + 1, n):

            # If the sum of data[i] and data[j] equals the target, return the pair
            if data[i] + data[j] == target:
                return (data[i], data[j])

    # If no pair is found that adds up to the target, return None
    return None

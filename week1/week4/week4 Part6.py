def findTriplets(L):
    triplets = set()
    n = len(L)
    
    # Convert list to set for faster lookup
    L_set = set(L)
    
    for i in range(n):
        for j in range(i+1, n):
            # Calculate the third number needed to make sum zero
            third_number = -(L[i] + L[j])
            
            # Check if third number exists in the set and is not the same as i and j
            if third_number in L_set and third_number != L[i] and third_number != L[j]:
                # Add the triplet to the set
                triplet = tuple(sorted([L[i], L[j], third_number]))
                triplets.add(triplet)
    
    return triplets

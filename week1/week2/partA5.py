def mostFrequentDigit(n):

    digit_count = {i: 0 for i in range(10)}

    
    n_str = str(abs(n))

   
    for digit in n_str:
        digit_count[int(digit)] += 1

    
    max_count = max(digit_count.values())
    most_frequent_digit = min(digit for digit, count in digit_count.items() if count == max_count)

    return most_frequent_digit


print(mostFrequentDigit(12345))  
print(mostFrequentDigit(112233445566))  
print(mostFrequentDigit(-9876543210))  

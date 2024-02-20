def generate_palindromes(digits, length):
    result = []
    for i in range(1, length + 1):
        current_palindromes = []
        for d in digits:
            if i == 1:
                current_palindromes.append(d)
            elif i == 2:
                current_palindromes.append(d + d)
            elif i % 2 == 0:
                for palindrome in result[i - 3]:
                    current_palindromes.append(d + palindrome + d)
            else:
                for palindrome in result[i - 3]:
                    current_palindromes.append(d + palindrome + d)
        result.append(current_palindromes)
        print(f"Palindromes of length {i}: {', '.join(current_palindromes)}")


E = ["0", "1", "2"]

generate_palindromes(E, 5)

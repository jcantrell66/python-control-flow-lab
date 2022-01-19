# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

loop_count = 0
two_previous = 0
one_previous = 0
while loop_count < 50:
    if loop_count == 1:
        one_previous += 1
    current_term = two_previous + one_previous
    print(f'Term: {loop_count} / Number: {current_term}')
    two_previous = one_previous
    one_previous = current_term
    loop_count += 1
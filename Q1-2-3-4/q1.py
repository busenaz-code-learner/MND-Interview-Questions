
"""
The number of trailing zeros depends on the number of 10 factors in the factorial, and since 10 is the product of 2 and 5,
 we need to count how many 5 and 2 factors are in the factorial.
 However, there are usually more 2's than 5's, so counting the number of 5's is sufficient.
"""
def count_zeros(n):
    count = 0
    i = 5
    while num // i > 0:
        count += num // i
        i *= 5
    return count

# Input Part
while True:
    try:
        num = int(input("Enter a num: "))
        if num < 0:
            print("Please enter a positive num.")
        else:
            print(f"The last {count_zeros(num)} digits of the number {num}! are 0.")
            break 
    except ValueError:
        print("Enter a valid num")

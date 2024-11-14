
"""Counts the total occurrences of digit '3' and collects numbers containing '3'."""

def count_digit_3(n):
    list3 = [i for i in range(n + 1) if '3' in str(i)]  # List of numbers containing '3'
    total = sum(str(num).count('3') for num in list3)  # Toplam 3 içeren sayılar
    return total, list3

# Input part
while True:
    try:
        num = int(input("Enter a number: ")) 
        if num < 0:
            print("Please enter a positive number.")  
        else:
            count, list3 = count_digit_3(num)  # Get count and list of numbers with 3
            print(f"{list3},from 0 to {num}, there are a total of {count} occurrences of the digit 3.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")  

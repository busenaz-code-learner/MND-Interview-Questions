def add(a, b):
    while b != 0:  
        carry = a & b  # AND işlemi ile carry bitlerini bul.Eğer her iki bit 1 ise,sonuç daha yüksek bite eklemek için sola kaydır
        a = a ^ b        # XOR işlemi
        b = carry << 1  # Taşıma bitlerini sola kaydır

    return a

# Input part
a = int(input("Enter first num: "))
b = int(input("Enter second num: "))

print(f"Summation of {a} and {b} = {add(a, b)}")

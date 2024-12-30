#PerulanganFOR
for i in range(6):
    print(i)
    
for i in range(0,11,2):
    print(i)
    
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print("Total nilai:", total)


n = int(input("Masukkan jumlah angka Fibonacci: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b


number = int(input("Masukkan angka: "))
is_prime = True
for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break
if is_prime and number > 1:
    print(number, "adalah bilangan prima.")
else:
    print(number, "bukan bilangan prima.")

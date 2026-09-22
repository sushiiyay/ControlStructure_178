nilai = int(input("Masukkan nilai fibonacci"))

a = 0
b = 1

for i in range(nilai):
    print (a, end=" ")
    a, b = b, a + b
angka_a = float(input("Masukkan angka_a: "))
angka_b = float(input("Masukkan angka_b: "))
angka_c = float(input("Masukkan angka_c: "))

if angka_a > angka_b and angka_b > angka_c:
    terbesar = a
    print("Angka terbesar adalah:", terbesar)
elif angka_b > angka_a and angka_b > angka_c:
    terbesar = b
    print("Angka terbesar adalah:", terbesar)
elif angka_c > angka_a and angka_c > angka_b:
    terbesar = c
    print("Angka terbesar adalah:", terbesar)
else:
    print("Tidak ada angka terbesar")
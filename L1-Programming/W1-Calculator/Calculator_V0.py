print("===Simple Calculator===")
angka1 = int(input("Masukan angka pertama : "))
angka2 = int(input("masukan angka kedua :"))

if angka2 == 0 or angka1 == 0:
  print("angka tidak bisa 0 untuk pembagian dan modulus")
else:
  print("Hasil  dari", angka1, "/", angka2, "=", angka1 / angka2)
  print("Hasil  dari", angka1, "%", angka2, "=", angka1 % angka2)

print("Hasil  dari", angka1, "+", angka2, "=", angka1 +angka2)
print("Hasil  dari", angka1, "-", angka2, "=", angka1 - angka2)
print("Hasil  dari", angka1, "*", angka2, "=", angka1 * angka2)
print("Hasil  dari", angka1, "**", angka2, "=", angka1 ** angka2)

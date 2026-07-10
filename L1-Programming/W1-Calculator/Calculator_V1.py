while True:
    print("===Simple Calculator===")
 # Input angka pertam dan kedua
    try:
     angka1 = int(input("Masukkan angka pertama: "))
     angka2 = int(input("Masukkan angka kedua: "))
    except ValueError:
     print("Input harus berupa angka. Silahkan coba lagi.")
     continue
 # Input operator yang ingin digunakan
    operator = input("Masukkan operator (+, -, *, /, %, **): ")

    if operator not in ["+", "-", "*", "/", "%", "**"]:
     print("Operator tidak valid. silahkan masukan operator yang baru.")
     continue

 # Perhitugnan berdasarkan operator yang dipilih.
    if operator == "+":
     print("Hasil dari", angka1, "+", angka2, "=", angka1 + angka2)

    elif operator == "-":
     print("Hasil dari", angka1, "-", angka2, "=", angka1 - angka2)

    elif operator == "*":
     print("Hasil dari", angka1, "*", angka2, "=", angka1 * angka2)

    elif operator == "/":
     if angka2 == 0:
      print("Pembagian tidak dapat dengan 0")
     else:
      print("Hasil dari", angka1, "/", angka2, "=", angka1 / angka2)

    elif operator == "%":
     if angka2 == 0:
      print("Modulo tidak dapat dengan 0")
     else:
      print("Hasil dari", angka1, "%", angka2, "=", angka1 % angka2)

    elif operator == "**":
     print("Hasil dari", angka1, "**", angka2, "=", angka1 ** angka2)

 # Ulangin program jika user ingin mengulang
    while True:
     ulang = input("\nApakah anda ingin mengulang? (y/n): ").lower()

     if ulang == "y":
      break
     elif ulang == "n":
      exit("Terima kasih sudah menggunakan Simple Calculator.")
     else:
      print("Input tidak valid. Silahkan masukkan 'y' untuk mengulang atau 'n' untuk keluar.")
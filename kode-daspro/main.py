#RIZKY BAGAS QARAN
#2607805
#1C
#STUDI KASUS 1

#komentar dibawah ini adalah komentar yang menjelaskan tentang program yang dibuat untuk TUGAS LTIK
#tugasnya adalah menampilkan angka dari 1 sampai 50, 
#namun jika angka tersebut habis dibagi 5 maka akan menampilkan kata "PASS"
for i in range(1, 51):
    if i % 5 == 0:
        print("PASS")
    else:
        print(i)

#RIZKY BAGAS QARAN
#2607805
#1C
#STUDI KASUS 2

jumlah_hewan = int(input("MASUKKAN JUMLAH HEWAN YANG AKAN DI INPUT: "))
hewan = []
for i in range(jumlah_hewan):
    hewan.append(input(f"HEWAN KE-{i+1}: "))
for i in range(len(hewan)):
    print(f"HEWAN KE-{i+1}: {hewan[i]}")

#RIZKY BAGAS QARAN
#2607805
#1C
#STUDI KASUS 3

n = int(input("MASUKKAN JUMLAH BILANGAN: "))
angka = []
for i in range(n):
    angka.append(int(input(f"MASUKKAN BILANGAN KE-{i+1}: ")))
for bilangan in angka:
    if bilangan % 2 == 0:
        print(f"{bilangan} ADALAH BILANGAN GENAP")
    else:
        print(f"{bilangan} ADALAH BILANGAN GANJIL")

#RIZKY BAGAS QARAN
#2607805
#1C
#STUDI KASUS 4

for i in range(1, 81):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

#RIZKY BAGAS QARAN
#2607805
#1C
#STUDI KASUS 5

username = "dasproRPL"
password = "RPL123!"
username_input = input("MASUKKAN USERNAME: ")
password_input = input("MASUKKAN PASSWORD: ")
if username == username_input and password == password_input:
    print("LOGIN BERHASIL")
else:
    print("PASSWORD/USERNAME SALAH")
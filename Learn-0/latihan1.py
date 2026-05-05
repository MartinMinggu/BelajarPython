# latihan satu: cek bilangan ganjil atau genap
# angka = int(input("masukan angka: "))
# if angka%2 == 0:
#     print(f"{angka} adalah bilangan genap")
# else:
#     print(f"{angka} adalah bilangan ganjil")


# latihan dua : hitung total dari list 
# angka = [10,20,30,40]
# result = 0
# for x in angka:
#     result += x
# print(f"totalnya adalah {result}")

# latihan 3 : hitung huruf vokal
# vokal = ["a", "i", "u", "e", "o"]
# kata = input("masukan kata: ").lower();
# result = 0
# for huruf in kata:
#     if huruf in vokal:
#         result+= 1
# print(f"jumlah huruf vokal adalah {result}")

# latihan 4: dictionary sederhana
# person = {
#     "nama" : "Budi",
#     "umur" : 20
# }

# print(person["nama"])
# print(person["umur"])

# latihan 6 : error handling
# try :
#     angka = int(input("masukan angka: "))
#     result = 10/angka
#     print(f"hasil {result}")
# except ZeroDivisionError:
#     print("tidak bisa dibagi nol")
# except:
#     print("input tidak valid")


# latihan 7: sistem login sederhana

# users = {
#     "admin" : "123",
#     "budi" : "abc"
# }

# nama = input("masukan nama: ")
# password = input("masukan password: ")


# if nama in users and users[nama] == password:
#     print(f"{nama} berhasil login")
# else:
#     print("login gagal")


# latihan 8 : tebak angka game
# import random
# angka_rahasia = random.randint(1,100);
# prev_tebakan_max = 100;
# prev_tebakan_min = 0;
# while True:

#     tebakan = int(input(f"masukan angka ({prev_tebakan_min}-{prev_tebakan_max}): "))
#     if tebakan < angka_rahasia:
#         print("tebakan anda lebih kecil")
#         prev_tebakan_min = tebakan
#     elif tebakan > angka_rahasia:
#         print("tebakan anda lebih besar")
#         prev_tebakan_max = tebakan
#     else:
#         print("tebakan anda benar")
#         break

# latihan 9: sistem login sederhana
# users ={}
# with open("users.txt", "r")as f:
#     for line in f:
#         username, password = line.strip().split(",")
#         users[username] = password
# username = input("masukan username: ") 
# password = input("masukan password: ") 
# if username in users and users[username] == password:
#     print(f"login berhasil sebagai {username}")
# else:
#     print("login gagal")

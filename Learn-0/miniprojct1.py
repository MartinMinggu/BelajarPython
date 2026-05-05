# todos = []
# with open("todos.txt", "r") as f:
#     for line in f:
#         cleaned_line = line.strip()
#         if cleaned_line:
#             todos.append(cleaned_line)
# print("initial todos")
# print(todos)
# print("end todos")
# while True:
#     print("\n1.Tambah\n2.Lihat\n3.Keluar dan simpan\n4.delete semua data\n5.delete satu data by indeks")
#     pilih = input("pilih: ")
#     if pilih=="1":
#         tugas = input("masukan tugas: ")
#         todos.append(tugas);
#     elif pilih == "2":
#         for i, t in enumerate(todos):
#             print(i+1, ".", t)
#     elif pilih == "3":
#         with open("todos.txt", "w")as f:
#             for i, t in enumerate(todos):
#                 f.write(f"{t}\n")    
#             break
#     elif pilih == "4":
#         todos = []
#         with open("todos.txt", "w")as f:
#             for i, t in enumerate(todos):
#                 f.write(f"{t}\n")
#     elif pilih == "5":
#         indeks = int(input("masukan indeks: "))
#         todos.pop(indeks)



def get_users_data_from_file():
    users ={}
    try:
        with open("users.txt","r") as f:
            for line in f:
                username, password = line.strip().split(",")
                users[username] = password
    except FileNotFoundError:
        pass
    return users


def save_users_data_to_file(users):
    try:
        with open("users.txt","w") as f:
            for username, password in users.items():
                f.write(f"{username},{password}\n")
            print("data berhasil di simpan")
    except Exception as e:
        print(f"terjadi kesalahan {e}")


users = get_users_data_from_file();
while True:
    print("Pilih\n1.login\n2.register")
    try:
        pilihan_aplikasi =  int(input("pilihanmu: "))
    except ValueError:
        print("input harus angka")
        exit()
    if pilihan_aplikasi == 1:
        username = input("masukan username: ")
        password = input("masukan password: ")
        if username in users and users[username] == password:
            print(f"{username} berhasil login")
        else:
            print(f"{username} gagal login")
    elif pilihan_aplikasi == 2:
        username = input("masukan username: ")
        password = input("masukan password: ")
        if username in users:
            print("ussername sudah terdaftar")
        else:
            users[username] = password
            save_users_data_to_file(users)

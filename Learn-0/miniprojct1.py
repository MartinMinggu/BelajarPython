todos = []
with open("todos.txt", "r") as f:
    todos.append(f.read())
while True:
    print("\n1.Tambah\n2.Lihat\n3.Keluar dan simpan\n4.delete semua data")
    pilih = input("pilih: ")
    if pilih=="1":
        tugas = input("masukan tugas: ")
        todos.append(tugas);
    elif pilih == "2":
        for i, t in enumerate(todos):
            print(i+1, ".", t)
    elif pilih == "3":
        with open("todos.txt", "w")as f:
            for i, t in enumerate(todos):
                f.write(f"{t}\n")    
            break
    elif pilih == "4":
        todos = []
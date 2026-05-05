todos = []
with open("todos.txt", "r") as f:
    for line in f:
        cleaned_line = line.strip()
        if cleaned_line:
            todos.append(cleaned_line)
print("initial todos")
print(todos)
print("end todos")
while True:
    print("\n1.Tambah\n2.Lihat\n3.Keluar dan simpan\n4.delete semua data\n5.delete satu data by indeks")
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
        with open("todos.txt", "w")as f:
            for i, t in enumerate(todos):
                f.write(f"{t}\n")
    elif pilih == "5":
        indeks = int(input("masukan indeks: "))
        todos.pop(indeks)
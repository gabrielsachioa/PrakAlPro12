n = int(input("Masukkan jumlah kategori: "))

aplikasi = {}
for i in range(n):

    kategori = str(input(f"Masukkan nama kategori ke-{i+1}: "))
    set_app = set()

    for j in range(5):
        inputan_app = str(input(f'\tMasukkan nama aplikasi ke-{j+1}: '))
        set_app.add(inputan_app)
        
    aplikasi[kategori] = set_app

list_kategori = []
for kategori in aplikasi:
    list_kategori.append(aplikasi[kategori])

hasil = list_kategori[0]
for k in range(1, len(list_kategori)):
    hasil = hasil.intersection(list_kategori[k])

hasil2 = list_kategori[0]
for l in range(1, len(list_kategori)):
    hasil2 = hasil2.symmetric_difference(list_kategori[l])

print(f"Kategori yang muncul semua: {hasil}")
print(f"Kategori yang muncul 1 kali: {hasil2}")
if n > 2:
    hasil3 = list_kategori[0]
    tmp = list_kategori[1]
    for m in range(1, len(list_kategori)):
        hasil3 = hasil3.symmetric_difference(list_kategori[m])
    print(f"Kategori yang muncul 2 kali: {hasil3}")
else:
    print("Kategori yang muncul 2 kali tidak ada")
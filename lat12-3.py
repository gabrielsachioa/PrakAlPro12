input1 = input("Masukkan file pertama: ")
input2 = input("Masukkan file kedua: ")

try:
    with open(input1, 'r') as f1, open(input2, 'r') as f2:
        file1 = f1.read().lower()
        file2 = f2.read().lower()
        
        file1 = file1.split()
        file2 = file2.split()

        file1 = set(file1)
        file2 = set(file2)
      
        hasil = file1.intersection(file2)
        print(f"Kata yang muncul di kedua file: {hasil}")
except:
    print("File tidak ditemukan")
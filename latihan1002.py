#Membuat perulangan For dengan list

for i in [1,2,3,4,5]:
    print("Ini pengulangan ke - ",i)

#Membuat perulangan For dengan isi string(tulisan)

for i in ["Rawon", "Nasi Kuning", "Soto Madura", "Kupat Tahu", "Kerak Telor", "Rendang Batoko", "Pempek Selam", "Ayam Betutu"] :
    print(i, "adalah masakan khas nusantara")

#Membuat perulangan For dengan String

for i in ["a", "b", "c", "d", "e"]:
    print(i, "adalah alfabet")

#Membuat Perulangan While
i=1
while i <=5:
    print(i)
    i=i+1
print("Program Selesai")


#Menghitung Rata-rata dari sejumlah nilai
print("PROGRAM PYTHON MENGHITUNG NILAI RATA-RATA")

banyakdata = 5
i = 0
print()

jum = 0
while i < 5 :
    nilai = int(input("Masukkan data ke-%d: " % (i+1)))
    i = i + 1
    jum = jum + nilai
    rata = jum/banyakdata
print("\nRata-rata = %0.2f" % rata)


#Menampilkan deretan bilangan ganjil
for g in range(1,16,2):
    print(g)

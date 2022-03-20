# soal 
# buatlah contoh codingan colecctions (List,Tuple,Set,Dictionary)
# isilah masing masing collections tersebut dengan beberapa value /nilai kemudian tampilakan menggunakan perulangan.
# cobalah update salah satu value /nilai dari masing-masing collections tersebut ,jelaskan apa yang terjadi 
#coba hapus salah satu nilai/value dari masing masing collections apa yang terjadi .
# cobalah tambahkan value ke masing masing colecctions tersebut ,jelaskn apa yang terjadi.
print("#" * 50)
print("data List")
data_list=["lisa","inayah","awal","luppi"]
print("kegiatan pertama")
print(" update data menggunakan perulangan for")
for i in data_list:
    print(i)
print("update data menggunakan perulangan while")
i=0
while i < 4:
    print(data_list[i])
    i+=1
print("kegiatan ke dua")
data_list[0] = "nurul"# uodate nilai/velue dalam data list
print(data_list)
print("kegiatan ke 3")
print(data_list)
data_list.remove("awal")# penghapus nilai/value dalam data list 
print("kegiatan ke 5")
print(data_list)
data_list.append("dina") #menabahkan nilai/value dalam data list
print(data_list)
data_list.insert(3,"ani")# menambahkan nilai/value dengan menentukan indeks yang kita mau
print(data_list)
print("#"*50)
print("data Tuple")
print("kegiatan pertama")
data_tuple=(10,3,20,2,5,7)
print(" update data menggunakan perulangan for")
for i in data_tuple:
    print(i)
print("update data menggunakan perulangan while")
i=0
while i < 6:
    print(data_tuple[i])
    i+=1
print("kegiatan ke dua ")
# didalam python tuple adalah salah satu data berkelompok yang niali elemen elemenya tidak dapat diubah.
# jumlah elemen di dalam tuple juga tidak dapat di tambah atau di hapus , oleh karena itu apabila 
# kita ingin mengubah data dari data tuple akan mengakibatkan outputnya akan eror 
print("kegiatan ke 3,4 dan 5")
print("hasil yang  di hasilkan akan eror krn data tuple tidak dapat di ubah nilai elemen dari data")
print("#"*50)
print("data set")
print("kegiatan pertama")
data_set={"nurul","naya",10,3,20}
print("kegiatan ke 2")
print(" update data menggunakan perulangan for")
for i in data_set:
    print(i)
print("update data menggunakan perulangan while")
i=0
while i < 1:
    print(data_set)
    i+=1 
print("kegiatan ke 3")
#di dalam data set objeknya tidak dapat diindeks maksudnya kita tdk dapat mengakses indeks dari data set
#tidak ada metode khusus yang digunakan untuk mengani keperluan ini.Namun, kita dapat menggunakan teknik di bawah ini
# untuk mengubah nilai dari sutu elemen di dalam set.
data_set={"nurul","naya",10,3,20}
print(data_set)
data_set.discard(20)
data_set.add(50)
print(data_set)
print("kegiatan ke 4")
data_set.discard("naya")
print(data_set)
# data_set.clear() di gunakan apbila kita ingin mengosongkan atau mengapus semua elemen  yang terdapat dalam set
print("kegiatan ke 5")
data_set.add(45)
print(data_set)
print("#"*50)
print("data dictionary")
print("kegiatan pertama")
data_dictionary={
    "nama": "nurul inayah",
    "fakultas":"teknik informatika",
    "kelas":"informatika G" }
print("kegiatan ke 2")
print("update data menggunakan perulangan while")
i=0
while i < 1:
    print(data_dictionary)
    i+=1
print("kegiatan ke 3")
data_dictionary["nama"]="suryandini"
print(data_dictionary)
print("kegiatan ke 4")
data_dictionary["alamat"]="kelurahan tande"
print(data_dictionary)
print("kegiatan ke 5")
del data_dictionary ["kelas"]
print(data_dictionary)
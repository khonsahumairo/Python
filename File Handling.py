file = open("data.txt", "w")
file.write("Halo, Semangat ulangan \nFisika nya!!!")
file.close

file = open("data.txt", "r")
print("isi file:")
print(file.read())
file.close()

#menambahkan isi baru ke file
file = open("data.txt", "a")
file.write("baris tambahan di file.\n") #\n itu utk menambahkan baris baru
file.close()

#membaca ulang isi file stlh ditambahkan
file = open("data.tx", "r")
print("isi file terbaru:")
print(file.read())
file.close()

#kenapa kita hrs belajar ttg file handling?
#file handling ini digunakan utk menyimpan data scr permanen walaupun program
#disebut working directory

#TUGAS FILE HANDLING----------------------------------------------------------

file = open("Biodata.txt", "w")
file.write("Nama : Khonsa \nHobi : Menulis, Menggambar, Memotret gambar \nTempat lahir : Bogor \nPengalaman ku selama belajar coding tuh moment yang pertamakali bgt aku belajar dan akhirnya aku jadi tau banyak hal tentang pemrograman yang ada di komputer. \nMulai dari membuat aplikasi sederhana sampai bahasa pemrograman lainnya. jujur awal awal aku kyk bingung ama coding tuh ngapain. tapi pas terus menerus diikuti jadi seru juga")
file.close()

file = open("data.txt", "r")
print("isi file:")
print(file.read())
file.close()


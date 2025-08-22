#buat lambda
lambda name : print("selamat datang", name)
#buat lambda dlm variabel
sayHello = lambda name : print("selamat datang", name)
#variable sayhello sudah jd function
sayHello("Malla")
#lambda tanpa argumen
(lambda : print("selamat datang"))()
#lambda dgn argumen
(lambda name : print("selamat datang", name))("Ravell")
#Lambda dgn default argumen
(lambda name="" : print("selamat datang"))()

#latihan 1 
#mendefinisikan fungsi lambda utk kuadrat
kuadrat = lambda x: x ** 2
#memanggil fungsi lambda dgn argumen 5
hasil = kuadrat(5)
print(hasil)

angka = [1, 2, 3, 4, 5]
hasil_kuadrat = list(map(lambda x: x ** 2, angka))
print(hasil_kuadrat)

#latihan 2
#applied
belanja = [12000, 5000, 30000, 8000]
hasil = list(filter(lambda x: x>=10000, belanja))
print(hasil)
def sayHello():
    print("Selamat Datang")

sayHello()

#kata kunci return
def sayHello():
    return "Selamat Datang"

print (sayHello()) #lbh bagus print aja langsung, biar gsh return dlu

#function argument
def sayHello(name):
    return "Selamat Datang " + name

print(sayHello("Budiarjo"))

#tambah argumen lebih dari satu
def addition(num1 , num2):
    result = num1 + num2
    print(num1,"+" ,num2, "=", result)

addition(15,16)


#menerapkan default argument yang sudah memiliki argumen bawaan\
def sayHello(name=""):
    return "Selamat Datang" + name

#menjalankan function tanpa argumen (lagi)
print(sayHello())
#bisa

#function keywords argument
def fullname(fname, lname=""):
    return fname+" "+lname

print(fullname(lname="antonio", fname="budiarjo"))


#*args
def addition(*numbers):
    result = 0
    for n in numbers :
        result += n
    
    return result

#*kwargs
def fullname(**kwargs):
    values= kwargs.values()
    print(" ".join(values))

fullname(a="Ahmad", b="Dwi", c="santoso")
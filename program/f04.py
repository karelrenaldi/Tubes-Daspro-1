import b01 as skc
import f01 as load
import fileAcces as fa


def signUp():
    found = False
    registered = False
    i = 0
    while (registered == False):
        nama = input("Masukkan nama: ")
        tanggalLahir = input("Tanggal lahir(DD/MM/YYYY): ")
        tinggiBadan = int(input("Masukkan tinggi badan pemain(cm): "))
        username = input("Masukkan username pemain: ")
        password = input("Masukkan password pemain: ")
        while (i < fa.getLength(load.user, load.markUser) and found == False):
            if(load.user[i][3] == username):
                found = True
                print("username sudah terdaftar")
            i += 1
        if (found == False):
            registered = True
        else:
            found = False
    load.user[fa.getLength(load.user, load.markUser)] = [nama, tanggalLahir, tinggiBadan, username, skc.encrypt(password), 'pemain', 0, 'regular']
    print("Akun telah didaftarkan")

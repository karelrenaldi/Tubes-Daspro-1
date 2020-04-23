import f01 as load
import fileAcces as fa


def goldAccount():
    found = False
    username = input("Masukkan username yang ingin di-upgrade: ")
    for i in range(fa.getLength(load.user, load.markUser)):
        if(load.user[i][3] == username):
            if(int(load.user[i][6]) >= 1500):
                load.user[i][7] = "golden"
                load.user[i][6] = int(load.user[i][6])-1500
                found = True
                print("Akun anda telah di upgrade")
            else:
                print("Saldo anda tidak cukup")
    if (found == False):
        print("Username salah atau akun belum terdaftar !")

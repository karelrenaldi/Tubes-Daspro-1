import f01 as load
import fileAcces as fa


def topup():
    username = input("Masukkan username: ")
    money = int(input("Masukkan saldo yang di top-up: "))
    for i in range(fa.getLength(load.user, load.markUser)):
        if(load.user[i][3] == username):
            load.user[i][6] = int(load.user[i][6]) + money
            print("Top up berhasil. Saldo {} bertambah menjadi {}".format(username, load.user[i][6]))

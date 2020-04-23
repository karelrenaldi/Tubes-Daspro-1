import csv
import f01 as load
import b01 as skc
import fileAcces as fa


def login():
    res = ["", ""]
    i = 0
    found = False
    username = input('Masukkan username: ')
    password = skc.encrypt(input("Masukkan password: "))
    while (i < fa.getLength(load.user, load.markUser) and found == False):
        if(load.user[i][4] == password and load.user[i][3] == username):
            print("Anda terdaftar")
            found = True
            res = [load.user[i][3], load.user[i][5]]
        i += 1
    if(found == False):
        print("Tidak terdaftar")
    return(res)

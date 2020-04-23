import fileAcces as fa
import f01 as load


def search():
    found = False
    i = 0
    username = input("Masukkan username: ")
    while (i < fa.getLength(load.user, load.markUser) and found == False):
        if(username == load.user[i][3]):
            print('Nama Pemain: ', load.user[i][0])
            print('Tinggi Pemain: ', load.user[i][2])
            print('Tanggal Lahir Pemain: ', load.user[i][1])
            found = True
        i += 1
    if (found == False):
        print("Pencarian tidak ditemukan!!")

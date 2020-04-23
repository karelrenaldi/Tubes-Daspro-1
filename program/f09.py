import csv
import f01 as load
import fileAcces as fa


def refund(username):
    wahanaPrice = 0
    found = False
    i = 0
    idWahana = input("Masukkan ID wahana: ")
    ticket = int(input("Jumlah tiket yang di-refund: "))
    today = input("Masukkan tanggal hari ini (DD/MM/YYYY): ")
    print(fa.getLength(load.kepemilikan, load.markKepemilikan))
    for i in range(fa.getLength(load.wahana, load.markWahana)):
        if load.wahana[i][0] == idWahana:
            wahanaPrice = int(load.wahana[i][2])
    i = 0
    while(i < fa.getLength(load.kepemilikan, load.markKepemilikan) and found == False):
        if(load.kepemilikan[i][0] == username and load.kepemilikan[i][1] == idWahana and ticket <= int(load.kepemilikan[i][2])):
            load.kepemilikan[i][2] = int(load.kepemilikan[i][2]) - ticket
            load.refund[fa.getLength(load.refund, load.markRefund)] = [
                username, today, idWahana, ticket]
            found = True
        i += 1

    if(found == True):
        for i in range(fa.getLength(load.user, load.markUser)):
            if(load.user[i][3] == username):
                load.user[i][6] = int(load.user[i][6]) + int(wahanaPrice*0.5*ticket)
                print("Uang refund sudah kami berikan pada akun Anda.")
    else:
        print("Anda tidak memiliki tiket terkait.")

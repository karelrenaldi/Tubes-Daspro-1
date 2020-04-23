import f01 as load
import fileAcces as fa


def laporanKehilangan():
    lost = False
    username = input("Masukkan username: ")
    date = input("Tanggal kehilangan tiket: ")
    idWahana = input("ID wahana: ")
    ticket = int(input("Jumlah tiket yang dihilangkan: "))
    i = 0
    while(lost == False and i < fa.getLength(load.kepemilikan, load.markKepemilikan)):
        if(load.kepemilikan[i][0] == username and load.kepemilikan[i][1] == idWahana and int(load.kepemilikan[i][2]) >= ticket):
            load.kepemilikan[i][2] = int(load.kepemilikan[i][2]) - ticket
            load.kehilangan[fa.getLength(load.kehilangan, load.markKehilangan)] = [username, date, idWahana, ticket]
            lost = True
    if(lost == False):
        print("Masukkan anda tidak diterima")

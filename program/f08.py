import csv
import f01 as load
import fileAcces as fa


def play(username):
    found = False
    i = 0
    idWahana = input("Masukkan ID wahana: ")
    today = input("Masukkan tanggal hari ini(DD/MM/YYYY): ")
    ticket = int(input("Masukkan jumlah tiket yang digunakkan: "))
    
    while(i < fa.getLength(load.kepemilikan, load.markKepemilikan) and found == False):
        if(load.kepemilikan[i][0] == username):
            if(load.kepemilikan[i][1] == idWahana):
                if(int(load.kepemilikan[i][2]) >= ticket):
                    load.kepemilikan[i][2] = int(
                        load.kepemilikan[i][2]) - ticket
                    j = 0
                    found1 = False
                    row = 0
                    while (j < fa.getLength(load.penggunaan, load.markPenggunaan) and found1 == False):
                        if (load.penggunaan[j][0] == username and load.penggunaan[j][1] == today and load.penggunaan[i][2] == idWahana):
                            found1 = True
                            row = j
                        j += 1
                    if(found1):
                        load.penggunaan[row][3] = int(load.penggunaan[row][3]) + ticket
                    else:
                        load.penggunaan[fa.getLength(load.penggunaan, load.markPenggunaan)] = [username, today, idWahana, ticket]
                    found = True
        i += 1
        
    if(found):
        print("Terimakasih telah bermain")
    else:
        print("Tiket anda tidak valid dalam sistem kami")

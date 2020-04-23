import f01 as load
import fileAcces as fa


def getAge(username, today):
    hasBirthday = False
    todayDate = int(today[0:2])
    todayMonth = int(today[3:5])
    todayYear = int(today[6:10])
    today = today.split("/")
    for i in range(fa.getLength(load.user, load.markUser)):
        if(load.user[i][3] == username):
            birth = load.user[i][1]

    birthDate = int(birth[0:2])
    birthMonth = int(birth[3:5])
    birthYear = int(birth[6:10])
    ageMax = todayYear - birthYear

    if(todayMonth > birthMonth):
        hasBirthday = True
    elif(birthMonth == todayMonth):
        if(todayDate >= birthDate):
            hasBirthday = True

    if(hasBirthday == True):
        return ageMax
    else:
        return ageMax-1


def buyTicket(username):
    permission1 = False
    permission2 = True
    dataWahana = ['', '', 0, 0, 0]
    for i in range(fa.getLength(load.user, load.markUser)):
        if(load.user[i][3] == username):
            userHeight = int(load.user[i][2])
            saldo = int(load.user[i][6])

    idWahana = input("Masukkan ID wahana: ")
    today = input("Masukkan tanggal hari ini (DD/MM/YYYY): ")
    ticket = int(input("Masukkan jumlah tiket yang dibeli: "))
    for i in range(fa.getLength(load.wahana, load.markWahana)):
        if(load.wahana[i][0] == idWahana):
            dataWahana[0] = load.wahana[i][0]
            dataWahana[1] = load.wahana[i][1]
            dataWahana[2] = int(load.wahana[i][2])
            dataWahana[3] = load.wahana[i][3]
            dataWahana[4] = load.wahana[i][4]

    if(dataWahana[4] == ">=170"):
        if(dataWahana[3] == "dewasa"):
            if(userHeight >= 170 and getAge(username, today) >= 17):
                permission1 = True
        elif(dataWahana[3] == "anak-anak"):
            if(userHeight >= 170 and getAge(username, today) < 17):
                permission1 = True
        else:
            if(userHeight >= 170):
                permission1 = True
    else:
        if(dataWahana[3] == "dewasa"):
            if(getAge(username, today) >= 17):
                permission1 = True
        elif(dataWahana[3] == "anak-anak"):
            if(getAge(username, today) < 17):
                permission1 = True

    if(permission1 == True):
        for i in range(fa.getLength(load.user, load.markUser)):
            if(load.user[i][3] == username):
                if(load.user[i][7] != "golden"):
                    if(dataWahana[2]*ticket > saldo):
                        permission2 = False
                else:
                    if(dataWahana[2]*ticket*0.5 > saldo):
                        permission2 = False

    if(permission1 == True and permission2 == True):
        # update data pembelian
        load.pembelian[fa.getLength(load.pembelian, load.markPembelian)] = [
            username, today, idWahana, ticket]
        # update data user
        for i in range(fa.getLength(load.user, load.markUser)):
            if(load.user[i][3] == username):
                if(load.user[i][7] != "golden"):
                    load.user[i][6] = int(saldo - ticket*dataWahana[2])
                else:
                    load.user[i][6] = int(saldo - ticket*dataWahana[2]*0.5)
        # update data kepemilikan
        updated = False
        for i in range(fa.getLength(load.kepemilikan, load.markKepemilikan)):
            if(load.kepemilikan[i][0] == username and load.kepemilikan[i][1] == idWahana):
                load.kepemilikan[i][2] = int(load.kepemilikan[i][2]) + ticket
                updated = True
        if (updated == False):
            load.kepemilikan[fa.getLength(load.kepemilikan, load.markKepemilikan)] = [username, idWahana, ticket]

        print("Selamat bersenang senang di ", dataWahana[1], ".")
    else:
        if permission1 == False:
            print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.")
            print("Silakan menggunakan wahana lain yang tersedia.")
        else:
            print("Saldo Anda tidak cukup")
            print("Silakan mengisi saldo Anda")

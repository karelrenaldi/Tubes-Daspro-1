import f01 as load
import fileAcces as fa


def tiketPemain():
    username = input("Masukkan username: ")
    for i in range(fa.getLength(load.kepemilikan, load.markKepemilikan)):
        if(load.kepemilikan[i][0] == username):
            for j in range(fa.getLength(load.wahana, load.markWahana)):
                if(load.wahana[j][0] == load.kepemilikan[i][1]):
                    print(' {}\t| {}\t| {}'.format(load.kepemilikan[i][1], load.wahana[j][1], load.kepemilikan[i][2]))

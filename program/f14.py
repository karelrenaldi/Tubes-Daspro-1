import f01 as load
import fileAcces as fa


def history():
    idWahana = input("Masukkan id wahana: ")
    print("Riwayat:")
    for i in range(fa.getLength(load.penggunaan, load.markPenggunaan)):
        if load.penggunaan[i][2] == idWahana:
            print('{}\t|{}\t|{}'.format(load.penggunaan[i][1], load.penggunaan[i][0], load.penggunaan[i][3]))

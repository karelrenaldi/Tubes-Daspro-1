import fileAcces as fa
import f01 as load


def searchWahana():
    res = 0
    print('''
    Jenis batasan umur:
    1. Anak - anak (<17 tahun)
    2. Dewasa (>=17 tahun)
    3. Semua umur

    Jenis batasan tinggi badan:
    1. Lebih dari 170 cm
    2. Tanpa batasan
    ''')
    umur = input("Batasan umur pemain: ")
    while (umur != "1" and umur != "2" and umur != "3"):
        print("Batasan umur tidak valid!")
        umur = input("Batasan umur pemain: ")
    if(umur == "1"):
        umur = "anak-anak"
    elif(umur == "2"):
        umur = "dewasa"
    else:
        umur = "semua umur"
    tinggi = input("Batasan tinggi badan: ")
    while (tinggi != "1" and tinggi != "2"):
        print("Batasan tinggi badan tidak valid!")
        tinggi = input("Batasan tinggi badan: ")
    if(tinggi == "1"):
        tinggi = ">=170"
    else:
        tinggi = "tanpa batasan"
    print("Hasil pencarian: ")
    for i in range(fa.getLength(load.wahana, load.markWahana)):
        if(load.wahana[i][3] == umur and load.wahana[i][4] == tinggi):
            print(load.wahana[i][0], "|", load.wahana[i][1], "|", load.wahana[i][2])
            res += 1
    if(res == 0):
        print("Tidak ada wahana yang sesuai dengan pencarian kamu")

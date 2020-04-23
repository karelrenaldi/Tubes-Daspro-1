import f01 as load
import fileAcces as fa


def tambahWahana():
    print("Masukkan Informasi Wahana yang ditambahkan:")
    idWahana = input("Masukkan ID Wahana: ")
    namaWahana = input("Masukkan Nama Wahana: ")
    hargaTiket = input("Masukkan Harga Tiket: ")
    print("pilihan umur: dewasa, anak-anak, semua umur")
    umur = input("Masukkan batasan umur: ")
    print("pilihan tinggi: tanpa batasan, >=170")
    tinggi = input("Masukkan batasan tinggi badan: ")
    load.wahana[fa.getLength(load.wahana, load.markWahana)] = [idWahana, namaWahana, hargaTiket, umur, tinggi]

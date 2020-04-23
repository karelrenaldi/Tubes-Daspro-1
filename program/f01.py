import csv
import fileAcces as fa


def load():
    global user, markUser
    global wahana, markWahana
    global pembelian, markPembelian
    global penggunaan, markPenggunaan
    global kepemilikan, markKepemilikan
    global refund, markRefund
    global kriksar, markKriksar
    global kehilangan, markKehilangan

    fileUser = input("Masukkan nama File User: ")
    markUser = ['', '', 0, '', '', '', 0, '']
    user = fa.load(fileUser, markUser)

    fileDaftarWahana = input("Masukkan nama File Daftar Wahana: ")
    markWahana = ['', '', 0, 0, '']
    wahana = fa.load(fileDaftarWahana, markWahana)

    filePembelianTiket = input("Masukkan nama File Pembelian Tiket: ")
    markPembelian = ['', '', '', 0]
    pembelian = fa.load(filePembelianTiket, markPembelian)

    filePenggunaanTiket = input("Masukkan nama File Penggunaan Tiket: ")
    markPenggunaan = ['', '', '', 0]
    penggunaan = fa.load(filePenggunaanTiket, markPenggunaan)

    fileKepemilikanTiket = input("Masukkan nama File Kepemilikan Tiket: ")
    markKepemilikan = ['', '', 0]
    kepemilikan = fa.load(fileKepemilikanTiket, markKepemilikan)

    fileRefundTiket = input("Masukkan nama File Refund Tiket: ")
    markRefund = ['', '', '', 0]
    refund = fa.load(fileRefundTiket, markRefund)

    fileKritikSaran = input("Masukkan nama File Kritik dan Saran: ")
    markKriksar = ['', '', '', '']
    kriksar = fa.load(fileKritikSaran, markKriksar)

    fileKehilangan = input("Masukkan nama File Kehilangan Tiket: ")
    markKehilangan = ['', '', '', 0]
    kehilangan = fa.load(fileKehilangan, markKehilangan)

    print("File perusahaan Willy Wangky’s Chocolate Factory telah di-load.")

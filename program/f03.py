import csv
import fileAcces as fa
import f01 as load


def save():
    fileUser = input("Masukkan nama File User: ")
    fa.save(fileUser, load.user, load.markUser)
    fileDaftarWahana = input("Masukkan nama File Daftar Wahana: ")
    fa.save(fileDaftarWahana, load.wahana, load.markWahana)
    filePembelianTiket = input("Masukkan nama File Pembelian Tiket: ")
    fa.save(filePembelianTiket, load.pembelian, load.markPembelian)
    filePenggunaanTiket = input("Masukkan nama File Penggunaan Tiket: ")
    fa.save(filePenggunaanTiket, load.penggunaan, load.markPenggunaan)
    fileKepemilikanTiket = input("Masukkan nama File Kepemilikan Tiket: ")
    fa.save(fileKepemilikanTiket, load.kepemilikan, load.markKepemilikan)
    fileRefundTiket = input("Masukkan nama File Refund Tiket: ")
    fa.save(fileRefundTiket, load.refund, load.markRefund)
    fileKritikSaran = input("Masukkan nama File Kritik dan Saran: ")
    fa.save(fileKritikSaran, load.kriksar, load.markKriksar)
    fileKehilangan = input("Masukkan nama File Kehilangan Tiket: ")
    fa.save(fileKehilangan, load.kehilangan, load.markKehilangan)

import f01 as load
import fileAcces as fa


def kritikDanSaran(username):
    idWahana = input("Masukkan ID Wahana: ")
    today = input("Masukkan tanggal pelaporan (DD/MM/YYYY): ")
    kritikSaran = input("Kritik/saran Anda: ")
    load.kriksar[fa.getLength(load.kriksar, load.markKriksar)] = [username, today, idWahana, kritikSaran]
    print("Kritik dan saran Anda kami terima.")

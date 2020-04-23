import csv
import f01 as load
import f02 as login
import f03 as save
import f04 as signUp
import f05 as pencarianPemain
import f06 as cariwahana
import f07 as pembelian
import f08 as penggunaanTiket
import f09 as refund
import f10 as kritikSaran
import f11 as lihat_laporan
import f12 as tambah_wahana
import f13 as topup
import f14 as riwayat_wahana
import f15 as tiket_pemain
import f16 as exits
import b01 as skc
import b02 as upgrade_gold
import b03 as best_wahana
import b04 as tiket_hilang


def printMainMenu(role):
    print("DAFTAR PILIHAN")
    if(role == "admin"):
        print('''
        ==> save
        ==> signup
        ==> login
        ==> cari pemain
        ==> lihat_laporan
        ==> tambah_wahana
        ==> topup
        ==> riwayat_wahana
        ==> tiket_pemain
        ==> exit
        ==> upgrade_gold
        ''')
    elif (role == 'pemain'):
        print('''
        ==> save
        ==> login
        ==> cari wahana
        ==> beli tiket
        ==> main
        ==> refund
        ==> kritik_saran
        ==> exit
        ''')
    else:
        print('''
        ==> login
        ==> exit
        ''')


def chooseMainMenu(role):
    printMainMenu(role)
    return (input("Masukkan perintah: ").lower())


def main():
    global nowPlayer
    nowPlayer = ["", ""]  # [username, role].
    finish = False  # Penentu jalannya program.
    # load program berfungsi untuk memastikan setiap data telah ter-load.
    load.load()
    # mode awal harus login terlebih dahulu sebelum menjalankan pilihan yang lain atau exit.
    printMainMenu(nowPlayer[1])
    mode = input("Masukkan pilihan: ")
    while (finish == False):

        if (mode == "signup" and nowPlayer[1] == "admin"):
            signUp.signUp()
            mode = chooseMainMenu(nowPlayer[1])

        elif (mode == "login"):
            lastPlayer = nowPlayer
            nowPlayer = login.login()
            if(len(nowPlayer) == 0):
                nowPlayer = lastPlayer
            mode = chooseMainMenu(nowPlayer[1])

        elif(mode == "save"):
            save.save()
            mode = chooseMainMenu(nowPlayer[1])

        elif (mode == "exit"):
            finish = exits.exit()

        elif (mode == "cari pemain" and nowPlayer[1] == "admin"):
            pencarianPemain.search()
            mode = chooseMainMenu(nowPlayer[1])

        elif(mode == "cari wahana" and nowPlayer[1] == "pemain"):
            cariwahana.searchWahana()
            mode = chooseMainMenu(nowPlayer[1])

        elif(mode == "beli tiket" and nowPlayer[1] == "pemain"):
            pembelian.buyTicket(nowPlayer[0])
            mode = chooseMainMenu(nowPlayer[1])

        elif(mode == "upgrade_gold" and nowPlayer[1] == "admin"):
            goldenAccount.goldAccount()
            mode = chooseMainMenu(nowPlayer[1])

        elif(mode == "main" and nowPlayer[1] == "pemain"):
            penggunaanTiket.play(nowPlayer[0])
            mode = chooseMainMenu(nowPlayer[1])

        elif(mode == "refund" and nowPlayer[1] == "pemain"):
            refund.refund(nowPlayer[0])
            mode = chooseMainMenu(nowPlayer[1])

        elif(mode == "kritik_saran" and nowPlayer[1] == "pemain"):
            kritikSaran.kritikDanSaran(nowPlayer[0])
            mode = chooseMainMenu(nowPlayer[1])

        elif(mode == 'lihat_laporan' and nowPlayer[1] == "admin"):
            lihat_laporan.lihatLaporan()
            mode = chooseMainMenu(nowPlayer[1])

        elif(mode == 'tambah_wahana' and nowPlayer[1] == "admin"):
            tambah_wahana.tambahWahana()
            mode = chooseMainMenu(nowPlayer[1])

        elif(mode == 'topup' and nowPlayer[1] == "admin"):
            topup.topup()
            mode = chooseMainMenu(nowPlayer[1])

        elif(mode == 'riwayat_wahana' and nowPlayer[1] == "admin"):
            riwayat_wahana.history()
            mode = chooseMainMenu(nowPlayer[1])

        elif(mode == 'tiket_pemain' and nowPlayer[1] == "admin"):
            tiket_pemain.tiketPemain()
            mode = chooseMainMenu(nowPlayer[1])

        elif(mode == "tiket_hilang" and nowPlayer[1] == "pemain"):
            tiket_hilang.laporanKehilangan()
            mode = chooseMainMenu(nowPlayer[1])

        elif(mode == 'best_wahana' and nowPlayer[1] == "admin"):
            best_wahana.bestWahana()
            mode = chooseMainMenu(nowPlayer[1])

        else:
            print("Masukkan anda salah silahkan masukkan pilihan yang tersedia !")
            mode = chooseMainMenu(nowPlayer[1])


if __name__ == "__main__":
    main()

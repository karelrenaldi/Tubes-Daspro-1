import f01 as load
import f03 as save


def exit():
    simpan = input(
        'Apakah anda mau melakukan penyimpanan file yang sudah dilakukan(Y/N)? ')
    if(simpan == 'Y'):
        save.save()
        print("Terima kasih sampai berjumpa kembali")
        return(True)
    else:
        print("Terima kasih sampai berjumpa kembali")
        return(True)

import f01 as load
import fileAcces as fa


def bestWahana():
    idWahana = [["", 0, ""] for i in range(100)]
    lengthIdWahana = 0
    for i in range(1, fa.getLength(load.wahana, load.markWahana)):
        idWahana[lengthIdWahana] = [load.wahana[i][0], 0, load.wahana[i][1]]
        lengthIdWahana += 1
    i = 0
    while (idWahana[i] != ["", 0, ""]):
        for j in range(1, fa.getLength(load.pembelian, load.markPembelian)):
            if(idWahana[i][0] == load.pembelian[j][2]):
                idWahana[i][1] += int(load.pembelian[j][3])
        i += 1
    # sorting ambil 3 terbesar
    for i in range(fa.getLength(idWahana, ["", 0, ""])):
        swap = ""
        for j in range(fa.getLength(idWahana, ["", 0, ""])):
            now = idWahana[i][1]
            if(now > idWahana[j][1]):
                swap = idWahana[i]
                idWahana[i] = idWahana[j]
                idWahana[j] = swap
                idWahana[j][1] = now
    # Menampilkan 3 wahana terbaik
    for i in range(3):
        print('{}\t| {}\t| {}\t| {}'.format(i+1, idWahana[i][0], idWahana[i][2], idWahana[i][1]))

import f01 as load
import fileAcces as fa


def lihatLaporan():
    # Bubble sort
    for i in range(1, fa.getLength(load.kriksar, load.markKriksar)):
        swap = ""
        for j in range(1, fa.getLength(load.kriksar, load.markKriksar)):
            now = load.kriksar[i][2]
            if(now < load.kriksar[j][2]):
                swap = load.kriksar[i]
                load.kriksar[i] = load.kriksar[j]
                load.kriksar[j] = swap
                load.kriksar[j][2] = now

    for i in range(1, fa.getLength(load.kriksar, load.markKriksar)):
        print('{}\t| {}\t| {}\t| {}'.format(load.kriksar[i][2], load.kriksar[i][1], load.kriksar[i][0], load.kriksar[i][3]))

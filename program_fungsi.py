print("\n"+"Perkenalan"+"\n"+20*"=")

nama = "merry"
umur = 18

def ket ():
    alamat = "mamuju"
    tgl_lahir = 19
    print("alamat :",alamat)
    print("tanggal lahir :",tgl_lahir)

print("nama :",nama)
print("umur :",umur)

ket()

print("\n"+"meampilkan daftar menu"+"\n"+20*"=")

bunga = []
def show_bunga():
    print("\n")
    print("-------------B U N G A-------------")
    print("[1]bunga matahari")
    print("[2]melati")
    print("[3]mawar")
    print("[4]asoka")
    print("[5]exit")

if bunga == 1:
    bunga_matahari()
elif bunga == 2:
    melati()
elif bunga == 3:
    mawar()
elif bunga == 4:
    asoka()
elif bunga == 5:
    exit()

show_bunga()





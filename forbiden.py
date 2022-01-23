# Mau Recode ? Ank Dajal
# Silahkan Recode Tapi Subrek Dulu
# Mikirlah Gk Gampang Buat Kek Ginian
# Subrek FIRZZZ ID



























































































































































































































































































































































































































































































































































import os,sys,time

def load():
    count = 0

    for t in range(101):
        time.sleep(0.1)
        print(f'\r \33[37;1m[\33[31;1m+\33[37;1m] Loading {t}%', end='', flush=True)
        count += 1
        if count == 3:
            count = 0

def nulis(mmk):
    for kntl in mmk + '\n':
        sys.stdout.write(kntl)
        sys.stdout.flush()
        time.sleep(0.1)

os.system("clear")
banner = """
\33[36;1m╦  \33[37;1m┌─┐┌─┐┬┌┐┌
\33[36;1m║  \33[37;1m│ ││ ┬││││ \33[31;1m> \33[37;1mCreator \33[31;1m: \33[1;33mFirzzz
\33[36;1m╩═╝\33[37;1m└─┘└─┘┴┘└┘ \33[31;1m> \33[37;1mYoutube \33[31;1m: \33[1;33mFIRZZZ ID

 \33[31;1m> \33[37;1mDownload Dulu Passwordnya
 \33[31;1m> \33[37;1mLink \33[31;1m: [ \33[32;1mhttps://cararegistrasi.com/sbn27 \33[31;1m]
\33[37;1m>-------------------------------------------------<\n"""

print(banner)

#-----------( Bang give alok bang hahahahahhhaha )-----------------
x = "Firzzz"
y = "anjirwibu"

def login():
    u = input("\33[31;1m# \33[37;1mUsername \33[31;1m: \33[30;1m")
    p = input("\33[31;1m# \33[37;1mPassword \33[31;1m: \33[30;1m")
    if u == x and p == y:
        print ("\33[31;1m> \33[37;1mLogin Succes \33[32;1m√\n")
        time.sleep(3)
        sys.exit
    else :
        print ("\33[31;1m> \33[37;1mLogin Gagal \33[31;1mX\n")
        login()


if __name__=='__main__':
       login()

#--------------( Yamate Ahahahahahaahhahahahahahah )---------------


def banner():
    os.system("clear")
    print ("\33[37;1m[\33[31;1m#\33[37;1m] \33[36;1mMake Doang \33[37;1mKagak Subrek \33[36;1m!!!")
    os.system("xdg-open https://youtube.com/channel/UCyOb9Jo3A0ZtUx_DcD4W2pQ")
    time.sleep(5)
    os.system("clear")
    print ("\33[35;1m╔═╗ ┌─┐ ┬─┐ ┌┐  ┬ ┌┬┐ ┌┬┐ ┌─┐ ┌┐┌")
    print ("\33[35;1m╠╣  │ │ ├┬┘ ├┴┐ │  ││  ││ ├┤  │││")
    print ("\33[35;1m╚   └─┘ ┴└─ └─┘ ┴ ─┴┘ ─┴┘ └─┘ ┘└┘")
    print (" ")
    print ("\33[31;1mΔ \33[37;1mBY \33[31;1m: \33[37;1mFirzzz")
    print ("\33[31;1mΔ \33[37;1mYT \33[31;1m: \33[37;1mFIRZZZ ID")
    print (" ")
    print ("\33[37;1m[\33[1;33m1\33[37;1m]\33[31;1m. \33[1;33mRepair")
    print ("\33[37;1m[\33[1;33m2\33[37;1m]\33[31;1m. \33[1;33mSupport Admin")
    print ("\33[37;1m[\33[1;33m3\33[37;1m]\33[31;1m. \33[1;33mExit\n")
    firz = input(" \33[37;1mInput \33[31;1m: \33[37;1m")
    if firz =="1":
       os.system("rm -rf $PREFIX/etc/apt/sources.list.d/*")
       print (" ")
       load()
       print (" ")
       time.sleep(1)
       os.system("pkg upgrade && pkg update")
       nulis("\n \33[37;1m[\33[32;1m√\33[37;1m] \33[32;1mSuccesfully\n")
       nulis(" \33[37;1m[\33[31;1m!\33[37;1m] Jangan Lupa Subrek \33[36;1mFIRZZZ ID\n")
    elif firz =="2":
         os.system("xdg-open https://youtube.com/channel/UCyOb9Jo3A0ZtUx_DcD4W2pQ")
    elif firz =="3":
         sys.exit()
    else:
         time.sleep(2)
         print ("\n \33[37;1mPilih Yang Bener Sayang \33[31;1m!!!")
         time.sleep(3)
         banner()




if __name__=='__main__':
    banner()

# Mau Recode? Anak dajal
# Silahkan Recode Tapi Subrek Dulu
# Mikir lah Gk Gampang Buat Kek Ginian 
# Yang Recode Tapi Gk Subrek Anak Dajal
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


def banner():
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

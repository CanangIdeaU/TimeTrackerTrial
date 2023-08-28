
import datetime as dt
print("\nPROGRAM SEDERHANA\nini adalah program untuk .....\n")
validasi = "apakah kamu ingin menjalankan program ini ? \n[y] yes \n[n] no\n\nINPUT USER : "
opening = input(validasi)
"\nini adalah program track time"
TrackTime = input("\nini adalah program track time.\napakah kamu ingin track time sekarang? \n[y] yes \n[n] no\n\nINPUT USER : ")

if opening == "y":

    TrackTime
    if TrackTime == "y":
            print("\nClock In kamu tercatat ")
            print("di tanggal :", dt.date.today())
            print("pada pukul :", dt.datetime.now().strftime("%H:%M:%S"), "\n")
            input=("\nSelanjutnya, apa yang ingin kamu lakukan sekarang sekarang? \n[x] Clock Cut \n[z] Break\n\nINPUT USER : ")
    else:
        print("\nTerimakasih sudah mau menjalankan program ini =) \n ")

else:
    print("\nTerimakasih sudah mau menjalankan program ini =) \n ")


import sys

print("++++++++++ PROGRAM ATM SEDERHANA ++++++++++")
print("1. Cek Uang")
print("2. Ambil Uang")
print("3. Setor Uang")


def atm():
    while True:
        pilih = int(input("Masukkan Angka Diatas : "))
        if pilih == 1:
            print("Jumlah Saldo Anda Adalah Rp 500000", '\n')
        if pilih == 2:
            print("Jumlah Saldo Anda Adalah Rp 500000")
            uang = 500000
            opsi1 = int(input("Mau Ambil Uang Berapa ? : "))
            hasil = uang - opsi1
            print("Saldo Anda Sekarang Berjumlah Rp :", hasil, '\n')
        elif pilih == 3:
            print("Saldo Anda Sekarang Adalah Rp 500000")
            opsi2 = int(input("Masukkan Jumlah Yang Ingin Disetor : "))
            uang1 = 500000
            hasil = opsi2 + uang1
            print("Jumlah Saldo Anda Sekarang Adalah Rp :", hasil, '\n')
        elif pilih != 1 and 2 and 3:
            print("Keywoard Salah!!!", '\n')
        lanjut = input("Ulangi Lagi ? (y/t) : ")
        if lanjut == 't':
            print("Terima Kasih....")
            break


atm()
input("Klik Enter To Quit Program...")
sys.exit()

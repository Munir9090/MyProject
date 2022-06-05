import sys
minuman = []
makanan = []
h_makanan = []
h_minuman = []
total = 0
print("""
 ========================================
                Munir Foods
             Makanan Dan Minuman
 ========================================
                
                Menu Makanan
 ------------------------------------------------
 |  Kode    |      Nama     |       Harga       |
 ------------------------------------------------
 |  12      |   Nasi Pecel  |   Rp. 7000        |
 |  20      |   Nasi Goreng |   Rp. 10000       |
 |  23      |   Nasi Boran  |   Rp. 12000       |
 |  28      |   Nasi Rawon  |   Rp. 15000       |
 ------------------------------------------------

                Menu Minuman
 ------------------------------------------------
 |  Kode    |      Nama     |       Harga       |
 ------------------------------------------------
 |  5       |   Es Jeruk    |   Rp. 5000        |
 |  10      |   Kopi        |   Rp. 4000        |
 |  12      |   Teh Hangat  |   Rp. 3000        |
 |  18      |   Es Teh      |   Rp. 4000        |
 ------------------------------------------------
""")

while True:
    makan = print("Ketik 1 Untuk Pilih Makanan")
    minum = print("Ketik 2 Untuk Pilih Minuman", '\n')
    pilih = int(input("Masukkan Angka Diatas : "))
    if pilih == 1:
        kode = int(input("Masukkan Kode Makanan : "))
        if kode == 12:
            makanan.append('Nasi Pecel')
            h_makanan.append(7000)
            total += 7000
        elif kode == 20:
            makanan.append('Nasi Goreng')
            h_makanan.append(10000)
            total += 10000
        elif kode == 23:
            makanan.append('Nasi Boran')
            h_makanan.append(12000)
            total += 12000
        elif kode == 28:
            makanan.append('Nasi Rawon')
            h_makanan.append(15000)
            total += 15000
    elif pilih == 2:
        kode = int(input("Masukkan Kode Minuman : "))
        if kode == 5:
            minuman.append('Es Jeruk')
            h_minuman.append(5000)
            total += 5000
        elif kode == 10:
            minuman.append('Kopi')
            h_minuman.append('4000')
            total += 4000
        elif kode == 12:
            minuman.append('Teh Hangat')
            h_minuman.append(3000)
            total += 3000
        elif kode == 18:
            minuman.append('Es Teh')
            h_minuman.append(4000)
            total += 4000
            print('')
    elif pilih == makan:
        print("Makanan Yang Dibeli : ", makanan)
        print("Harga Makanan :", h_makanan)
        print("Yang Harus Anda Bayarkan :", total, '\n')
        uang = int(input("Masukkan Uang Pembayaran : "))
        if uang > makan:
            print("Uang Kembalian Anda :", uang - total)
        elif uang == makan:
            print("Uang Anda Pas")
        else:
            print("Uang Anda Kurang :", uang - makan)
    lanjut_2 = input("Mau Pesan Lagi ? (y/t) : ")
    if lanjut_2 == 't':
        break

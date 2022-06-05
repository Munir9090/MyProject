import sys
jumlah = 10
barang = ["Roti", "Buku", "Pensil", "Penggaris", "Masker",
          "Stella", "Kacamata", "Minyak Goreng", "Kedelai", "Mie Instan"]
harga = [5000, 8000, 3000, 3000, 23000, 7000, 23000, 7000, 12000, 3500]
total = 0
barang_1 = []
harga_2 = []
print("""
----------------------------------------------------
|      Kode      |   Barang       |      Harga     |
----------------------------------------------------""")

for v in range(jumlah):
    kolom_1 = str(v+1)
    kolom_2 = str(barang[v])
    kolom_3 = str(harga[v])
    print('| ' + kolom_1 + (15-len(kolom_1))*' '
          + '| ' + kolom_2 + (15-len(kolom_2))*' '
          + '| ' + kolom_3 + (15-len(kolom_3))*' ' + '|')
print('----------------------------------------------------')


while True:
    kode = int(input("Masukkan Kode Diatas : "))
    if kode == 1:
        barang_1.append('Roti')
        harga_2.append(5000)
        total += 5000
    elif kode == 2:
        barang_1.append('Buku')
        harga_2.append(8000)
        total += 8000
    elif kode == 3:
        barang_1.append('Pensil')
        harga_2.append(3000)
        total += 3000
    elif kode == 4:
        barang_1.append('Penggaris')
        harga_2.append(3000)
        total += 3000
    elif kode == 5:
        barang_1.append('Masker')
        harga_2.append(23000)
        total += 23000
    elif kode == 6:
        barang_1.append('Stella')
        harga_2.append(7000)
        total += 7000
    elif kode == 7:
        barang_1.append('Kacamata')
        harga_2.append(23000)
        total += 23000
    elif kode == 8:
        barang_1.append('Minyak Goreng')
        harga_2.append(7000)
        total += 7000
    elif kode == 9:
        barang_1.append('Kedelai')
        harga_2.append(13000)
        total += 13000
    elif kode == 10:
        barang_1.append('Mie Instan')
        harga_2.append(3500)
        total += 3500
    else:
        print("Kode Tidak Valid!!!")
    lanjut = input("Mau Lanjut Belanja ? (y/t) : ")
    if lanjut == 't':
        print('')
        break


print("Barang Yang Anda Beli :", barang_1)
print("Harga Barang :", harga_2)
print("Uang Yang Harus Dibayarkan :", total, '\n')

uang = int(input("Masukkan Uang Pembayaran : "))
if uang > total:
    print("Uang Kembalian :", uang-total)
elif uang < total:
    print("Uang Anda Kurang :", uang-total)
elif uang == total:
    print("Uang Anda Pas", '\n')


input("Klik Enter To Quit Program...")
sys.exit()

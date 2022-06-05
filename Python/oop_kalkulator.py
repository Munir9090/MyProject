class kalkulator():
    def tambah(a,b):
        hasil = a + b
        print("Hasilnya adalah", hasil)
    
    def kurang(a,b):
        hasil = a - b
        print("hasilnya adalah", hasil)

    def bagi(a,b):
        hasil = a / b
        print("hasilnya adalah", hasil)

    def kali(a,b):
        hasil = a * b
        print("hasilnya adalah", hasil)

    a = int(input("masukkan angka pertama : "))
    operator = input("masukkan operator (+, -, /, *) : ")
    b = int(input("masukkan angka kedua : "))
    

    if operator == '+':
         tambah(a,b)
    elif operator == '-':
        kurang(a,b)
    elif operator == '/':
        bagi(a,b)
    elif operator == '*':
        kali(a,b)
    else:
        print("Perintah yang anda masukkan salah !!!")
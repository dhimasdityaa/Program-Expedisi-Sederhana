
def menu():
    print('++++++++++++++++++++++++++++++++++++++')
    print('+ Selamat Datang di Program Expedisi +')
    print('++++++++++++++++++++++++++++++++++++++')

    print('1. Kirim Paket')
    print('2. Cek Onkir')


def kirimPaket():
    namaP = str(input('Masukan Nama Pengirim : '))
    descP = str(input('Masukan Deskripsi Paket : '))
    noP = int(input('Masukan Nomer Handphone Pengirim : '))
    namaPe = str(input('Masukan Nama Penerima : '))
    AlaPe = str(input('Masukan Alamat Penerima : '))
    noPe = int(input('Masukan Nomer Handphone Penerima : '))
    AsalP = str(input('Masukan Lokasi Pengirim : '))
    tujuPe = str(input('Masukan Lokasi Penerima : '))
    berat = int(input('Masukan Berat Paket : '))

    def result():
        total = int(ongkir) * int(berat)

        print('+================================================+')
        print('+++++++++++ BUKTI PEMBAYARAN PENGIRIMAN ++++++++++')
        print('+================================================+')
        print('+ Nama Pengirim :', namaP)
        print('+ No Handphone pengirim :', noP)
        print('+ Nama Penerima :', namaPe)
        print('+ Alamat Penerima :', AlaPe)
        print('+ No Handphone Penerima :', noPe)
        print('+ Deskripsi Paket :', descP)
        print('+ Asal Paket dari :', AsalP)
        print('+ Tujuan Paket Ke :', tujuPe)
        print('+ Berat Paket Adalah :', berat)
        print('+ Biaya Pengiriman :', total)
        print('+================================================+')

    # AsalP Paket Dari Surabaya
    if AsalP == "Surabaya":
        if tujuPe == "Bekasi":
            ongkir = 45000
            result()
        elif tujuPe == "Jakarta":
            ongkir = 50000
            result()
        elif tujuPe == "Cikarang":
            ongkir = 40000
            result()
        elif tujuPe == "Jogja":
            ongkir = 25000
            result()
        elif tujuPe == "Malang":
            ongkir = 30000
            result()
        elif tujuPe == "Cilacap":
            ongkir = 44000
            result()
        elif tujuPe == "Brebes":
            ongkir = 42000
            result()
    # AsalP Paket Bekasi
    elif AsalP == "Bekasi":
        if tujuPe == "Surabaya":
            ongkir = 45000
            result()
        elif tujuPe == "Jakarta":
            ongkir = 20000
            result()
        elif tujuPe == "Cikarang":
            ongkir = 10000
            result()
        elif tujuPe == "Jogja":
            ongkir = 40000
            result()
        elif tujuPe == "Malang":
            ongkir = 35000
            result()
        elif tujuPe == "Cilacap":
            ongkir = 28000
            result()
        elif tujuPe == "Brebes":
            ongkir = 33000
            result()
    # AsalP Paket Cikarang
    elif AsalP == "Cikarang":
        if tujuPe == "Surabaya":
            ongkir = 45000
            result()
        elif tujuPe == "Jakarta":
            ongkir = 20000
            result()
        elif tujuPe == "Bekasi":
            ongkir = 10000
            result()
        elif tujuPe == "Jogja":
            ongkir = 40000
            result()
        elif tujuPe == "Malang":
            ongkir = 35000
            result()
        elif tujuPe == "Cilacap":
            ongkir = 28000
            result()
        elif tujuPe == "Brebes":
            ongkir = 33000
            result()
    # AsalP Paket Jogja
    elif AsalP == "Jogja":
        if tujuPe == "Surabaya":
            ongkir = 45000
            result()
        elif tujuPe == "Jakarta":
            ongkir = 20000
            result()
        elif tujuPe == "Cikarang":
            ongkir = 10000
            result()
        elif tujuPe == "Bekasi":
            ongkir = 40000
            result()
        elif tujuPe == "Malang":
            ongkir = 35000
            result()
        elif tujuPe == "Cilacap":
            ongkir = 28000
            result()
        elif tujuPe == "Brebes":
            ongkir = 33000
            result()
    # AsalP Paket Malang
    elif AsalP == "Malang":
        if tujuPe == "Surabaya":
            ongkir = 45000
            result()
        elif tujuPe == "Jakarta":
            ongkir = 20000
            result()
        elif tujuPe == "Cikarang":
            ongkir = 10000
            result()
        elif tujuPe == "Jogja":
            ongkir = 40000
            result()
        elif tujuPe == "Bekasi":
            ongkir = 35000
            result()
        elif tujuPe == "Cilacap":
            ongkir = 28000
            result()
        elif tujuPe == "Brebes":
            ongkir = 33000
            result()
    # AsalP Paket Cilacap
    elif AsalP == "Cilacap":
        if tujuPe == "Surabaya":
            ongkir = 45000
            result()
        elif tujuPe == "Jakarta":
            ongkir = 20000
            result()
        elif tujuPe == "Cikarang":
            ongkir = 10000
            result()
        elif tujuPe == "Jogja":
            ongkir = 40000
            result()
        elif tujuPe == "Malang":
            ongkir = 35000
            result()
        elif tujuPe == "Bekasi":
            ongkir = 28000
            result()
        elif tujuPe == "Brebes":
            ongkir = 33000
            result()
    # Brebes
    elif AsalP == "Bekasi":
        if tujuPe == "Surabaya":
            ongkir = 45000
            result()
        elif tujuPe == "Jakarta":
            ongkir = 20000
            result()
        elif tujuPe == "Cikarang":
            ongkir = 10000
            result()
        elif tujuPe == "Jogja":
            ongkir = 40000
            result()
        elif tujuPe == "Malang":
            ongkir = 35000
            result()
        elif tujuPe == "Cilacap":
            ongkir = 28000
            result()
        elif tujuPe == "Bekasi":
            ongkir = 33000
            result()


def cekOnkir():
    AsalP = str(input('Masukan Kota Asal Pengiriman :'))
    tujuPe = str(input('Masukan Kota Tujuan Penerima :'))
    berat = int(input('Masukan Berat Paket :'))

    def result():
        total = int(ongkir) * int(berat)

        print('+--------------------------------------------+')
        print('|--------------- LACAK PAKET ----------------|')
        print('+--------------------------------------------+')
        print('| Kota Asal Pengirim :', AsalP)
        print('| Kota Tujuan Penerima :', tujuPe)
        print('| Biaya Ongkos Kirim :', ongkir, 'Per Kg')
        print('| Berat Paket :', berat, 'Kg')
        print('| Total Biaya Pengiriman :', total)
        print('+--------------------------------------------+')
 # AsalP Paket Dari Surabaya
    if AsalP == "Surabaya":
        if tujuPe == "Bekasi":
            ongkir = 45000
            result()
        elif tujuPe == "Jakarta":
            ongkir = 50000
            result()
        elif tujuPe == "Cikarang":
            ongkir = 40000
            result()
        elif tujuPe == "Jogja":
            ongkir = 25000
            result()
        elif tujuPe == "Malang":
            ongkir = 30000
            result()
        elif tujuPe == "Cilacap":
            ongkir = 44000
            result()
        elif tujuPe == "Brebes":
            ongkir = 42000
            result()
    # AsalP Paket Bekasi
    elif AsalP == "Bekasi":
        if tujuPe == "Surabaya":
            ongkir = 45000
            result()
        elif tujuPe == "Jakarta":
            ongkir = 20000
            result()
        elif tujuPe == "Cikarang":
            ongkir = 10000
            result()
        elif tujuPe == "Jogja":
            ongkir = 40000
            result()
        elif tujuPe == "Malang":
            ongkir = 35000
            result()
        elif tujuPe == "Cilacap":
            ongkir = 28000
            result()
        elif tujuPe == "Brebes":
            ongkir = 33000
            result()
    # AsalP Paket Cikarang
    elif AsalP == "Cikarang":
        if tujuPe == "Surabaya":
            ongkir = 45000
            result()
        elif tujuPe == "Jakarta":
            ongkir = 20000
            result()
        elif tujuPe == "Bekasi":
            ongkir = 10000
            result()
        elif tujuPe == "Jogja":
            ongkir = 40000
            result()
        elif tujuPe == "Malang":
            ongkir = 35000
            result()
        elif tujuPe == "Cilacap":
            ongkir = 28000
            result()
        elif tujuPe == "Brebes":
            ongkir = 33000
            result()
    # AsalP Paket Jogja
    elif AsalP == "Jogja":
        if tujuPe == "Surabaya":
            ongkir = 45000
            result()
        elif tujuPe == "Jakarta":
            ongkir = 20000
            result()
        elif tujuPe == "Cikarang":
            ongkir = 10000
            result()
        elif tujuPe == "Bekasi":
            ongkir = 40000
            result()
        elif tujuPe == "Malang":
            ongkir = 35000
            result()
        elif tujuPe == "Cilacap":
            ongkir = 28000
            result()
        elif tujuPe == "Brebes":
            ongkir = 33000
            result()
    # AsalP Paket Malang
    elif AsalP == "Malang":
        if tujuPe == "Surabaya":
            ongkir = 45000
            result()
        elif tujuPe == "Jakarta":
            ongkir = 20000
            result()
        elif tujuPe == "Cikarang":
            ongkir = 10000
            result()
        elif tujuPe == "Jogja":
            ongkir = 40000
            result()
        elif tujuPe == "Bekasi":
            ongkir = 35000
            result()
        elif tujuPe == "Cilacap":
            ongkir = 28000
            result()
        elif tujuPe == "Brebes":
            ongkir = 33000
            result()
    # AsalP Paket Cilacap
    elif AsalP == "Cilacap":
        if tujuPe == "Surabaya":
            ongkir = 45000
            result()
        elif tujuPe == "Jakarta":
            ongkir = 20000
            result()
        elif tujuPe == "Cikarang":
            ongkir = 10000
            result()
        elif tujuPe == "Jogja":
            ongkir = 40000
            result()
        elif tujuPe == "Malang":
            ongkir = 35000
            result()
        elif tujuPe == "Bekasi":
            ongkir = 28000
            result()
        elif tujuPe == "Brebes":
            ongkir = 33000
            result()
    # Brebes
    elif AsalP == "Bekasi":
        if tujuPe == "Surabaya":
            ongkir = 45000
            result()
        elif tujuPe == "Jakarta":
            ongkir = 20000
            result()
        elif tujuPe == "Cikarang":
            ongkir = 10000
            result()
        elif tujuPe == "Jogja":
            ongkir = 40000
            result()
        elif tujuPe == "Malang":
            ongkir = 35000
            result()
        elif tujuPe == "Cilacap":
            ongkir = 28000
            result()
        elif tujuPe == "Bekasi":
            ongkir = 33000
            result()


menu()

pilih = int(input('Silahkan Pilih : '))

if pilih == 1:
    kirimPaket()
else:
    cekOnkir()

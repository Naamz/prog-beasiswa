maximalIPK  = float(4.00)
minimumIPK  = float(3.00)
nama        = input("Masukkan nama mahasiswa : ")

while True:
    try:
        nim = int(input("Masukkan NIM mahasiswa : "))
    # VALIDASI NIM
    except ValueError:
        # PESAN ERROR JIKA NIM TIDAK DIISI DENGAN ANGKA
        print("NIM harus diisi angka!!")
        # JIKA NIM DIISI DENGAN ANGKA, KODE PROGRAM AKAN BERLANJUT
        continue
    else:
        while True:
            try:
                ipk = float(input("Masukkan nilai IPK : "))
            #VALIDASI IPK 
            except ValueError:
                # PESAN ERROR JIKA NILAI IPK TIDAK DIISI DENGAN ANGKA
                print("Nilai IPK harus diisi angka!!")
                # JIKA NIM DIISI DENGAN ANGKA, KODE PROGRAM AKAN BERLANJUT
                continue
            else:
                # CEK APAKAH DAPET BEASISWA ATAU TIDAK
                if ipk <= maximalIPK:
                    if ipk >= minimumIPK:
                        print("Selamat, kamu memenuhi syarat untuk mendapatkan beasiswa")
                        break
                    else:
                        print("Maaf, kamu belum memenuhi syarat untuk mendapatkan beasiswa")
                        break
                else:
                    # PESAN ERROR JIKA NILAI IPK > 4
                    print("Nilai IPK tidak boleh lebih dari 4.00")
    break
print("Terimakasih")

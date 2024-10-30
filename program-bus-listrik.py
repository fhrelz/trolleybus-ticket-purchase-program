# fahrel
def cetak():
    print("================================================")
cetak()
print("    SELAMAT DATANG DI BUS LISTRIK SOLO")
print("     SILAHKAN PILIH KOTA TUJUAN ANDA!")
cetak()

print()
print("  Kode Tujuan |  Kota Tujuan  | Harga Masuk |")
print('''   ________________________________________   
      ''')
print("  JKRT        |   Jakarta     | Rp. 350000  |")
print("  CRBN        |   Cirebon     | Rp. 312000  |")
print("  CKRG        |   Cikarang    | Rp. 315000  |")
print("  JGJA        |   Jogja       | Rp. 135000  |")
print("  BKSI        |   Bekasi      | Rp. 270000  |")
print("  SRBA        |   Surabaya    | Rp. 150000  |")
print("  KAWE        |   Kaligawe    | Rp. 190000  |")
print("  SMRG        |   Semarang    | Rp. 90000   |")
print("  TGAL        |   Tegal       | Rp. 110000  |")
print("  PKLN        |   Pekalongan  | Rp. 148000  |")
print("  MLNG        |   Malang      | Rp. 97000   |")
print("  PRBG        |   Probolinggo | Rp. 210000  |")
print("  BWGI        |   Banyuwangi  | Rp. 248000  |")

cetak()
print("    SELAMAT DATANG DI BUS LISTRIK SOLO")
print("     SILAHKAN MASUKKAN DATA DIRI ANDA!")
cetak()

# Input data
nama = input("Nama Pengguna : ")
no_hp = input("Masukkan Nomor Hp : ")
kode = input("Masukkan Kode Kota Tujuan Anda : ")
jumlah_pembelian = int(input("Jumlah Tiket Yang ingin Dibeli : "))

cetak()
print("          MOHON MENUNGGU SEBENTAR...")

# Logika / langkah selanjutnya ketika user memberikan input sesuai dengan data yang tersedia

if kode == "JKRT" or kode == "jkrt":
    jurusan = "Jakarta"
    harga = 350000
elif kode == "CRBN" or kode == "crbn":
    jurusan + "Cirebon"
    harga = 312000
elif kode == "CKRG" or kode == "ckrg":
    jurusan = "Cikarang"
    harga = 315000
elif kode == "JGJA" or kode == "jgja":
    jurusan = "Jogja"
    harga = 135000
elif kode == "BKSI" or kode == "bksi":
    jurusan = "Bekasi"
    harga = 270000
elif kode == "SRBA" or kode == "srba":
    jurusan = "Surabaya"
    harga = 150000
elif kode == "KAWE" or kode == "kawe":
    jurusan = "Kaligawe"
    harga = 190000
elif kode == "SMRG" or kode == "smrg":
    jurusan = "Semarang"
    harga = 90000
elif kode == "TGAL" or kode == "tgal":
    jurusan = "Tegal"
    harga = 110000
elif kode == "PKLN" or kode == "pkln":
    jurusan = "Pekalongan"
    harga = 148000
elif kode == "MLNG" or kode == "mlng":
    jurusan = "Malang"
    harga = 97000
elif kode == "PRBG" or kode == "prbg":
    jurusan = "Probolinggo"
    harga = 210000
elif kode == "BWGI" or kode == "bwgi":
    jurusan = "Banyuwangi"
    harga = 248000
else :
    jurusan = "Maaf Mohon Masukkan Kode Sesuai Dengan Yang Tertera di Layar"
    harga = 0
    

print("              MEMPROSES HARGA...")
cetak()

#proses potongan 
if jumlah_pembelian >= 3 : 
    potongan= (jumlah_pembelian * harga) * 0.05
else: 
    potongan=0 

total_harga = (harga * jumlah_pembelian) - potongan

# Proses logika menampilkan harga
print("Nama                          :", nama)
print("No Hp                         :", no_hp)
print("Kode Kota Tujuan              :", kode)
print("Kota Tujuan                   :", jurusan)
print("Jumlah Tiket Yang Dibeli      :", jumlah_pembelian)
print("Jumlah Diskon Yang Didapatkan :", potongan)
print("Total Harga                   : Rp", total_harga)

cetak()
konfirmasi = input('Ingin Melanjutkan Pembayaran? = Y/N :')
cetak()

if konfirmasi == "Y" or konfirmasi == "y":
    harga2 = int(input("Masukan Jumlah Uang Anda :"))
    uang_kembali = (total_harga - harga2)
    print("Kembalian Anda :", uang_kembali)
    cetak()
    print("  TERIMAKASIH TELAH MENGGUNAKAN LAYANAN KAMI!")
    print(" SILAHKAN LANGSUNG MENUJU KE TAHAP SELANJUTNYA!")
    cetak()
    
else:
    cetak()
    print("  TERIMAKASIH TELAH MENGGUNAKAN LAYANAN KAMI..")
    print("            SAMPAI JUMPA DI LAIN WAKTU..")
    cetak()
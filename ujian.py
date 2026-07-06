# print('selamat datang di assetment akhir')
# print('soal pertama')

# suhu = float(input('masukan suhu yang ingin di ubah :'))
# fahrenhait = (suhu * 9//5 ) + 32

# print(f' suhu {suhu}°c dan fahrenhait {fahrenhait}°f')

# print('soal kedua')
# one = int(input('Masukkan angka ke-1:'))
# two = int(input('Masukkan angka ke-2:'))
# three = int(input('Masukkan angka ke-3:'))
# four  = int(input('Masukkan angka ke-4:'))
# fifty = int(input('Masukkan angka ke-5:'))

# number = [one,two,three,four,fifty]
# genap = 0
# ganjil = 0
# for n in number:
#     if n % 2 == 0:
#         print('GENAP')
#         genap += 1
#     else:
#         print('GANJIl')
#         ganjil += 1

#     print(f"""hasil analisis
#     {one} adalah {'GENAP' if one % 2 == 0 else 'GANJIL'}
#     {two} adalah {'GENAP' if two % 2 == 0 else 'GANJIL'}
#     {three} adalah {'GENAP' if three % 2 == 0 else 'GANJIL'}
#     {four} adalah {'GENAP' if four % 2 == 0 else 'GANJIL'}
#     {fifty} adalah {'GENAP' if fifty % 2 == 0 else 'GANJIL'}""")

# print(f'Genap = {genap} \n Ganjil = {ganjil}')

# print('soal ketiga')
# nama = input('masukan nama anda :')
# first_exam = int(input('masukan nilai ujian pertama:'))
# seccond_exam = int(input('masukan nilai ujian kedua :'))
# third_exam = int(input('masukan nilai ujian ketiga :'))
# avarege_exam = (first_exam + seccond_exam + third_exam)/3
# grade = ' '

# if avarege_exam >= 85 :
#     grade = 'A'
# elif avarege_exam >= 75 :
#     grade = 'B'
# elif avarege_exam >= 60 :
#     grade = 'C'
# else:
#     print('maaf kamu tidak lulus')


# print(f'nama siswa = {nama}\n nilai ujian pertama {first_exam}\n nilai ujian kedua {seccond_exam}\n nilai ujian ketiga {third_exam}')
# print(f'nilai rata rata = {avarege_exam}')
# print(f'Grade = {grade}')

# print('soal keempat')


# kalimat = input('masukan kalimat anda :').title()
# print(f"""
# kalimat = {kalimat}
# jumlah abjad = {len(kalimat)}
# jumlah kata = {len(kalimat.split(' '))}
# uppercase = {kalimat.upper()}
# lowercase = {kalimat.lower()}
# titlecase = {kalimat.title()}
# posisi python = {kalimat.find('Python')}""")

# print('soal kelima')
# numbers = [10,20,30,40,50]
# print(numbers)
# numbers.append(60)
# numbers.append(70)
# numbers.append(80)

# print(f'Setelah di tambahkah [60,70,80]: {numbers}')

# numbers[2]= 25
# print(f'setelah di tambahkan 25 : {numbers}')
# del numbers[4]
# print(f'setelah indeks ke-4 di hapus : {numbers}')
# print(f'total elemen = {len(numbers)}')

# print('soal keenam')

# first_number = int(input('masukan angka 1 :'))
# second_number = int(input('masukan angka 2 :'))
# third_number = int(input('masukan angka 3 :'))

# def factorial_iterative(n: int)-> int: 
#     if n < 0:
#         ValueError('factorial is not difined for negativ number')
#     result = 1
#     for i in range(2,n + 1):
#         result *= i
#     return result

# print(f'Faktorial dari {first_number} adalah: {factorial_iterative(first_number)}')
# print(f'Faktorial dari {second_number} adalah: {factorial_iterative(second_number)}')
# print(f'Faktorial dari {third_number} adalah: {factorial_iterative(third_number)}')
# print(f'Total hitungan: 3 angka telah diproses')


# data = []
# def Data_karyawan(nama= str, devisi = str , gaji = int):
#     data_karyawan = {}
#     data_karyawan['nama']= nama
#     data_karyawan['devisi'] = devisi
#     data_karyawan['gaji'] = gaji
#     data.append(data_karyawan)
#     print(f'nama = {nama} bekerja di devisi = {devisi} gaji = {gaji}')

# def tampilkan_data(data):
#     for i, karyawan in enumerate(data, 1):
#         print(f'{i} {karyawan['nama']} - {karyawan['devisi']} - {karyawan['gaji']}')

# def cari_karyawan(nama,data):
#     print(f'di cari nama = {nama}')
#     for item in data:
#      if item['nama'] == nama:
#         print(f'di temukan {item['nama']} devisi {item['devisi']} gaji {item['gaji']}')

# def update_gaji(nama : str, gaji_baru : int, data):
#    print(f'update gaji {nama} menjadi Rp {gaji_baru}')
#    for item in data:
#       if item['nama'] == nama:
#          item['gaji'] = gaji_baru
#          print(f'gaji {nama} berhasil di update')
#          break
#       else:
#          print(f'gaji {nama} gagal di update')
   
# def hapus_karyawan(nama,data):
#    print(f'hapus data {nama}')
#    for item in data:
#     if item['nama'] == nama :
#       data.remove(item)
#       print(f'< data {nama} berhasil di hapus')
#       return
#     else :
#        print(f'data {nama} tidak berhasil di hapus')

# print('== DATA KARYAWAN ==')
# Data_karyawan('budi','data analyist', 10000)
# Data_karyawan('jobel','dokter', 10000)
# Data_karyawan('jordan','ai engeenering', 20000)

# print('data semua karyawan')
# tampilkan_data(data)

# print('cari karyawan')
# cari_karyawan('jordan', data)

# print('update gaji')
# update_gaji(nama='budi',gaji_baru=300000,data= data)

# print('hapus data')
# hapus_karyawan(nama= 'jobel',data=data)

# value = int(input('masukan angka :'))
# print('pola segitiga bintang')
# for i in range(1, value + 1):
#     for j in range(i):
#         print('*', end=' ')
#     print()
# print('pola segitiga bintang terbalik')
# for i in range(value,0,-1):
#     for j in range(i):
#         print('*', end=' ')
#     print()

# import random

# random_list = [random.randint(1, 100) for _ in range(10)]
# print(f'List original : {random_list}')
# print(f'list angka 50 ke atas : {sorted([num for num in random_list if num >= 50])}')
# print(f'list angka genap : {sorted([num for num in random_list if num % 2 == 0])}')
# print(f' angka yang habis di bagi 3 : {len(sorted([num for num in random_list if num % 3 == 0]))}')

# print(f"""statistik
#       angka terbesar = {max(random_list)}
#       angka terkecil = {min(random_list)}
#       rata-rata = {sum(random_list) / len(random_list)}
#       jumlah angka = {sum(random_list)}""")

# print(f'list terurut dari kecil ke besar : {sorted(random_list)}')
# print(f'list terurut dari besar ke kecil : {sorted(random_list, reverse=True)}')

# try:
#     numbers = int(input('masukan angka pertama:'))
#     second_numbers = int(input('masukan angka kedua:'))
# except ValueError:
#       print('ValueError angka harus berupa integer')
#       exit()
# try:
#     operator = input('masukan operator (+,-,*,/):')
# except ValueError:
#     print('ValueError operator tidak valid')
#     exit()

# if operator == '+':
#    numbers += second_numbers
#    print(f'hasil penjumlahan = {numbers}')
# elif operator == '-':
#    numbers -= second_numbers
#    print(f'hasil pengurangan = {numbers}')
# elif operator == '*':
#    numbers *= second_numbers
#    print(f'hasil perkalian = {numbers}')
# elif operator == '/':
#    try:
#       numbers /= second_numbers
#       print(f'hasil pembagian = {numbers}')
#    except ZeroDivisionError:
#       print('Error: Pembagian dengan nol tidak diperbolehkan.')

# print('=== OPERATOR SELESAI ===')
from unicodedata import name


# history = []
# def TebakAngka():
#     import random
#     angka_rahasia = random.randint(1,10)
#     percobaan = 0
#     batas_percobaan = 10
    
#     print('selamat datang di permainan tebak angka')
#     while percobaan < batas_percobaan:
#         tebakan = int(input('masukan angka antara 1 sampai 10 :'))
#         history.append(tebakan)
#         if tebakan < angka_rahasia:
#             percobaan += 1
#             print('terlalu rendah')
#         elif tebakan > angka_rahasia:
#             percobaan += 1
#             print('terlalu tinggi')
#         else:
#             print(f'selamat tebakan anda benar {angka_rahasia}')
#             break
#     print(f'anda telah mencoba {percobaan} kali, angka rahasia adalah {angka_rahasia}')
#     print('skor permainan tebak angka :')
#     print(f'history percobaan = {history}')
#     if percobaan == 3 and percobaan <= 3:
#          print('skor anda = 100')
#     elif percobaan >= 4 and percobaan <= 5:
#          print('skor anda = 75')
#     elif percobaan >= 6 and percobaan <= 7:
#          print('skor anda = 50')
#     else:
#          print('skor anda = 25')
         
# TebakAngka()

# db_mahasiswa = {}
# def tambah_mahasiswa(nama,nim,semestar,gpa,):
#     if nim in db_mahasiswa:
#        raise ValueError(f'Mahasiswa dengan NIM {nim} sudah ada dalam database.')
#     else:
#         db_mahasiswa[nim] = (nama, semestar, gpa)
#         print(f'{nim} - {nama} - (semester{semestar} -  gpa{gpa} ditambahkan')

# def tampilkan_mahasiswa():
#     nama = input('masukan nama mahasiswa yang ingin di tampilkan :')
#     if nama not in [mahasiswa[0] for mahasiswa in db_mahasiswa.values()]:
#         print(f'Mahasiswa dengan nama {nama} tidak ditemukan dalam database.')
#     else:
#         print('Daftar Mahasiswa :')
#         for nim, (nama, semester, gpa) in db_mahasiswa.items():
#             print(f'NIM: {nim}, Nama: {nama}, Semester: {semester}, GPA: {gpa}')

# def update_gpa(nim, gpa_baru,db):
#     nama,semester,gpa = db[nim]
#     db[nim] = (nama, semester, gpa_baru)
#     print(f'GPA mahasiswa dengan NIM {nim} dari {gpa} berhasil diperbarui menjadi {gpa_baru}.')


# def cari_mahasiswa(min_gpa ,db):
#     for nim, (nama, semester, gpa) in db.items():
#         if gpa >= min_gpa:
#             print(f'Mahasiswa dengan GPA {gpa} ditemukan:')
#             print(f'NIM: {nim}, Nama: {nama}, Semester: {semester}, GPA: {gpa}')

# def statistik_gpa(db):
#     if not db:
#         print('Database mahasiswa kosong.')
#         return
#     else:
#         gpa_list = [gpa[2] for gpa in db.values()]
#         print(f'Statistik GPA:')
#         print(f'GPA Tertinggi: {max(gpa_list)}')
#         print(f'GPA Terendah: {min(gpa_list)}')
#         print(f'GPA Rata-rata: {sum(gpa_list) / len(gpa_list):.2f}')

# def hapus_mahasiswa(nim, db):
#     if nim in db:
#         del db[nim]
#         print(f'Mahasiswa dengan NIM {nim} berhasil dihapus dari database.')


# tambah_mahasiswa('budi', '12345', 3 , 3.5)
# tampilkan_mahasiswa()
# update_gpa('12345', 3.8, db_mahasiswa)
# statistik_gpa(db_mahasiswa)
# cari_mahasiswa(3.0, db_mahasiswa)
# hapus_mahasiswa('12345', db_mahasiswa)


# with open('data_penjualan.txt', 'w') as file:
#     while True:
#         produk = input('Masukkan nama produk: ')
#         harga = float(input('Masukkan harga produk: '))
#         jumlah = int(input('Masukkan jumlah produk: '))
#         file.write(f' {produk}, {harga}, {jumlah}, {harga * jumlah}\n')
#         print(f'Data Penjualan {produk} berhasil disimpan ke file data_penjualan.txt')
#         lanjut = input('Apakah Anda ingin menambahkan data penjualan lagi? (y/n): ')
#         if lanjut.lower() != 'y':
#                 break

def hitung_bunga_majemuk(principal, rate, time, n=1):
    rate = rate / 100
    jumlah_akhir = principal * (1 + rate / n) ** (n * time)
    bunga_total = jumlah_akhir - principal
    return jumlah_akhir, bunga_total

def validasi_input(principle, rate, time):
    if principle <= 0:
        return False, 'modal harus lebih dari 0'
    if rate <= 0 :
        return False, 'suku bunga harus lebih dari 0'
    if time <= 0 :
        return False, 'waktu investasi harus lebih dari kosong'
    else:
        return True, ""
def banding_investasi(principle, rate , time):
    hasil_dict = {}

    for modal in principle:
        akhir, bunga = hitung_bunga_majemuk(modal,rate,time)
        hasil_dict[modal] = {
            'jumlah_akhir' : akhir,
            'bunga' : bunga
        }

    investasi_terbaik = max(
        hasil_dict,
        key= lambda x : hasil_dict[x] ['jumlah_akhir']
    )
    return hasil_dict,investasi_terbaik

def generate_laporan(nama_investasi, principal,final_amount, bunga):
    laporan = f"""
  === {nama_investasi} ===
  Modal Awal : Rp {principal:.2f}
  Jumlah Akhir : Rp {final_amount:.2f}
  keuntungan : Rp {bunga:.2f}
  Roi        : Rp {(bunga / principal)* 100:.2f}"""
    return laporan

def menu():
    print('=== KALKULATOR INVESTASI ===')
    principal =float(input('masukan jumlah investasi awal : Rp'))
    rate = float(input('masukan suku bunga tahunan (&) : '))
    time = float(input('masukan jangka waktu investasi (tahun) :'))

    valid,pesan = validasi_input(principal,rate,time)

    if not valid:
        print(pesan)
    else:
        akhir, bunga = hitung_bunga_majemuk(principal,rate,time)

        print('== ANALISI INVESTASI ANDA ==')
        print(generate_laporan('investasi anda',principal, rate, time))
        
        pilihan = [10000000, 15000000, 20000000]

        hasil, terbaik = banding_investasi(pilihan, rate, time)

        print('== PERBANDINGAN INVESTASI ==')
        for modal, data in hasil.items():
            print(generate_laporan(
            f'modal Rp {modal:.2f}',
            modal,
            data['jumlah_akhir'],
            data['bunga'],
          ))
            
        print(f'investasi terbaik : Rp {terbaik :.2f}')
menu()
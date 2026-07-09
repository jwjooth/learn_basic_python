suhu = float(input('masukan suhu yang ingin di input:'))


fahrenheit = (suhu * 9/5) + 32
print(f"{suhu}°C sama dengan {fahrenheit:.2f}°F")

first = float(input('masukan angka ke 1 :'))
seccond =float(input('masukan angka ke 2 :'))
third = float(input('masukan angka ke 3 :'))
four = float(input('masukan angka ke 4 :'))
five = float(input('masukan angka ke 5 :'))

data = [first]
genap = 0
ganjil = 0
for i in data:
    if i % 2 == 0:
        genap += 1
    else:
        ganjil += 1

print('== HASIL ANALISiS ==')
print(f"""
{first} adalah angka {'GENAP' if first % 2 == 0 else 'GANJIL' }
{seccond} adalah angka {'GENAP' if seccond % 2 == 0 else 'GANJIL' }
{third} adalah angka {'GENAP' if third  % 2 == 0 else 'GANJIL' }
{four} adalah angka {'GENAP' if four % 2 == 0 else 'GANJIL' }
{five} adalah angka {'GENAP' if five % 2 == 0 else 'GANJIL' }""")

print(f'JUMLAH GENAP {genap}\nJUMLAH GANJIL {ganjil}')
grade = []
nama_siswa = input('masukan nama siswa :')
nilai1 = int(input('masukan nilai ujian 1 :'))
nilai2 = int(input('masukan nilai ujian 2 :'))
nilai3 = int(input('masukan nilai ujian 3 :'))
data = [nilai1,nilai2,nilai3]
rata_rata = (sum(data) / len(data))

kalimat = input('masukan kalimat :')
total_abjad = len(kalimat)
title = kalimat.title()
cari_nama = input('masukan nama di cari :')
cari = kalimat.find(cari_nama)
total_kata = kalimat.strip().split(' ')

print(f"""
kalimat original = {kalimat}
total abjad = {total_abjad}
total_kata = {total_kata}
""")
grade = []
if rata_rata >= 85:
    grade.append('GRADE A')
elif rata_rata >= 75 and rata_rata < 80 :
    grade.append('GRADE B')
elif rata_rata >= 65 and rata_rata < 75 :
    grade.append('GRADE C') 
else:
    print('maaf kamu tidak lulus')
    

print('== HASIL UJIAN ==')
print(f"""
Nama : {nama_siswa}
Nilai 1 : {nilai1}
Nilai 2 : {nilai2}
Nilai 3 : {nilai3}""")
print(f'rata rata : {rata_rata}')
print(f'{rata_rata:.2f}')
print(grade)

kalimat = input('masukan kalimat :')
total_abjad = len(kalimat)
kata = kalimat.strip().split(' ')
total_kata = len(kata)
upper = kalimat.upper()
lower = kalimat.lower()
# upper case = {upper}
# lower case = {lower}
# title case = {title}
# posisi {cari_nama} = di temukan di indeks {cari}""")

list = []
list2 = []

for i in range(5):
    nilai = (int(input('masukan angka :')))
    list.append(nilai)

print(f'list original : {list}')

for i in range(3):
    nilai2 = int(input('masukan 3 number tambahan :'))
    list2.append(nilai2)
    total = list + list2
total = list + list2

print(f'setelah di tambahkan {list2} =\n {total}')
sisipkan = total.insert(2, 25)
print(f'setelah di sisipkan \" 25 \" di indeks[2] = {total}')
del total[2]
print(f'setelah indeks 2 di hapus = {total}')

print(f'total elemen = {len(total)}')

one = int(input('masukan angka 1 :'))
two = int(input('masukan angka 2 :'))
three = int(input('masukan angka 3 :'))

def hitung_faktorial(n):
    if n < 0:
        raise ValueError('input tidak bisa bernilai negatif')
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result  

print(f'Masukkan angka ke-1: {one}, faktorial dari {one} adalah :{hitung_faktorial(one)}')
print(f'Masukkan angka ke-2: {two},  faktorial dari {two} adalah : {hitung_faktorial(two)}')
print(f'Masukkan angka ke-3: {three}, faktorial dari {three} adalah : {hitung_faktorial(three)}')
print('total hitungan : 3 angka telah di proses')

data = []
def tambah_karyawan(nama,devisi,gaji):
    data_karyawan ={}
    data_karyawan['nama'] = nama
    data_karyawan['devisi'] = devisi
    data_karyawan['gaji'] = gaji
    data.append(data_karyawan)
    print(f'nama : {nama}, devisi : {devisi}, gaji : Rp{gaji} di tambahkan ')

def tampilkan_data(data):
    for i, karyawan in enumerate(data,1):
        print(f'{i}. {karyawan['nama']} - {karyawan['devisi'] }- Rp{karyawan['gaji']}')

def cari_karyawan(nama,data):
    print(f'di cari nama {nama}')
    for item in data:
        if item['nama'] == nama:
            print(f'di temukan nama : {nama} bekerja di bidang : {item['devisi']} gaji : Rp{item['gaji']}')

def update_gaji(nama,gaji_baru,data):
    print(f'di cari nama {nama}')
    for key in data:
        if key['nama'] == nama:
            print(f'ubah gaji karyawan gaji awal Rp{key['gaji']} di update ke gaji baru menjadi Rp{gaji_baru}')

def hapus_karyawan(nama,data):
    print(f'nama : {nama}')
    for item in data: 
        if item['nama'] == nama:
            data.remove(item)
            print(f'data {nama} berhasil di hapus dari sistem')

print('menambah kan data karyawan')
tambah_karyawan('BUDI','IT',1000)
tambah_karyawan('ASEP','SISTEM DATA',3000)
tambah_karyawan('UCUP','WEB DEV', 2000)

print('menampilkan data karyawan')
tampilkan_data(data)

print('cari karyawan')
cari_karyawan('BUDI',data)
cari_karyawan('ASEP',data)
cari_karyawan('UCUP',data)

print('update gaji karyawan')
update_gaji('BUDI',200000,data)
update_gaji('ASEP',3000,data)
update_gaji('UCUP',1500,data)

print('hapus data karyawan ')
hapus_karyawan('BUDI',data)

number = int(input('masukan jumlah baris : '))
print('POLA SEGIGA :')
for i in range(1,number + 1):
    for j in range(i):
        print('*', end=' ')
    print()
print('POLA SEGITIGA TERBALIK :')
for i in range(number,0,-1):
    for i in range(i):
        print('*', end=' ')
    print()

import random

random_list =[random.randint(1,100) for i in range(15)]

print(f'original list {random_list}')
print(f'number > 50 = {sorted([x for x in random_list if x > 50 ])}')
print(f'number genap in list : {(sorted([x for x in random_list if x % 2 == 0]))}')
print(f'jumlah angka yang habis di bagi 3 : {len(sorted([x for x in random_list if x % 3 == 0]))}')
print()
print('STATISTIK')
print(f"""
# Angka terbesar = {max(random_list)}
# Angka terkecil = {min(random_list)}
# rata rata = {sum(random_list) / len(random_list)}
# List terurut = {sorted(random_list)}
# """)


try:
    while True :
        angka1 = int(input('masukan angka pertama :'))

        while True:
            operator = input('masukan operator = ')

            if operator == '=':
                print(f'result {angka1} ')
                break
            angka2 = int(input('masukan angka selanjutnya :'))

            if operator == '+':
                angka1 += angka2
            elif operator == '-':
                angka1 -= angka2
            elif operator == '*':
                angka1 *= angka2
            elif operator == '/':
                if angka2 != 0:
                    angka1 /= angka2
            else:
                raise ValueError('operator tidak valid')
                

        lanjutan = input('ingin menghitung lagi (ya/no) :')
        if lanjutan == 'no':
            break
except ValueError:
    raise ValueError('input harus berupa number(int)')
except ZeroDivisionError:
    raise ZeroDivisionError('input pembagian tidak bole 0')

import random
random_number = random.randint(1,10)
list_tebakan = []

for i in range(10):
    tebakan_random = int(input(f'masukan tebakan random : tebakan ke-{i} :'))
    list_tebakan.append(tebakan_random)
    
    if tebakan_random == random_number:
        print(f'jawaban kamu {tebakan_random} benar!')
        break
    elif tebakan_random > random_number :
        print(f'tebakan ke {i+1 } ')
        print('tebakan terlalu besar!')
    elif tebakan_random < random_number:
        print(f'tebakan ke {i+1 }')
        print('tebakan terlalu kecil!')

print(f'history tebakan {list_tebakan}')
data = f'jumlah tebakan = {len(list_tebakan)}'
print(data)
score = 0
if len(list_tebakan) <= 3 :
    print('skor kamu 90')
elif len(list_tebakan) > 3 :
    print('skor kamu 75')
elif len(list_tebakan) >= 7 :
    print('skor kamu 50')


db_mahasiswa =  {}

def tambah_mahasiswa(nim,nama,semester,gpa):
        if nim in db_mahasiswa:
            print('tidak bisa menambahkan nim yang sudah ada')
        else:
            db_mahasiswa[nim] = (nama,semester,gpa)
        print(f'✓ {nim} - {nama} (Semester {semester}, GPA {gpa}) ditambahkan')
def tampilkan_mahasiswa(nim,db):
    nama , semester , gpa = db[nim]
    return f'NIM: {nim} | Nama: {nama}  | Semester: {semester}  | GPA: {gpa}'
    
def update_gpa(nim,gpa_baru,db):
     nama,semester , gpa = db[nim]
     db[nim] = (nama,semester,gpa_baru)
     print(f'nama {nama}  dengan gpa lama {gpa} berhasil di update menjadi {gpa_baru}')

def hapus_data_gpa_min(nim,db):
     del db[nim]

def cari_mahasiswa_gpa_min(min_gpa,db):
     for nim, data in db.items():
        nama , semester , gpa = data
        print(data)
        print(f'nama {nama} memiliki gpa di atas {min_gpa} yaitu {gpa}')

def statistik_gpa(db):
    gpas = [data[2] for data in db.values()]
    avg = sum(gpas) / len(gpas)
    max_gpa = max(gpas)
    min_gpa = min(gpas)

    print(f"Rata-rata GPA: {avg}")
    print(f"GPA Tertinggi: {max_gpa}")
    print(f"GPA Terendah: {min_gpa}")

print("=== DATABASE MAHASISWA === \n")

print("Menambah mahasiswa...")
tambah_mahasiswa("001", "Andi", 3, 3.75)
tambah_mahasiswa("002", "Bella", 2, 3.50)
tambah_mahasiswa("003", "Citra", 4, 3.90)
tambah_mahasiswa("004", "Doni", 1, 3.25)
tambah_mahasiswa("005", "Eka", 3, 3.80)

print("\n=== DATA MAHASISWA ===")
print(tampilkan_mahasiswa("001", db_mahasiswa))
print(tampilkan_mahasiswa("002", db_mahasiswa))
print(tampilkan_mahasiswa("003", db_mahasiswa))
print(tampilkan_mahasiswa("004", db_mahasiswa))
print(tampilkan_mahasiswa("005", db_mahasiswa))

print("\n=== STATISTIK GPA ===")
statistik_gpa(db_mahasiswa)

print("\n=== MAHASISWA DENGAN GPA >= 3.70 ===")
cari_mahasiswa_gpa_min(3.70, db_mahasiswa)

print("\n=== UPDATE GPA ===")
update_gpa("001", 3.80, db_mahasiswa)


with open ('data_penjualan_csv', 'w') as file:
    while True:
        produk = input('masukan nama produk anda :')
        harga = int(input('masukan harga produk anda :'))
        jumlah = int(input('masukan jumlah produk :'))
        total = harga * jumlah
        file.write((f'{produk}, {harga}, {jumlah}, {total}\n'))
        print(f'produk : {produk} berhasil di input')
        lanjutan = input('ingin menambahkan produk lagi? (ya/no) :')
        if lanjutan == 'no' :
            break

for i in range(1,6):
    print(i ,end= '')
    print('.',end=' ' )
    for j in range(6):
        print('[X]', '[ ]', end=' ')
    print()



harga = [50000, 75000, 75000, 100000, 100000]

kursi = [
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "]
]

kolom = ["A", "B", "C", "D", "E", "F", "G", "H"]

pesanan = []
total = 0

print("=== SISTEM PEMESANAN TIKET BIOSKOP ===")

while True:
    print("\nPETA KURSI (5 Baris x 8 Kolom):")
    print("  ", end="")
    for k in kolom:
        print(f"{k:^3}", end=" ")
    print()

    for i in range(5):
        print(i + 1, end=" ")
        for j in range(8):
            print(f"[{kursi[i][j]}]", end=" ")
        print(f" Rp {harga[i]:,}".replace(",", "."))

    print("\nPesan kursi (format: 1A, 2B, dll) atau 'selesai' untuk keluar")
    pilih = input("Pilih kursi: ").upper()

    if pilih == "SELESAI":
        break

    if len(pilih) < 2:
        print("Input tidak valid!")
        continue

    baris = int(pilih[0]) - 1
    kol = ord(pilih[1]) - ord("A")

    if not (0 <= baris < 5 and 0 <= kol < 8):
        print("Kursi tidak ada!")
        continue

    if kursi[baris][kol] == "X":
        print("Kursi sudah terisi!")
    else:
        kursi[baris][kol] = "X"
        pesanan.append(pilih)
        total += harga[baris]
        print(f"✓ {pilih} berhasil dipesan (Rp {harga[baris]:,})".replace(",", "."))

print("\nRINGKASAN PEMESANAN:")
print("Kursi yang dipesan:", ", ".join(pesanan))
print(f"Total Harga: Rp {total:,}".replace(",", "."))

lanjut = input("\nLanjutkan pemesanan? (y/n): ").lower()

if lanjut == "n":
    print("Terima kasih telah menggunakan sistem kami!")



def bunga_majemuk(principal,rate,time, n=1):
    r = rate / 100
    A = principal * (1 + r/n)**(n*time)
    bunga_total = A * principal
    return A , bunga_total

def validasi_input(principal,rate,time):
    if principal <= 0 :
        return False, 'modal awal tidak bisa 0'
    if rate <= 0 :
        return False, 'bunga awal tidak bisa 0'
    if time <= 0 :
        return False, 'jangka waktu harus lebih dari 0'
    else:
        return True , 'validasi input approved'
    
def generate_laporan(nama,principal,final_amount,bunga):
    roi = (bunga / principal) * 100
    laporan = f"""
=== {nama.upper()} ===
Principal: Rp {principal:,.0f}
Jumlah Akhir: Rp {final_amount:,.0f}
Keuntungan Bunga: Rp {bunga:,.0f}
ROI: {roi:.2f}%
"""
    return laporan

def banding_investasi(principal,rate,time):
    hasil_dict = {}
    max_amount = 0
    terbaik = None

    for p in principal:
        akhir , bunga = bunga_majemuk(p,rate,time)
        hasil_dict[p] = (akhir,bunga)
        if akhir > max_amount:
            max_amount = akhir
            terbaik = p
    return hasil_dict , terbaik

def menu():
    print(f'== SELAMAT DATANG DI INVESTASI ==')
    nama = input('masukan nama anda :')
    principal = float(input('masukan modal awal :'))
    rate = float(input(' masukan jumlah suku bunga (%) :'))
    time = float(input('masukan jangka waktu  investasi :'))

    is_validasi, error = validasi_input(principal,rate,time)
    if not is_validasi:
        print(is_validasi, error)
        return
    else:
        print(is_validasi, error)
    
    print('== ANALISI INVESTASI ==')
    akhir , bunga = bunga_majemuk(principal,rate,time)
    print(generate_laporan(nama,principal,akhir,bunga))

    print('perbandingan investasi')
    number_list =  [100_000_000, 150_000_000, 200_000_000]
    hasil , terbaik = banding_investasi(number_list,rate,time)
    for p, (bunga, akhir) in hasil.items():
        print(generate_laporan(f'investasi Rp{p:,}',p,akhir,bunga))

    print(f'investasi terbaik adalah Rp {terbaik:,} dengan jumlah akhir Rp{hasil[terbaik][0]:,.0f}')

if __name__ == '__main__':
    menu()


    
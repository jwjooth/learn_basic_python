# UJIAN AKHIR SEMESTER
## Python Dasar - Final Assessment

**Instruktur:** Prof. Claude AI  
**Tanggal Ujian:** Semester 1, 2024  
**Durasi:** Unlimited  
**Sifat Ujian:** Tertutup (No Copy-Paste)  
**Metode Pengumpulan:** Buat file `.py` untuk setiap soal  

---

## PERATURAN UJIAN

1. **Tuliskan jawaban Anda dalam bentuk file Python (.py)** dengan nama sesuai soal
2. **Kode harus dapat dijalankan tanpa error** dan memberikan output yang sesuai dengan requirement
3. **Jangan gunakan library eksternal** kecuali yang sudah dipelajari di course (built-in Python saja)
4. **Beri komentar pada kode Anda** untuk menjelaskan logic yang kompleks
5. **Test kode Anda terlebih dahulu** sebelum dikumpulkan
6. **Ketentuan Kelulusan:** Minimal 70/100 untuk lanjut ke course berikutnya

---

## BAGIAN 1: SOAL MUDAH (5 Soal × 5 Poin = 25 Poin)

### **Soal 1: Konversi Suhu**
Buat program yang mengkonversi suhu dari Celsius ke Fahrenheit.

**Requirement:**
- Terima input suhu dalam Celsius dari user
- Rumus konversi: `F = (C × 9/5) + 32`
- Tampilkan hasil dengan format: `"{celsius}°C sama dengan {fahrenheit}°F"`
- Hasil harus menampilkan 2 angka desimal

**Input Contoh:**
```
Masukkan suhu dalam Celsius: 25
```

**Output Contoh:**
```
25.0°C sama dengan 77.00°F
```

**File:** `soal_1_konversi_suhu.py`

---

### **Soal 2: Validasi Bilangan Genap dan Ganjil**
Buat program yang menerima 5 angka dari user dan tentukan mana yang genap dan ganjil.

**Requirement:**
- Minta user memasukkan 5 angka (satu per satu)
- Tentukan setiap angka apakah GENAP atau GANJIL
- Hitung berapa jumlah angka GENAP dan berapa GANJIL
- Tampilkan hasil dalam format terstruktur

**Input Contoh:**
```
Masukkan angka ke-1: 10
Masukkan angka ke-2: 7
Masukkan angka ke-3: 24
Masukkan angka ke-4: 15
Masukkan angka ke-5: 8
```

**Output Contoh:**
```
Hasil Analisis:
10 adalah GENAP
7 adalah GANJIL
24 adalah GENAP
15 adalah GANJIL
8 adalah GENAP

Total Genap: 3
Total Ganjil: 2
```

**File:** `soal_2_genap_ganjil.py`

---

### **Soal 3: Hitung Rata-Rata Nilai**
Buat program untuk menghitung rata-rata nilai siswa dan menentukan grade.

**Requirement:**
- Terima input nama siswa dan 3 nilai ujian
- Hitung rata-rata dari ketiga nilai tersebut
- Tentukan grade berdasarkan kriteria:
  - `>= 85`: Grade A
  - `>= 75 dan < 85`: Grade B
  - `>= 65 dan < 75`: Grade C
  - `< 65`: Grade D
- Tampilkan hasil dalam format yang jelas

**Input Contoh:**
```
Nama Siswa: Budi
Nilai Ujian 1: 85
Nilai Ujian 2: 90
Nilai Ujian 3: 88
```

**Output Contoh:**
```
=== HASIL UJIAN ===
Nama: Budi
Nilai Ujian 1: 85
Nilai Ujian 2: 90
Nilai Ujian 3: 88
Rata-rata: 87.67
Grade: A
```

**File:** `soal_3_hitung_grade.py`

---

### **Soal 4: Manipulasi String Dasar**
Buat program yang melakukan manipulasi string sebagai berikut.

**Requirement:**
- Terima input sebuah kalimat dari user
- Hitung jumlah karakter (termasuk spasi)
- Hitung jumlah kata
- Tampilkan kalimat dengan format:
  - UPPERCASE
  - lowercase
  - Title Case
- Cari posisi kemunculan pertama kata "Python" (jika ada)

**Input Contoh:**
```
Masukkan kalimat: Saya sedang belajar Python
```

**Output Contoh:**
```
Kalimat Original: Saya sedang belajar Python
Jumlah Karakter: 25
Jumlah Kata: 5
UPPERCASE: SAYA SEDANG BELAJAR PYTHON
lowercase: saya sedang belajar python
Title Case: Saya Sedang Belajar Python
Posisi "Python": Ditemukan di index 21
```

**File:** `soal_4_manipulasi_string.py`

---

### **Soal 5: Operasi List Dasar**
Buat program untuk memanipulasi list dengan operasi-operasi dasar.

**Requirement:**
- Buat list berisi 5 angka
- Tampilkan list original
- Tambahkan 3 angka baru di akhir menggunakan `append()`
- Sisipkan 1 angka di posisi index 2
- Hapus angka di posisi index 4
- Tampilkan list final dan jumlah elemen dalam list

**Input Contoh (Hard-coded dalam kode):**
```python
numbers = [10, 20, 30, 40, 50]
```

**Output Contoh:**
```
List Original: [10, 20, 30, 40, 50]

Setelah menambah 60, 70, 80:
[10, 20, 30, 40, 50, 60, 70, 80]

Setelah insert 25 di index 2:
[10, 20, 25, 30, 40, 50, 60, 70, 80]

Setelah hapus index 4:
[10, 20, 25, 30, 50, 60, 70, 80]

Total elemen: 8
```

**File:** `soal_5_operasi_list.py`

---

## BAGIAN 2: SOAL MEDIUM (5 Soal × 15 Poin = 75 Poin)

### **Soal 6: Fungsi Faktorial dengan Validasi**
Buat program dengan function untuk menghitung faktorial dengan validasi input.

**Requirement:**
- Buat function `hitung_faktorial(n)` yang menerima parameter angka
- Validasi: n harus angka positif dan bilangan bulat
- Jika validasi gagal, return -1 dan tampilkan pesan error
- Hitung faktorial menggunakan loop
- Di main program, minta input user dan tampilkan hasilnya
- Hitung faktorial untuk 3 angka sekaligus

**Input Contoh:**
```
Masukkan angka ke-1: 5
Masukkan angka ke-2: 0
Masukkan angka ke-3: 10
```

**Output Contoh:**
```
Faktorial dari 5 adalah: 120
Faktorial dari 0 adalah: 1
Faktorial dari 10 adalah: 3628800

Total hitungan: 3 angka telah diproses
```

**Catatan:**
- `0! = 1` (konvensi matematika)
- `5! = 5 × 4 × 3 × 2 × 1 = 120`

**File:** `soal_6_faktorial.py`

---

### **Soal 7: Dictionary untuk Data Karyawan**
Buat program manajemen data karyawan menggunakan dictionary.

**Requirement:**
- Buat function `tambah_karyawan(nama, divisi, gaji)` yang menambah data ke dictionary
- Buat function `tampilkan_semua_karyawan(data)` yang menampilkan semua data
- Buat function `cari_karyawan(nama, data)` yang mencari data karyawan berdasarkan nama
- Buat function `update_gaji(nama, gaji_baru, data)` yang mengupdate gaji
- Buat function `hapus_karyawan(nama, data)` yang menghapus data karyawan
- Main program: demonstrasikan semua function di atas dengan minimal 3 karyawan

**Output Contoh:**
```
=== SISTEM MANAJEMEN KARYAWAN ===

Menambah data karyawan...
✓ Budi (Divisi IT, Gaji: Rp 8.000.000) ditambahkan
✓ Siti (Divisi HR, Gaji: Rp 6.500.000) ditambahkan
✓ Ahmad (Divisi Sales, Gaji: Rp 7.000.000) ditambahkan

=== SEMUA KARYAWAN ===
1. Budi - IT - Rp 8.000.000
2. Siti - HR - Rp 6.500.000
3. Ahmad - Sales - Rp 7.000.000

=== CARI KARYAWAN ===
Cari: Budi
Ditemukan! Budi bekerja di IT dengan gaji Rp 8.000.000

=== UPDATE GAJI ===
Update gaji Budi menjadi Rp 9.000.000
✓ Gaji Budi berhasil diupdate

=== HAPUS KARYAWAN ===
Hapus Ahmad
✓ Ahmad berhasil dihapus dari sistem
```

**File:** `soal_7_data_karyawan.py`

---

### **Soal 8: Loop Bersarang - Pola Bintang**
Buat program yang menampilkan pola menggunakan nested loop.

**Requirement:**
- Minta input user untuk jumlah baris (n)
- Buat pola bintang yang membentuk segitiga sama sisi
- Setiap baris i menampilkan i bintang
- Buat versi kedua: pola terbalik (segitiga terbalik)
- Validasi input harus angka positif antara 1-10

**Input Contoh:**
```
Masukkan jumlah baris: 5
```

**Output Contoh:**
```
=== POLA SEGITIGA ===
*
**
***
****
*****

=== POLA SEGITIGA TERBALIK ===
*****
****
***
**
*
```

**File:** `soal_8_pola_bintang.py`

---

### **Soal 9: List Comprehension dan Filter**
Buat program untuk mengolah list menggunakan berbagai teknik.

**Requirement:**
- Buat list berisi 15 angka random (1-100)
- Tampilkan list original
- Filter hanya angka yang > 50 menggunakan list comprehension
- Filter hanya angka genap menggunakan loop
- Hitung berapa jumlah angka yang habis dibagi 3
- Tampilkan statistik: angka terbesar, terkecil, dan rata-rata
- Urutkan list dari terkecil ke terbesar

**Output Contoh:**
```
List Original: [45, 78, 23, 92, 56, 34, 89, 12, 67, 88, 41, 95, 27, 73, 18]

Angka > 50: [78, 92, 56, 89, 67, 88, 95, 73]

Angka Genap: [78, 92, 56, 34, 12, 88, 28, 18]

Jumlah angka habis dibagi 3: 4

Statistik:
- Angka Terbesar: 95
- Angka Terkecil: 12
- Rata-rata: 57.27

List Terurut: [12, 18, 23, 27, 34, 41, 45, 56, 67, 73, 78, 88, 89, 92, 95]
```

**File:** `soal_9_list_comprehension.py`

---

### **Soal 10: Try-Except untuk Input User**
Buat program untuk menangani berbagai jenis error dengan try-except.

**Requirement:**
- Minta user memasukkan 2 angka (dengan konversi int)
- Minta user memilih operasi: + (tambah), - (kurang), * (kali), / (bagi)
- Tangani error:
  - `ValueError`: jika input bukan angka
  - `ZeroDivisionError`: jika pembagian dengan 0
  - Operasi tidak valid: tampilkan pesan error custom
- Gunakan try-except-else-finally
- Tampilkan hasil jika berhasil

**Input Contoh:**
```
Masukkan angka 1: 10
Masukkan angka 2: 0
Pilih operasi (+, -, *, /): /
```

**Output Contoh (Scenario 1 - Success):**
```
10 + 5 = 15
--- Operasi selesai dengan sukses ---
```

**Output Contoh (Scenario 2 - Error):**
```
ERROR: Pembagian dengan 0 tidak diperbolehkan!
--- Operasi selesai ---
```

**File:** `soal_10_error_handling.py`

---

## BAGIAN 3: SOAL SULIT (5 Soal × 15 Poin = 75 Poin)

### **Soal 11: Permainan Tebak Angka (Guessing Game)**
Buat permainan tebak angka dengan fitur-fitur advanced.

**Requirement:**
- Program membuat angka random antara 1-100
- User bisa menebak sampai 10 kali
- Setiap kali menebak, berikan hint:
  - Jika tebakan < angka: "Terlalu kecil!"
  - Jika tebakan > angka: "Terlalu besar!"
  - Jika tebakan == angka: "BENAR!"
- Hitung skor berdasarkan jumlah tebakan:
  - 1-3 tebakan: Skor 100
  - 4-6 tebakan: Skor 75
  - 7-10 tebakan: Skor 50
  - Lebih dari 10: Skor 0
- Tampilkan history semua tebakan user
- Tanyakan apakah user ingin bermain lagi
- Hitung statistik total permainan

**Output Contoh:**
```
=== PERMAINAN TEBAK ANGKA ===
Saya sudah memikirkan sebuah angka antara 1-100.
Anda punya 10 kesempatan untuk menebaknya!

Tebakan ke-1: 50
Terlalu besar!

Tebakan ke-2: 25
Terlalu kecil!

Tebakan ke-3: 37
Terlalu kecil!

Tebakan ke-4: 43
BENAR! Angka yang saya pikir adalah 43

History Tebakan: [50, 25, 37, 43]
Jumlah Tebakan: 4
Skor Anda: 75

Mainkan lagi? (y/n): n
--- Game Over ---
```

**File:** `soal_11_tebak_angka.py`

---

### **Soal 12: Tuple dan Dictionary - Database Mahasiswa**
Buat sistem database mahasiswa dengan tuple dan dictionary.

**Requirement:**
- Gunakan tuple untuk menyimpan data mahasiswa (nim, nama, semester, gpa)
- Gunakan dictionary untuk koleksi mahasiswa dengan NIM sebagai key
- Buat function:
  - `tambah_mahasiswa(nim, nama, semester, gpa, db)`: Tambah data
  - `tampilkan_mahasiswa(nim, db)`: Tampilkan 1 mahasiswa
  - `update_gpa(nim, gpa_baru, db)`: Update GPA mahasiswa
  - `hapus_mahasiswa(nim, db)`: Hapus mahasiswa
  - `cari_mahasiswa_gpa_min(min_gpa, db)`: Cari mahasiswa dengan GPA >= min_gpa
  - `statistik_gpa(db)`: Hitung rata-rata GPA, GPA tertinggi, terendah
- Main program: demonstrasikan dengan minimal 5 mahasiswa
- Gunakan try-except untuk validasi data

**Output Contoh:**
```
=== DATABASE MAHASISWA ===

Menambah mahasiswa...
✓ 001 - Andi (Semester 3, GPA 3.75) ditambahkan
✓ 002 - Bella (Semester 2, GPA 3.50) ditambahkan
✓ 003 - Citra (Semester 4, GPA 3.90) ditambahkan
✓ 004 - Doni (Semester 1, GPA 3.25) ditambahkan
✓ 005 - Eka (Semester 3, GPA 3.80) ditambahkan

=== DATA MAHASISWA ===
NIM: 001 | Nama: Andi | Semester: 3 | GPA: 3.75
NIM: 002 | Nama: Bella | Semester: 2 | GPA: 3.50
NIM: 003 | Nama: Citra | Semester: 4 | GPA: 3.90
NIM: 004 | Nama: Doni | Semester: 1 | GPA: 3.25
NIM: 005 | Nama: Eka | Semester: 3 | GPA: 3.80

=== STATISTIK GPA ===
Rata-rata GPA: 3.64
GPA Tertinggi: 3.90 (Citra)
GPA Terendah: 3.25 (Doni)

=== MAHASISWA DENGAN GPA >= 3.70 ===
001 - Andi: 3.75
003 - Citra: 3.90
005 - Eka: 3.80

=== UPDATE GPA ===
NIM 002 - GPA diupdate dari 3.50 menjadi 3.65
✓ GPA Bella berhasil diupdate
```

**File:** `soal_12_database_mahasiswa.py`

---

### **Soal 13: File I/O - Baca dan Proses Data CSV**
Buat program untuk membaca dan memproses file data CSV.

**Requirement:**
- Buat file `data_penjualan.csv` dengan struktur:
  ```
  Produk,Harga,Jumlah,Total
  Laptop,8000000,2,16000000
  Mouse,150000,10,1500000
  Keyboard,500000,5,2500000
  Monitor,2000000,3,6000000
  ```
- Baca file CSV menggunakan file I/O biasa (bukan library csv)
- Hitung:
  - Total penjualan keseluruhan
  - Produk dengan penjualan tertinggi
  - Produk dengan penjualan terendah
  - Rata-rata penjualan per produk
- Buat file output `laporan_penjualan.txt` dengan format terstruktur
- Gunakan try-except untuk error handling

**Output di Console:**
```
=== LAPORAN PENJUALAN ===

DATA PENJUALAN:
Produk: Laptop | Harga: 8000000 | Jumlah: 2 | Total: 16000000
Produk: Mouse | Harga: 150000 | Jumlah: 10 | Total: 1500000
Produk: Keyboard | Harga: 500000 | Jumlah: 5 | Total: 2500000
Produk: Monitor | Harga: 2000000 | Jumlah: 3 | Total: 6000000

ANALISIS:
Total Penjualan: Rp 26.500.000
Produk Tertinggi: Laptop (Rp 16.000.000)
Produk Terendah: Mouse (Rp 1.500.000)
Rata-rata per Produk: Rp 6.625.000

✓ Laporan tersimpan di laporan_penjualan.txt
```

**File yang dibuat:** `soal_13_file_io.py` + `data_penjualan.csv` (dibuat oleh program)

---

### **Soal 14: Nested Loop - Sistem Pemesanan Tiket**
Buat sistem pemesanan tiket bioskop dengan berbagai kondisi.

**Requirement:**
- Buat representasi kursi bioskop (5 baris × 8 kolom)
- Kursi dinyatakan dengan: `[ ]` (kosong), `[X]` (terisi)
- Fitur program:
  - Tampilkan peta kursi dengan nomor baris (1-5) dan kolom (A-H)
  - User memilih kursi (input: 1A, 2C, dll)
  - Validasi: kursi harus kosong dan posisi valid
  - Hitung harga berdasarkan baris:
    - Baris 1: Rp 50.000
    - Baris 2-3: Rp 75.000
    - Baris 4-5: Rp 100.000
  - User bisa memesan multiple kursi
  - Tampilkan total harga
  - Opsi untuk membatalkan pemesanan
- Gunakan nested loop untuk menampilkan peta kursi

**Output Contoh:**
```
=== SISTEM PEMESANAN TIKET BIOSKOP ===

PETA KURSI (5 Baris × 8 Kolom):
   A   B   C   D   E   F   G   H
1  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  Rp 50.000
2  [ ] [X] [ ] [ ] [ ] [ ] [X] [ ]  Rp 75.000
3  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  Rp 75.000
4  [X] [ ] [X] [ ] [ ] [ ] [ ] [ ]  Rp 100.000
5  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [X]  Rp 100.000

Pesan kursi (format: 1A, 2B, dll) atau 'selesai' untuk keluar
Pilih kursi: 1A
✓ 1A berhasil dipesan (Rp 50.000)

Pilih kursi: 2A
✓ 2A berhasil dipesan (Rp 75.000)

Pilih kursi: selesai

RINGKASAN PEMESANAN:
Kursi yang dipesan: 1A, 2A
Total Harga: Rp 125.000

Lanjutkan pemesanan? (y/n): n
Terima kasih telah menggunakan sistem kami!
```

**File:** `soal_14_pemesanan_tiket.py`

---

### **Soal 15: Function dengan Multiple Return & Logic Kompleks - Sistem Kalkulator Investasi**
Buat program kalkulator investasi dengan logika perhitungan kompleks.

**Requirement:**
- Function `hitung_bunga_majemuk(principal, rate, time, n)` yang menghitung bunga majemuk
  - Formula: `A = P(1 + r/n)^(nt)`
  - Return: tuple (jumlah_akhir, bunga_total)
- Function `validasi_input(principal, rate, time)` yang return tuple (is_valid, pesan_error)
- Function `banding_investasi(principals, rate, time)` yang:
  - Menerima list principal yang berbeda
  - Hitung bunga majemuk untuk masing-masing
  - Return: tuple (hasil_dict, investasi_terbaik)
- Function `generate_laporan(nama_investasi, principal, final_amount, bunga)` yang:
  - Generate string laporan terformat
  - Return: string laporan
- Main program:
  - Minta input user (modal awal, suku bunga tahunan, waktu investasi dalam tahun)
  - Bandingkan dengan pilihan investasi standar (100jt, 150jt, 200jt)
  - Tampilkan hasil lengkap dengan analisis

**Output Contoh:**
```
=== KALKULATOR INVESTASI ===

Masukkan jumlah investasi awal (Rp): 100000000
Masukkan suku bunga tahunan (%): 8
Masukkan jangka waktu investasi (tahun): 5

ANALISIS INVESTASI ANDA:
Principal: Rp 100.000.000
Suku Bunga: 8% per tahun
Jangka Waktu: 5 tahun

Jumlah Akhir: Rp 146.933.280
Keuntungan Bunga: Rp 46.933.280
ROI: 46.93%

=== PERBANDINGAN INVESTASI STANDAR ===

Investasi 100 Juta:
Principal: Rp 100.000.000
Jumlah Akhir: Rp 146.933.280
Keuntungan: Rp 46.933.280

Investasi 150 Juta:
Principal: Rp 150.000.000
Jumlah Akhir: Rp 220.399.920
Keuntungan: Rp 70.399.920

Investasi 200 Juta:
Principal: Rp 200.000.000
Jumlah Akhir: Rp 293.866.560
Keuntungan: Rp 93.866.560

REKOMENDASI: Investasi 200 Juta memberikan keuntungan terbesar
```

**File:** `soal_15_kalkulator_investasi.py`

---

## KRITERIA PENILAIAN

### **Aspek yang Dinilai:**

1. **Correctness (40%)**
   - Output sesuai requirement
   - Logic program benar
   - Menangani edge cases

2. **Code Quality (30%)**
   - Clean code dan readable
   - Proper naming convention
   - Penggunaan function yang efektif
   - Penggunaan struktur data yang tepat

3. **Error Handling (15%)**
   - Validasi input user
   - Try-except yang tepat
   - Pesan error yang jelas

4. **Documentation (15%)**
   - Komentar yang jelas
   - Docstring di function
   - Readable output format

### **Rubric Penilaian:**

| Skor | Kriteria |
|------|----------|
| 5 | Sempurna - semua requirement terpenuhi, code berkualitas tinggi |
| 4 | Baik - hampir semua requirement terpenuhi, sedikit issue |
| 3 | Cukup - sebagian besar requirement terpenuhi, beberapa issue |
| 2 | Kurang - requirement kurang terpenuhi, banyak issue |
| 1 | Sangat Kurang - requirement tidak terpenuhi |

---

## PANDUAN PENGUMPULAN

### **Struktur Folder:**
```
UJIAN_PYTHON_DASAR/
├── soal_1_konversi_suhu.py
├── soal_2_genap_ganjil.py
├── soal_3_hitung_grade.py
├── soal_4_manipulasi_string.py
├── soal_5_operasi_list.py
├── soal_6_faktorial.py
├── soal_7_data_karyawan.py
├── soal_8_pola_bintang.py
├── soal_9_list_comprehension.py
├── soal_10_error_handling.py
├── soal_11_tebak_angka.py
├── soal_12_database_mahasiswa.py
├── soal_13_file_io.py
├── soal_13_data_penjualan.csv (auto generated)
├── soal_14_pemesanan_tiket.py
└── soal_15_kalkulator_investasi.py
```

### **Checklist Sebelum Pengumpulan:**
- [ ] Semua file `.py` sudah dibuat
- [ ] Semua kode dapat dijalankan tanpa error
- [ ] Output sesuai requirement
- [ ] Ada komentar pada logic kompleks
- [ ] Tidak ada hardcoding yang tidak perlu
- [ ] Input validation sudah diterapkan
- [ ] File sudah di-test sebelum dikumpulkan

---

## TIPS MENGERJAKAN

1. **Jangan terburu-buru:** Pahami setiap requirement dengan baik sebelum coding
2. **Test incrementally:** Test setiap bagian sebelum menggabungkan
3. **Gunakan function:** Pisahkan logic ke dalam function yang reusable
4. **Handling error:** Antisipasi kemungkinan error dari input user
5. **Baca requirement berkali-kali:** Pastikan tidak ada yang terlewat
6. **Output yang jelas:** Format output agar mudah dibaca
7. **Jangan copy-paste:** Pahami setiap baris kode yang Anda tulis

---

## SCORING SUMMARY

| Bagian | Jumlah Soal | Poin per Soal | Total Poin |
|--------|-------------|---------------|-----------|
| Mudah | 5 | 5 | 25 |
| Medium | 5 | 15 | 75 |
| Sulit | 5 | 15 | 75 |
| **TOTAL** | **15** | **-** | **175** |

**Konversi ke Nilai 100:**
- Skor ÷ 1.75 = Nilai Akhir

| Skor Total | Nilai Akhir | Grade |
|-----------|-------------|-------|
| 157-175 | 90-100 | A |
| 140-156 | 80-89 | B |
| 122-139 | 70-79 | C |
| < 122 | < 70 | D (TIDAK LULUS) |

---

## CATATAN PENTING

⚠️ **Peserta yang memperoleh nilai < 70 HARUS melakukan remedial dan mengulang soal-soal yang gagal sebelum lanjut ke course berikutnya.**

✅ **Peserta yang memperoleh nilai >= 70 DIIZINKAN lanjut ke Python Intermediate / Course berikutnya.**

---

**Good Luck! 🚀**

*Semoga Anda telah menguasai semua konsep dasar Python dengan baik. Jika masih ada yang kurang, jangan ragu untuk review materi sebelum mengerjakan soal.*

---

**Tanggal Terakhir Dikumpulkan:** -  
**Dosen Pengampu:** Prof. Claude AI  
**Semester:** 1 / 2024

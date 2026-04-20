# 🐍 Python Basics untuk Machine Learning
### Seri Latihan — Gaya HackerRank

> **Bahasa:** Python 3.10+
> **Format:** Setiap soal memiliki spesifikasi input/output yang eksak, constraints, dan contoh test case.
> **Aturan:** Implementasi murni Python — dilarang menggunakan `numpy`, `pandas`, `scikit-learn`, atau library eksternal apapun kecuali yang disebutkan secara eksplisit.

---

## 🟢 EASY (5 Soal)

---

### E-1 — Statistik Dasar Dataset

**Deskripsi:**
Dalam ML, langkah pertama exploratory data analysis (EDA) adalah menghitung statistik dasar dari sebuah dataset. Buat fungsi-fungsi berikut **tanpa menggunakan library apapun**.

**Fungsi yang harus dibuat:**

```python
def mean(data: list[float]) -> float: ...
def median(data: list[float]) -> float: ...
def mode(data: list[float]) -> float: ...
def variance(data: list[float]) -> float: ...
def std_dev(data: list[float]) -> float: ...
def data_range(data: list[float]) -> float: ...
```

**Spesifikasi:**
- `mean`: rata-rata aritmatika
- `median`: nilai tengah setelah diurutkan. Jika n genap, ambil rata-rata dua nilai tengah.
- `mode`: nilai yang paling sering muncul. Jika ada tie, kembalikan nilai **terkecil**.
- `variance`: variansi **populasi** → `sum((x - mean)²) / n`
- `std_dev`: akar dari variance populasi
- `data_range`: `max - min`

Semua fungsi harus raise `ValueError("Data tidak boleh kosong")` jika input list kosong.

**Format Input (stdin):**
```
Baris 1: angka-angka dipisah spasi
```

**Format Output (stdout):**
```
Mean    : {nilai}
Median  : {nilai}
Mode    : {nilai}
Variance: {nilai}
Std Dev : {nilai}
Range   : {nilai}
```

**Contoh Input:**
```
4 1 2 2 3 5
```

**Contoh Output:**
```
Mean    : 2.8333
Median  : 2.5
Mode    : 2
Variance: 1.8056
Std Dev : 1.3437
Range   : 4
```

**Test Cases:**

| Input | mean | median | mode | variance | std_dev | range |
|-------|------|--------|------|----------|---------|-------|
| `1 2 3 4 5` | `3.0` | `3.0` | `1` | `2.0` | `1.4142` | `4` |
| `2 2 2 2` | `2.0` | `2.0` | `2` | `0.0` | `0.0` | `0` |
| `1 1 2 2 3` | `1.8` | `2.0` | `1` | `0.56` | `0.7483` | `2` |

**Constraints:**
- Semua nilai input adalah bilangan bulat
- `1 ≤ len(data) ≤ 10000`
- Output float dibulatkan **4 desimal**. Jika nilai bulat, tampilkan tanpa desimal (contoh: `3.0` → `3.0`, bukan `3`)

---

### E-2 — Normalisasi dan Standarisasi

**Deskripsi:**
Dua teknik scaling paling umum di ML adalah **Min-Max Normalization** dan **Z-Score Standardization**. Implementasikan keduanya sebagai fungsi.

**Fungsi yang harus dibuat:**

```python
def min_max_normalize(data: list[float]) -> list[float]: ...
def z_score_standardize(data: list[float]) -> list[float]: ...
def describe_scaling(data: list[float]) -> dict: ...
```

**Spesifikasi:**
- `min_max_normalize`: kembalikan list baru di mana setiap nilai `x` diubah menjadi `(x - min) / (max - min)`. Raise `ValueError("Semua nilai sama, tidak bisa dinormalisasi")` jika `max == min`.
- `z_score_standardize`: kembalikan list baru di mana setiap nilai `x` diubah menjadi `(x - mean) / std`. Raise `ValueError("Standar deviasi = 0, tidak bisa distandarisasi")` jika `std == 0`.
- `describe_scaling`: kembalikan dict dengan key `"original_min"`, `"original_max"`, `"original_mean"`, `"original_std"`, `"normalized_min"`, `"normalized_max"`, `"standardized_mean"`, `"standardized_std"` — semua nilai float dibulatkan 4 desimal.

**Format Input (stdin):**
```
Baris 1: angka-angka dipisah spasi
Baris 2: nama operasi ("normalize", "standardize", atau "describe")
```

**Format Output:**
- Jika `normalize` atau `standardize`: cetak hasil list, setiap nilai dipisah spasi, dibulatkan 4 desimal
- Jika `describe`: cetak setiap key-value satu per baris, format `key: value`

**Contoh Input:**
```
1 2 3 4 5
normalize
```

**Contoh Output:**
```
0.0 0.25 0.5 0.75 1.0
```

**Test Cases:**

| Input | Operasi | Output |
|-------|---------|--------|
| `0 5 10` | normalize | `0.0 0.5 1.0` |
| `2 4 6` | standardize | `-1.2247 0.0 1.2247` |
| `3 3 3` | normalize | `ValueError: Semua nilai sama, tidak bisa dinormalisasi` |
| `3 3 3` | standardize | `ValueError: Standar deviasi = 0, tidak bisa distandarisasi` |

**Constraints:**
- `1 ≤ len(data) ≤ 10000`
- Output float dibulatkan 4 desimal

---

### E-3 — Manipulasi Matrix dengan List of Lists

**Deskripsi:**
Matrix adalah struktur data dasar dalam ML (bobot neural network, dataset, dll). Implementasikan operasi matrix dasar menggunakan list of lists **tanpa numpy**.

**Fungsi yang harus dibuat:**

```python
def matrix_add(A: list[list[float]], B: list[list[float]]) -> list[list[float]]: ...
def matrix_multiply(A: list[list[float]], B: list[list[float]]) -> list[list[float]]: ...
def transpose(A: list[list[float]]) -> list[list[float]]: ...
def matrix_scalar_multiply(A: list[list[float]], scalar: float) -> list[list[float]]: ...
```

**Spesifikasi:**
- `matrix_add`: penjumlahan element-wise. Raise `ValueError("Ukuran matrix tidak sama")` jika dimensi berbeda.
- `matrix_multiply`: perkalian matrix standar (dot product baris × kolom). Raise `ValueError("Dimensi tidak kompatibel untuk perkalian")` jika kolom A ≠ baris B.
- `transpose`: balik baris dan kolom.
- `matrix_scalar_multiply`: kalikan setiap elemen dengan scalar.

**Format Input (stdin):**
```
Baris 1: operasi ("add", "multiply", "transpose", "scalar_mul")
Baris 2: dimensi matrix A → "baris kolom"
Baris 3...: isi matrix A, satu baris per baris matrix
Baris selanjutnya: dimensi matrix B (jika dibutuhkan), isinya
Baris terakhir: nilai scalar (hanya untuk scalar_mul)
```

**Contoh Input (multiply):**
```
multiply
2 3
1 2 3
4 5 6
3 2
7 8
9 10
11 12
```

**Contoh Output:**
```
58 64
139 154
```

**Contoh Input (transpose):**
```
transpose
2 3
1 2 3
4 5 6
```

**Contoh Output:**
```
1 4
2 5
3 6
```

**Test Cases:**

| Operasi | A | B/scalar | Output |
|---------|---|----------|--------|
| add | `[[1,2],[3,4]]` | `[[5,6],[7,8]]` | `[[6,8],[10,12]]` |
| transpose | `[[1,2,3]]` | — | `[[1],[2],[3]]` |
| scalar_mul | `[[1,2],[3,4]]` | `2` | `[[2,4],[6,8]]` |
| multiply | `[[1,2]]` (1×2) | `[[1],[2]]` (2×1) | `[[5]]` |

**Constraints:**
- Nilai elemen matrix adalah integer
- Dimensi matrix: baris dan kolom masing-masing antara 1 dan 50
- Output: setiap baris matrix dicetak dalam satu baris, nilai dipisah spasi

---

### E-4 — Fungsi Aktivasi Neural Network

**Deskripsi:**
Fungsi aktivasi adalah komponen penting dalam neural network. Implementasikan fungsi aktivasi yang paling umum digunakan.

**Fungsi yang harus dibuat:**

```python
import math

def sigmoid(x: float) -> float: ...
def relu(x: float) -> float: ...
def tanh(x: float) -> float: ...
def softmax(x: list[float]) -> list[float]: ...
def leaky_relu(x: float, alpha: float = 0.01) -> float: ...

def apply_activation(data: list[float], activation: str, **kwargs) -> list[float]: ...
```

**Spesifikasi:**
- `sigmoid(x)`: `1 / (1 + e^(-x))`
- `relu(x)`: `max(0, x)`
- `tanh(x)`: `(e^x - e^(-x)) / (e^x + e^(-x))` — gunakan `math.tanh` diperbolehkan
- `softmax(x)`: `e^(x_i) / sum(e^(x_j))` untuk setiap elemen. Untuk stabilitas numerik, kurangi setiap elemen dengan `max(x)` sebelum eksponen.
- `leaky_relu(x, alpha)`: `x` jika `x > 0`, else `alpha * x`
- `apply_activation(data, activation, **kwargs)`: terapkan fungsi aktivasi ke seluruh list. `activation` bisa `"sigmoid"`, `"relu"`, `"tanh"`, `"leaky_relu"`. Raise `ValueError("Aktivasi '{activation}' tidak dikenal")` jika tidak valid. Untuk `softmax`, gunakan langsung fungsi `softmax(data)`.

**Format Input (stdin):**
```
Baris 1: nama aktivasi
Baris 2: angka-angka dipisah spasi
Baris 3 (opsional): nilai alpha (hanya untuk leaky_relu)
```

**Contoh Input:**
```
sigmoid
0 1 -1 2
```

**Contoh Output:**
```
0.5 0.7311 0.2689 0.8808
```

**Test Cases:**

| Aktivasi | Input | Output |
|----------|-------|--------|
| relu | `-2 -1 0 1 2` | `0 0 0 1 2` |
| softmax | `1 2 3` | `0.0900 0.2447 0.6652` |
| leaky_relu (alpha=0.01) | `-10 0 10` | `-0.1 0.0 10.0` |
| tanh | `0` | `0.0` |
| unknown | `1 2` | `ValueError: Aktivasi 'unknown' tidak dikenal` |

**Constraints:**
- `x` bisa berupa angka float atau integer apapun
- Output float dibulatkan 4 desimal
- `softmax`: jumlah output harus = 1.0 (dalam toleransi floating point)
- `alpha` pada leaky_relu selalu > 0

---

### E-5 — Encoding Fitur Kategorikal

**Deskripsi:**
Sebelum memasukkan data kategorikal ke model ML, data harus diubah ke format numerik. Implementasikan dua teknik encoding yang paling umum.

**Fungsi yang harus dibuat:**

```python
def label_encode(data: list[str]) -> tuple[list[int], dict]: ...
def one_hot_encode(data: list[str]) -> tuple[list[list[int]], list[str]]: ...
def decode_label(encoded: list[int], mapping: dict) -> list[str]: ...
```

**Spesifikasi:**
- `label_encode(data)`: ubah setiap label unik ke integer mulai dari 0, diurutkan **alphabetically**. Kembalikan `(encoded_list, mapping_dict)` di mana `mapping_dict` seperti `{"cat": 0, "dog": 1}`.
- `one_hot_encode(data)`: kembalikan `(matrix, categories)` di mana `matrix` adalah list of lists berisi 0/1, dan `categories` adalah list label unik yang sudah diurutkan alphabetically. Setiap baris mewakili satu sampel.
- `decode_label(encoded, mapping)`: kembalikan label asli dari list integer dan mapping. Raise `ValueError("Index {i} tidak ada di mapping")` jika ada integer yang tidak valid.

**Format Input (stdin):**
```
Baris 1: label-label dipisah spasi
Baris 2: operasi ("label", "onehot")
```

**Format Output:**
- `label`: cetak encoded list dipisah spasi, lalu mapping (satu per baris, format `label: index`)
- `onehot`: cetak header kategori (dipisah spasi), lalu setiap baris matrix

**Contoh Input:**
```
cat dog bird cat dog
label
```

**Contoh Output:**
```
1 2 0 1 2
bird: 0
cat: 1
dog: 2
```

**Contoh Input:**
```
cat dog bird
onehot
```

**Contoh Output:**
```
bird cat dog
0 1 0
0 0 1
1 0 0
```

**Test Cases:**

| Input | Operasi | encoded | categories |
|-------|---------|---------|------------|
| `yes no yes` | label | `1 0 1` | `no: 0, yes: 1` |
| `a b c` | onehot | matrix 3×3 identity | `a b c` |
| `x x x` | label | `0 0 0` | `x: 0` |

**Constraints:**
- Label hanya mengandung huruf kecil
- `1 ≤ len(data) ≤ 1000`
- Jumlah kategori unik: 2 sampai 20

---

## 🟡 MEDIUM (5 Soal)

---

### M-1 — Implementasi K-Fold Cross Validation

**Deskripsi:**
Cross-validation adalah teknik untuk mengevaluasi model secara robust. Implementasikan K-Fold Cross Validation dari nol.

**Fungsi yang harus dibuat:**

```python
def k_fold_split(n: int, k: int) -> list[tuple[list[int], list[int]]]: ...
def cross_val_accuracy(
    X: list[list[float]],
    y: list[int],
    k: int,
    predictor_fn  # callable: fit_predict(X_train, y_train, X_val) -> list[int]
) -> dict: ...
```

**Spesifikasi:**

`k_fold_split(n, k)`:
- Bagi index `0` sampai `n-1` menjadi `k` fold secara **sequential** (berurutan, tidak shuffle)
- Kembalikan list of `k` tuple: `(train_indices, val_indices)`
- Fold ke-i: `val = index [i*fold_size : (i+1)*fold_size]`, `train = sisanya`
- Jika `n` tidak habis dibagi `k`, `k-1` fold pertama berukuran `floor(n/k)` dan fold terakhir mendapat sisa
- Raise `ValueError("k harus antara 2 dan n")` jika `k < 2` atau `k > n`

`cross_val_accuracy(X, y, k, predictor_fn)`:
- Jalankan k_fold_split lalu untuk setiap fold:
  - Buat `X_train, y_train, X_val, y_val` dari indices
  - Panggil `predictor_fn(X_train, y_train, X_val)` → `y_pred`
  - Hitung akurasi fold: `sum(pred == true) / len(val)`
- Kembalikan dict: `{"scores": [f1, f2, ...], "mean": float, "std": float, "min": float, "max": float}` — semua float dibulatkan 4 desimal

**Format Input (stdin):**
```
Baris 1: n k
```

**Format Output untuk `k_fold_split`:**
```
Fold 1: train=[...] val=[...]
Fold 2: train=[...] val=[...]
...
```

**Contoh Input:**
```
10 3
```

**Contoh Output:**
```
Fold 1: train=[3, 4, 5, 6, 7, 8, 9] val=[0, 1, 2]
Fold 2: train=[0, 1, 2, 6, 7, 8, 9] val=[3, 4, 5]
Fold 3: train=[0, 1, 2, 3, 4, 5] val=[6, 7, 8, 9]
```

**Test Cases:**

| n | k | ukuran setiap val fold |
|---|---|----------------------|
| 10 | 5 | `[2,2,2,2,2]` |
| 9 | 4 | `[2,2,2,3]` |
| 6 | 2 | `[3,3]` |
| 5 | 6 | `ValueError: k harus antara 2 dan n` |

**Constraints:**
- `2 ≤ k ≤ n`
- Setiap index hanya muncul **tepat satu kali** di val set seluruh fold
- Gabungan semua val indices = `list(range(n))`

---

### M-2 — Kalkulasi Loss Functions

**Deskripsi:**
Loss function mengukur seberapa jauh prediksi model dari nilai aktual. Implementasikan loss functions yang paling umum digunakan.

**Fungsi yang harus dibuat:**

```python
def mse(y_true: list[float], y_pred: list[float]) -> float: ...
def rmse(y_true: list[float], y_pred: list[float]) -> float: ...
def mae(y_true: list[float], y_pred: list[float]) -> float: ...
def r2_score(y_true: list[float], y_pred: list[float]) -> float: ...
def binary_cross_entropy(y_true: list[int], y_pred: list[float]) -> float: ...
def categorical_cross_entropy(y_true: list[list[int]], y_pred: list[list[float]]) -> float: ...
```

**Spesifikasi:**
- `mse`: `sum((y_true - y_pred)²) / n`
- `rmse`: `sqrt(mse)`
- `mae`: `sum(|y_true - y_pred|) / n`
- `r2_score`: `1 - SS_res/SS_tot` di mana `SS_res = sum((y_true - y_pred)²)`, `SS_tot = sum((y_true - mean(y_true))²)`
- `binary_cross_entropy`: `- sum(y * log(p) + (1-y) * log(1-p)) / n`. Gunakan clipping: `p = max(min(p, 1-1e-15), 1e-15)` untuk menghindari `log(0)`.
- `categorical_cross_entropy`: `- sum(sum(y_ij * log(p_ij))) / n`. Gunakan clipping yang sama. `y_true` adalah one-hot encoded.

Semua fungsi raise `ValueError("Panjang y_true dan y_pred harus sama")` jika panjang berbeda.

**Format Input (stdin):**
```
Baris 1: nama loss function
Baris 2: y_true dipisah spasi
Baris 3: y_pred dipisah spasi
```

**Contoh Input:**
```
mse
1 2 3 4 5
1.1 1.9 3.2 3.8 5.1
```

**Contoh Output:**
```
0.0220
```

**Test Cases:**

| Loss | y_true | y_pred | Output |
|------|--------|--------|--------|
| mse | `[1,2,3]` | `[1,2,3]` | `0.0` |
| mae | `[0,1,2]` | `[1,2,3]` | `1.0` |
| r2_score | `[1,2,3,4,5]` | `[1,2,3,4,5]` | `1.0` |
| r2_score | `[1,2,3]` | `[2,2,2]` | `0.0` |
| binary_cross_entropy | `[1,0,1]` | `[0.9,0.1,0.8]` | `0.1643` |

**Constraints:**
- `y_pred` untuk binary/categorical CE selalu dalam rentang `(0, 1)`
- `y_true` untuk binary CE hanya berisi 0 atau 1
- Output dibulatkan 4 desimal
- `r2_score` bisa bernilai negatif (jika prediksi lebih buruk dari baseline mean)

---

### M-3 — String Processing untuk NLP Dasar

**Deskripsi:**
Sebelum text bisa diproses model ML, teks harus melalui tahap preprocessing. Implementasikan pipeline preprocessing teks dasar.

**Fungsi yang harus dibuat:**

```python
def clean_text(text: str) -> str: ...
def tokenize(text: str) -> list[str]: ...
def remove_stopwords(tokens: list[str], stopwords: list[str]) -> list[str]: ...
def build_vocabulary(corpus: list[str]) -> dict: ...
def bag_of_words(text: str, vocabulary: dict) -> list[int]: ...
def tf_idf_score(term: str, document: str, corpus: list[str]) -> float: ...
```

**Spesifikasi:**
- `clean_text(text)`: ubah ke lowercase, hapus semua karakter selain huruf, angka, dan spasi. Hapus spasi berlebih (multiple spaces → single space). Strip spasi di awal/akhir.
- `tokenize(text)`: panggil `clean_text` lalu split berdasarkan spasi. Kembalikan list token.
- `remove_stopwords(tokens, stopwords)`: hapus token yang ada di `stopwords` (case-insensitive).
- `build_vocabulary(corpus)`: terima list dokumen (string), kembalikan dict `{word: index}` di mana setiap kata unik diberi index mulai dari 0, **diurutkan alphabetically**.
- `bag_of_words(text, vocabulary)`: kembalikan list integer sepanjang `len(vocabulary)`, setiap posisi = jumlah kemunculan kata tersebut di `text`.
- `tf_idf_score(term, document, corpus)`:
  - TF = `count(term in document) / total_words_in_document`
  - IDF = `log(total_documents / (1 + documents_containing_term))` (gunakan `math.log`)
  - Return `TF * IDF`, dibulatkan 4 desimal

**Format Input (stdin):**
```
Baris 1: operasi
Baris 2+: data sesuai operasi
```

**Contoh Input (bag_of_words):**
```
bow
the cat sat
the cat sat on the mat
```
*(baris 2: teks input, baris 3: seluruh corpus untuk build vocabulary)*

**Contoh Output:**
```
0 0 1 1 0 1 2
```
*(vocabulary: cat=0, mat=1, on=2, sat=3, the=4 → tapi output sesuai index alphabetical)*

**Test Cases:**

| Fungsi | Input | Output |
|--------|-------|--------|
| clean_text | `"Hello, World!! 123"` | `"hello world 123"` |
| tokenize | `"The CAT sat."` | `["the", "cat", "sat"]` |
| remove_stopwords | `["the","cat","sat"]`, sw=`["the"]` | `["cat","sat"]` |
| build_vocabulary | `["cat sat", "cat ran"]` | `{"cat":0,"ran":1,"sat":2}` |
| tf_idf (term="cat", doc="cat sat", corpus=["cat sat","dog ran"]) | — | `0.0` (karena log(2/(1+2)) < 0 jika semua dok mengandung "cat") |

**Constraints:**
- Teks input hanya mengandung ASCII
- `corpus` untuk `build_vocabulary` minimal 1 dokumen
- Stopwords sudah dalam huruf kecil

---

### M-4 — Implementasi Gradient Descent 1D

**Deskripsi:**
Gradient descent adalah algoritma optimasi inti di balik pelatihan model ML. Implementasikan gradient descent untuk meminimalkan fungsi sederhana.

**Fungsi yang harus dibuat:**

```python
def gradient_descent(
    func,           # callable: f(x) -> float
    grad_func,      # callable: f'(x) -> float
    x_init: float,
    learning_rate: float,
    epochs: int,
    tolerance: float = 1e-6
) -> dict: ...

def numerical_gradient(func, x: float, h: float = 1e-5) -> float: ...
```

**Spesifikasi:**

`gradient_descent`:
- Mulai dari `x = x_init`
- Setiap epoch: `x = x - learning_rate * grad_func(x)`
- Berhenti lebih awal jika `|x_baru - x_lama| < tolerance`
- Kembalikan dict: `{"x_optimal": float, "f_optimal": float, "epochs_run": int, "converged": bool, "history": list[float]}` di mana `history` adalah list nilai `x` setiap epoch (panjang = `epochs_run`)
- Raise `ValueError("learning_rate harus positif")` jika `learning_rate <= 0`
- Raise `ValueError("epochs harus positif")` jika `epochs < 1`

`numerical_gradient(func, x, h)`:
- Hitung gradient secara numerik: `(f(x + h) - f(x - h)) / (2 * h)`

**Format Input (stdin):**
```
Baris 1: nama fungsi preset ("quadratic", "cubic", "absolute")
Baris 2: x_init learning_rate epochs
```

Fungsi preset yang harus didefinisikan di dalam program:
- `"quadratic"`: `f(x) = x²`, `f'(x) = 2x` → minimum di `x=0`
- `"cubic"`: `f(x) = x³ - 3x`, `f'(x) = 3x² - 3` → minimum lokal di `x=1`
- `"absolute"`: `f(x) = |x|`, gradient = `numerical_gradient`

**Contoh Input:**
```
quadratic
2.0 0.1 100
```

**Contoh Output:**
```
x_optimal : 0.0000
f_optimal : 0.0000
epochs_run: 87
converged : True
```

**Test Cases:**

| Fungsi | x_init | lr | epochs | x_optimal (±0.001) | converged |
|--------|--------|-----|--------|---------------------|-----------|
| quadratic | `4.0` | `0.1` | `1000` | `0.0` | `True` |
| quadratic | `1.0` | `2.0` | `100` | divergen (x sangat besar) | `False` |
| cubic | `2.0` | `0.01` | `10000` | `1.0` | `True` |

**Constraints:**
- `history` hanya menyimpan nilai `x` (bukan nilai fungsi)
- Jika tidak konvergen dalam `epochs` langkah, `converged = False`
- Output float dibulatkan 4 desimal

---

### M-5 — Analisis Dataset dengan Dictionary dan List Comprehension

**Deskripsi:**
Data analyst dan ML engineer sering bekerja dengan dataset berbentuk list of dictionaries. Implementasikan fungsi analisis dataset tanpa library eksternal.

**Format dataset:** List of dict, contoh:
```python
[
  {"id": 1, "age": 25, "salary": 50000, "dept": "IT", "label": 1},
  {"id": 2, "age": 30, "salary": 60000, "dept": "HR", "label": 0},
  ...
]
```

**Fungsi yang harus dibuat:**

```python
def filter_by(dataset: list[dict], field: str, value) -> list[dict]: ...
def select_columns(dataset: list[dict], columns: list[str]) -> list[dict]: ...
def group_by(dataset: list[dict], field: str) -> dict: ...
def compute_stats_per_group(dataset: list[dict], group_field: str, value_field: str) -> dict: ...
def normalize_column(dataset: list[dict], column: str) -> list[dict]: ...
def missing_value_report(dataset: list[dict]) -> dict: ...
```

**Spesifikasi:**
- `filter_by`: kembalikan list dict di mana `row[field] == value`. Raise `KeyError("Field '{field}' tidak ada")` jika field tidak ada di row manapun.
- `select_columns`: kembalikan list dict hanya dengan key yang ada di `columns`. Raise `KeyError("Column '{col}' tidak ditemukan")` jika salah satu column tidak ada.
- `group_by`: kembalikan `{nilai_field: [list_row]}`.
- `compute_stats_per_group`: untuk setiap grup, hitung `{"mean": float, "min": float, "max": float, "count": int}` dari `value_field`.
- `normalize_column`: kembalikan dataset baru (tidak modifikasi in-place) di mana nilai kolom tersebut sudah dinormalisasi min-max. Nilai kolom harus numerik.
- `missing_value_report`: kembalikan `{field: jumlah_None}` untuk setiap field yang memiliki minimal 1 nilai `None`.

**Format Input (stdin):**
```
Baris 1: jumlah baris dataset (n)
Baris 2..n+1: data dalam format CSV (header di baris 2)
Baris n+2: operasi
Baris n+3: argumen operasi
```

**Contoh Input:**
```
4
id,age,dept,label
1,25,IT,1
2,30,HR,0
3,28,IT,1
4,35,HR,0
group_by
dept
```

**Contoh Output:**
```
IT: 2 records
HR: 2 records
```

**Test Cases:**

| Operasi | Input | Output |
|---------|-------|--------|
| filter_by dept=IT | dataset di atas | 2 rows dengan dept IT |
| compute_stats age per dept | — | IT: mean=26.5, HR: mean=32.5 |
| normalize_column age | — | age ternormalisasi 0.0–1.0 |

**Constraints:**
- Semua field yang dioperasikan selalu ada di dataset (kecuali untuk test error cases)
- Dataset selalu memiliki minimal 1 baris
- `normalize_column` tidak mengubah dataset asli (kembalikan copy)

---

## 🔴 HARD (5 Soal)

---

### H-1 — Implementasi Naive Bayes Classifier dari Scratch

**Deskripsi:**
Implementasikan **Gaussian Naive Bayes Classifier** dari nol untuk klasifikasi multi-kelas.

**Fungsi/class yang harus dibuat:**

```python
import math

def gaussian_pdf(x: float, mean: float, std: float) -> float: ...

def naive_bayes_fit(
    X: list[list[float]],
    y: list[int]
) -> dict: ...

def naive_bayes_predict(
    X_test: list[list[float]],
    model: dict
) -> list[int]: ...

def naive_bayes_predict_proba(
    X_test: list[list[float]],
    model: dict
) -> list[dict]: ...
```

**Spesifikasi:**

`gaussian_pdf(x, mean, std)`:
- Hitung PDF Gaussian: `(1 / (std * sqrt(2π))) * e^(-(x-mean)² / (2*std²))`
- Jika `std == 0`, kembalikan `1.0` jika `x == mean`, else `0.0`

`naive_bayes_fit(X, y)`:
- Kembalikan `model` berupa dict dengan struktur:
  ```python
  {
    "classes": [kelas_unik_sorted],
    "priors": {kelas: P(kelas)},
    "means": {kelas: [mean_per_fitur]},
    "stds": {kelas: [std_per_fitur]}  # std populasi
  }
  ```

`naive_bayes_predict(X_test, model)`:
- Untuk setiap sampel, hitung log posterior setiap kelas:
  `log P(kelas) + sum(log(gaussian_pdf(x_j, mean_j, std_j)))`
- Prediksi = kelas dengan log posterior tertinggi
- Jika ada tie, pilih kelas dengan nilai integer **terkecil**

`naive_bayes_predict_proba`:
- Kembalikan list of dict `{kelas: probabilitas}` untuk setiap sampel
- Konversi log scores ke probabilitas: `exp(score) / sum(exp(score))` (softmax dari log scores)
- Probabilitas dibulatkan 4 desimal

**Format Input (stdin):**
```
Baris 1: n_train n_features
Baris 2..n_train+1: fitur dipisah spasi, label di kolom terakhir
Baris n_train+2: n_test
Baris n_train+3..akhir: fitur test dipisah spasi
```

**Contoh Input:**
```
6 2
1.0 2.0 0
1.5 1.8 0
2.0 3.0 0
5.0 6.0 1
5.5 5.8 1
6.0 6.2 1
2
1.2 2.1
5.2 5.9
```

**Contoh Output:**
```
0
1
```

**Test Cases:**

| Skenario | X_train | y_train | X_test | Expected predict |
|----------|---------|---------|--------|-----------------|
| Linearly separable | kelas 0: fitur ~[1,2], kelas 1: fitur ~[5,6] | — | `[[1,2],[5,6]]` | `[0,1]` |
| 3 kelas | kelas 0,1,2 masing-masing 10 sampel | — | sampel dari masing-masing kelas | label kelas yang benar |

**Constraints:**
- Kelas adalah integer non-negatif
- Semua fitur adalah float
- `n_features ≥ 1`, `n_samples ≥ 2`
- Setiap kelas minimal memiliki 1 sampel training
- Output probabilitas dibulatkan 4 desimal

---

### H-2 — Implementasi Algoritma Sorting untuk Data Ranking

**Deskripsi:**
Dalam ML, sorting digunakan untuk ranking prediksi, mencari nearest neighbor, dan menghitung metrik seperti AUC-ROC. Implementasikan sorting dan ranking dari nol.

**Fungsi yang harus dibuat:**

```python
def merge_sort(data: list, key=None, reverse=False) -> list: ...
def quicksort(data: list, key=None, reverse=False) -> list: ...
def argsort(data: list, reverse=False) -> list[int]: ...
def rank_data(data: list[float], method: str = "average") -> list[float]: ...
def compute_auc_roc(y_true: list[int], y_scores: list[float]) -> float: ...
```

**Spesifikasi:**
- `merge_sort` dan `quicksort`: implementasi dari nol, support `key` function dan `reverse`. Kembalikan list baru (tidak modifikasi in-place).
- `argsort`: kembalikan list index yang akan mengurutkan data dari kecil ke besar. Contoh: `argsort([3,1,2])` → `[1,2,0]`.
- `rank_data(data, method)`:
  - `"average"`: rank tie diberi rata-rata rank
  - `"min"`: rank tie diberi rank minimum
  - `"max"`: rank tie diberi rank maksimum
  - Rank dimulai dari 1
- `compute_auc_roc`: hitung AUC-ROC menggunakan **metode trapesium**:
  - Urutkan prediksi dari skor tertinggi ke terendah
  - Hitung TPR dan FPR di setiap threshold
  - Gunakan `argsort` yang kamu implementasikan
  - AUC = luas di bawah kurva ROC

**Format Input (stdin):**
```
Baris 1: operasi
Baris 2: data dipisah spasi
Baris 3 (opsional): argumen tambahan
```

**Contoh Input (argsort):**
```
argsort
3.0 1.0 4.0 1.5 2.0
```

**Contoh Output:**
```
1 3 4 0 2
```

**Test Cases:**

| Fungsi | Input | Output |
|--------|-------|--------|
| merge_sort | `[3,1,4,1,5]` | `[1,1,3,4,5]` |
| quicksort reverse | `[3,1,4]` | `[4,3,1]` |
| argsort | `[3,1,2]` | `[1,2,0]` |
| rank_data average | `[3,1,2,1]` | `[4.0,1.5,3.0,1.5]` |
| compute_auc_roc | y_true=`[1,1,0,0]`, scores=`[0.9,0.8,0.3,0.1]` | `1.0` |
| compute_auc_roc | y_true=`[1,0,1,0]`, scores=`[0.5,0.5,0.5,0.5]` | `0.5` |

**Constraints:**
- `merge_sort` dan `quicksort` harus **diimplementasikan sendiri** — dilarang menggunakan `sorted()` atau `list.sort()` di dalamnya
- AUC-ROC dibulatkan 4 desimal
- `rank_data` dimulai dari rank 1

---

### H-3 — Implementasi Backpropagation 1 Hidden Layer

**Deskripsi:**
Implementasikan neural network sederhana dengan **1 hidden layer** menggunakan backpropagation. Ini adalah implementasi dari nol tanpa library apapun.

**Arsitektur:** Input → Hidden (sigmoid) → Output (sigmoid) → Binary Cross-Entropy Loss

**Fungsi yang harus dibuat:**

```python
import math
import random

def init_weights(n_input: int, n_hidden: int, n_output: int, seed: int = 42) -> dict: ...
def forward(X: list[float], weights: dict) -> dict: ...
def backward(X: list[float], y: float, cache: dict, weights: dict, lr: float) -> dict: ...
def train(
    X_train: list[list[float]],
    y_train: list[float],
    n_hidden: int,
    lr: float,
    epochs: int,
    seed: int = 42
) -> tuple[dict, list[float]]: ...
def predict(X_test: list[list[float]], weights: dict) -> list[int]: ...
```

**Spesifikasi:**

`init_weights(n_input, n_hidden, n_output, seed)`:
- Gunakan `random.seed(seed)`, inisialisasi bobot dengan `random.uniform(-1, 1)`
- Kembalikan:
  ```python
  {
    "W1": [[float]*n_input]*n_hidden,   # bobot input→hidden
    "b1": [float]*n_hidden,              # bias hidden
    "W2": [[float]*n_hidden]*n_output,  # bobot hidden→output
    "b2": [float]*n_output               # bias output
  }
  ```

`forward(X, weights)`:
- `z1 = W1 @ X + b1` (perkalian matrix-vector)
- `a1 = sigmoid(z1)`
- `z2 = W2 @ a1 + b2`
- `a2 = sigmoid(z2)`
- Kembalikan cache: `{"z1", "a1", "z2", "a2"}`

`backward(X, y, cache, weights, lr)`:
- Hitung gradients menggunakan chain rule:
  - `dL_da2 = a2 - y`
  - `dL_dz2 = dL_da2 * a2 * (1 - a2)`
  - `dL_dW2 = outer(dL_dz2, a1)` (outer product)
  - `dL_db2 = dL_dz2`
  - `dL_da1 = W2.T @ dL_dz2`
  - `dL_dz1 = dL_da1 * a1 * (1 - a1)`
  - `dL_dW1 = outer(dL_dz1, X)`
  - `dL_db1 = dL_dz1`
- Update weights: `W = W - lr * dW`
- Kembalikan weights yang sudah diupdate

`train`:
- Jalankan SGD (satu sampel per update) dengan loop epochs
- Setiap epoch: iterasi semua sampel, lakukan forward + backward
- Simpan **rata-rata BCE loss per epoch** di `loss_history`
- Kembalikan `(weights, loss_history)`

`predict`:
- Threshold `a2 >= 0.5` → label `1`, else `0`

**Format Input (stdin):**
```
Baris 1: n_samples n_features
Baris 2..n+1: fitur + label (label di kolom terakhir, 0 atau 1)
Baris n+2: n_hidden lr epochs
```

**Contoh Input (XOR problem):**
```
4 2
0 0 0
0 1 1
1 0 1
1 1 0
2 0.1 1000
```

**Contoh Output:**
```
Epoch 100: Loss = 0.6931
Epoch 200: Loss = 0.6920
...
Epoch 1000: Loss = 0.2341
Predictions: [0, 1, 1, 0]
Accuracy: 1.0000
```

**Test Cases:**

| Dataset | n_hidden | lr | epochs | Expected accuracy |
|---------|----------|-----|--------|-------------------|
| XOR (4 sampel) | 4 | 0.5 | 5000 | ≥ 0.75 |
| AND gate (4 sampel) | 2 | 0.1 | 2000 | 1.0 |
| OR gate (4 sampel) | 2 | 0.1 | 2000 | 1.0 |

**Constraints:**
- Implementasikan operasi matrix-vector secara manual (nested loop) — dilarang numpy
- `outer(a, b)` = `[[a_i * b_j for b_j in b] for a_i in a]`
- Matrix transpose dilakukan manual
- Loss dicetak setiap 100 epoch
- Output accuracy dibulatkan 4 desimal

---

### H-4 — Implementasi Logistic Regression dengan Regularisasi

**Deskripsi:**
Implementasikan **Logistic Regression** dengan gradient descent dan dua tipe regularisasi (L1 dan L2) untuk klasifikasi biner.

**Fungsi yang harus dibuat:**

```python
def sigmoid(x: float) -> float: ...

def logistic_regression_fit(
    X: list[list[float]],
    y: list[int],
    lr: float = 0.01,
    epochs: int = 1000,
    regularization: str = "none",   # "none", "l1", "l2"
    lambda_: float = 0.01,
    tolerance: float = 1e-6,
    verbose: bool = False
) -> dict: ...

def logistic_regression_predict(
    X: list[list[float]],
    model: dict,
    threshold: float = 0.5
) -> list[int]: ...

def logistic_regression_predict_proba(
    X: list[list[float]],
    model: dict
) -> list[float]: ...

def compute_decision_boundary(model: dict, x_range: tuple) -> tuple: ...
```

**Spesifikasi:**

`logistic_regression_fit`:
- Inisialisasi `weights = [0.0] * n_features`, `bias = 0.0`
- Setiap epoch, hitung gradient untuk **seluruh dataset** (batch gradient descent):
  - `y_hat = sigmoid(X @ w + b)`
  - `dw = (1/n) * X.T @ (y_hat - y)`
  - `db = (1/n) * sum(y_hat - y)`
  - Regularisasi L2: tambahkan `(lambda_ / n) * w` ke `dw`
  - Regularisasi L1: tambahkan `(lambda_ / n) * sign(w)` ke `dw` (sign: 1 jika positif, -1 jika negatif, 0 jika nol)
- Berhenti jika `max(|delta_w|) < tolerance`
- Kembalikan `{"weights": list, "bias": float, "loss_history": list, "epochs_run": int, "converged": bool}`
- Jika `verbose=True`: cetak `"Epoch {e}: Loss = {loss:.6f}"` setiap 100 epoch

`compute_decision_boundary(model, x_range)`:
- Untuk model 2-fitur: kembalikan `(x_values, y_values)` di mana `y = -(w[0]*x + bias) / w[1]`
- `x_range` adalah tuple `(x_min, x_max)`, buat 100 titik merata di range tersebut
- Raise `ValueError("Decision boundary hanya tersedia untuk model 2 fitur")` jika bukan 2 fitur

**Format Input (stdin):**
```
Baris 1: n_samples n_features
Baris 2..n+1: fitur + label (label terakhir)
Baris n+2: lr epochs regularization lambda_
```

**Contoh Input:**
```
6 2
1.0 2.0 0
1.5 1.8 0
2.0 1.5 0
5.0 6.0 1
5.5 5.8 1
6.0 6.2 1
0.1 500 l2 0.01
```

**Contoh Output:**
```
Converged: True
Epochs run: 312
Final weights: [1.2345, 1.4567]
Final bias: -7.8901
Accuracy: 1.0000
```

**Test Cases:**

| Dataset | Regularisasi | Accuracy (≥) |
|---------|-------------|--------------|
| Linearly separable 2D | none | `1.0` |
| Linearly separable 2D | l2, lambda=0.1 | `1.0` |
| Linearly separable 2D | l1, lambda=0.1 | `1.0` |
| Non-separable | none | `≥ 0.7` |

**Constraints:**
- Semua operasi matrix-vector dilakukan manual
- `sign(0) = 0`
- Loss = binary cross-entropy dengan clipping seperti di soal M-2
- Output float dibulatkan 4 desimal

---

### H-5 — Pipeline Feature Engineering Lengkap

**Deskripsi:**
Buat pipeline feature engineering end-to-end yang menggabungkan semua konsep sebelumnya: cleaning, encoding, scaling, splitting, dan evaluasi.

**Yang harus diimplementasikan:**

```python
def load_csv_string(csv_string: str) -> tuple[list[list], list[str]]: ...
def detect_feature_types(data: list[list], headers: list[str]) -> dict: ...
def handle_missing_values(
    data: list[list],
    headers: list[str],
    strategy: dict  # {column: "mean"|"median"|"mode"|"drop"|"constant:<value>"}
) -> list[list]: ...
def auto_preprocess(
    data: list[list],
    headers: list[str],
    target_column: str,
    scale_numeric: bool = True,
    encode_categorical: bool = True
) -> tuple[list[list[float]], list, list[str]]: ...
def feature_importance_correlation(
    X: list[list[float]],
    y: list[float],
    feature_names: list[str]
) -> list[tuple[str, float]]: ...
```

**Spesifikasi:**

`load_csv_string(csv_string)`:
- Parse string CSV (baris pertama = header), kembalikan `(data, headers)`
- Coba konversi setiap nilai ke float. Jika gagal, biarkan sebagai string. Jika string kosong atau `"NA"` atau `"null"`, ubah menjadi `None`.

`detect_feature_types(data, headers)`:
- Kembalikan dict `{column: type}` di mana type adalah `"numeric"` atau `"categorical"`
- Kolom dianggap numeric jika mayoritas (>50%) nilai non-None bisa direpresentasikan sebagai float

`handle_missing_values(data, headers, strategy)`:
- `"mean"` / `"median"` / `"mode"`: isi dengan statistik kolom tersebut (hanya nilai non-None)
- `"drop"`: hapus seluruh baris yang memiliki None di kolom tersebut
- `"constant:<value>"`: isi dengan value yang diberikan (misal `"constant:0"` → isi dengan 0)
- Kembalikan dataset baru (tidak modifikasi in-place)

`auto_preprocess(data, headers, target_column, ...)`:
- Pisahkan kolom target dari fitur
- Jika `encode_categorical=True`: terapkan label encoding ke kolom kategorikal
- Jika `scale_numeric=True`: terapkan min-max normalization ke kolom numerik
- Kembalikan `(X, y, feature_names)` di mana X adalah list of lists of float

`feature_importance_correlation(X, y, feature_names)`:
- Hitung **Pearson correlation** antara setiap fitur dan target:
  `r = sum((x_i - mean_x)(y_i - mean_y)) / sqrt(sum((x_i - mean_x)²) * sum((y_i - mean_y)²))`
- Kembalikan list of `(feature_name, |r|)` diurutkan dari korelasi **terbesar ke terkecil**
- Jika std = 0 untuk sebuah fitur, korelasi = 0.0

**Format Input (stdin):**
CSV string diberikan langsung, diikuti instruksi operasi.

**Contoh Input:**
```
age,salary,dept,churn
25,50000,IT,0
30,60000,HR,1
28,,IT,0
35,70000,HR,1
22,45000,IT,0
auto_preprocess
churn
```

**Contoh Output:**
```
Feature names: ['age', 'salary_normalized', 'dept_encoded']
X shape: 5 x 3
y: [0, 1, 0, 1, 0]
Missing values in salary: filled with mean (56250.0)
```

**Test Cases:**

| Input CSV | Operasi | Expected |
|-----------|---------|----------|
| 5 baris, 1 missing | handle_missing mean | baris tetap 5, None terganti mean |
| 5 baris, 1 missing | handle_missing drop | baris = 4 |
| mixed numeric+categorical | detect_types | type per kolom benar |
| 2 fitur + target | feature_importance | urutan korelasi descending |

**Constraints:**
- Tidak ada pandas atau library eksternal
- `auto_preprocess` menangani missing values dengan strategi `"mean"` untuk numerik dan `"mode"` untuk kategorikal secara otomatis sebelum encoding/scaling
- Pearson correlation dibulatkan 4 desimal
- Kolom dengan semua nilai None di-drop otomatis di `auto_preprocess`

---

## 📊 Ringkasan

| Bagian | Soal | Topik Utama |
|--------|------|-------------|
| Easy | E-1 | Statistik dasar (mean, median, mode, variance) |
| Easy | E-2 | Normalisasi dan standarisasi data |
| Easy | E-3 | Operasi matrix dengan list of lists |
| Easy | E-4 | Fungsi aktivasi neural network |
| Easy | E-5 | Encoding fitur kategorikal |
| Medium | M-1 | K-Fold cross validation |
| Medium | M-2 | Loss functions (MSE, MAE, BCE, CCE) |
| Medium | M-3 | NLP preprocessing dan Bag-of-Words |
| Medium | M-4 | Gradient descent 1D |
| Medium | M-5 | Analisis dataset dengan dict dan list comprehension |
| Hard | H-1 | Naive Bayes Classifier dari scratch |
| Hard | H-2 | Sorting algorithms + AUC-ROC |
| Hard | H-3 | Backpropagation 1 hidden layer dari scratch |
| Hard | H-4 | Logistic Regression + regularisasi L1/L2 |
| Hard | H-5 | Pipeline feature engineering end-to-end |

**Penilaian:** Setiap soal dinilai berdasarkan test case yang lolos.

| Grade | Soal Lulus |
|-------|-----------|
| A | 13–15 soal |
| B | 10–12 soal |
| C | 7–9 soal |
| < C | ≤ 6 soal |

> **Syarat lulus minimum:** Semua 5 soal Easy harus lulus.
# Laporan Proyek Machine Learning - Sendhy Maula Ammarulloh

## **Domain Proyek**

Beras merupakan kebutuhan pokok yang tidak tergantikan bagi mayoritas masyarakat Indonesia. Fluktuasi harga beras sangat memengaruhi stabilitas ekonomi rumah tangga, terutama di kalangan masyarakat menengah ke bawah. Fenomena kenaikan harga beras yang terjadi di Pasar Rakyat Sumedang, sebagaimana dilaporkan oleh Pemerintah Kabupaten Sumedang, menunjukkan adanya lonjakan harga yang cukup signifikan dalam waktu singkat. Harga beras kelas 1 misalnya, naik dari Rp 16.000 menjadi Rp 17.000 per kilogram hanya dalam kurun waktu satu minggu [1]. Faktor penyebab utamanya adalah kelangkaan gabah yang berdampak langsung pada rantai pasokan beras di pasar.

Secara nasional, tren harga beras memang menunjukkan peningkatan sejak Agustus 2022 hingga awal tahun 2024, berdasarkan laporan Sistem Pemantauan Pasar dan Kebutuhan Pokok (SP2KP) Kementerian Perdagangan. Hal ini terjadi meskipun produksi beras secara global mengalami peningkatan, bahkan mencetak rekor tertinggi 520,8 juta ton pada periode 2021–2022 menurut Food and Agriculture Organization (FAO). Fakta ini menunjukkan bahwa kenaikan harga bukan semata karena pasokan global, melainkan juga dipengaruhi oleh faktor domestik seperti distribusi, cuaca, dan kondisi pertanian lokal [2].

Perubahan harga beras yang terjadi secara dinamis ini berpotensi memberikan dampak signifikan terhadap inflasi dan kesejahteraan masyarakat. Oleh karena itu, diperlukan pendekatan analisis data yang mampu memprediksi harga beras secara akurat dan tepat waktu. Salah satu metode yang sudah terbukti dapat digunakan untuk tujuan ini adalah **Regresi Linear**, sebagaimana diterapkan dalam penelitian sebelumnya oleh Veri Arinal & Muhammad Azhari (2023), yang berhasil memprediksi harga beras dengan tingkat kesalahan (RMSE) sebesar 109.062 menggunakan data dari tahun 2021–2023.

Dengan adanya sistem prediksi harga beras berbasis regresi, baik pemerintah daerah maupun pelaku pasar dapat merencanakan kebijakan atau strategi penanggulangan lebih dini. Solusi ini juga berpotensi meningkatkan efisiensi distribusi dan mencegah kelangkaan akibat panic buying.

---

### **Referensi**
- E. D. Kusnaedi, "Harga Beras di Pasar Rakyat Sumedang Terus Melejit," *sumedangkab.go.id*, Feb. 15, 2024. [Online]. Available: https://sumedangkab.go.id/berita/detail/harga-beras-di-pasar-rakyat-sumedang-terus-melejit
- V. Arinal and M. Azhari, "Penerapan Regresi Linear Untuk Prediksi Harga Beras Di Indonesia," *Jurnal Sains dan Teknologi*, vol. 5, no. 1, pp. 341–346, 2023.

---

## **Business Understanding**

Bagian ini menjelaskan proses klarifikasi masalah dalam proyek prediksi harga beras, yang berfokus pada analisis data historis harga beras di Kabupaten Sumedang dan pengembangan model prediksi untuk mendukung pengambilan keputusan.

---

### **Problem Statements**

1. Harga beras di pasar rakyat Sumedang mengalami fluktuasi yang cukup signifikan dan seringkali tidak terduga, sehingga menyulitkan masyarakat dan pelaku pasar dalam merencanakan pembelian atau penjualan.

2. Belum tersedia sistem berbasis data yang dapat memprediksi harga beras secara akurat dalam jangka pendek, khususnya untuk wilayah Sumedang, sehingga pengambilan keputusan masih bersifat reaktif.

---

### **Goals**

1. Mengidentifikasi dan menganalisis tren harga beras di Kabupaten Sumedang dari data historis untuk memahami pola fluktuasinya.

2. Membangun model prediksi harga beras berbasis regresi untuk memperkirakan harga dalam jangka pendek dengan akurasi yang dapat diukur, guna mendukung pengambilan keputusan yang lebih proaktif.

---

### **Solution Statements**

1. Mengimplementasikan **Regresi Linear** sebagai baseline model untuk memprediksi harga beras menggunakan data historis lokal. Evaluasi akurasi dilakukan menggunakan beberapa metrik evaluasi regresi, yaitu:
   - **Root Mean Squared Error (RMSE)** untuk mengukur rata-rata kesalahan prediksi dalam satuan yang sama dengan data asli,
   - **Mean Absolute Error (MAE)** untuk mengetahui rata-rata besar kesalahan absolut dari prediksi,
   - **Mean Squared Error (MSE)** untuk mengukur rata-rata kuadrat dari kesalahan prediksi, dan
   - **R-squared (R²)** untuk menilai seberapa baik model menjelaskan variasi harga beras dari data historis.

2. Membandingkan hasil Regresi Linear dengan model lain seperti **Decision Tree Regressor** dan **Random Forest Regressor** untuk mengetahui model dengan performa terbaik dalam konteks data harga beras di Kabupaten Sumedang.

---

## **Data Understanding**

Dataset yang digunakan dalam proyek ini bersumber langsung dari **Dinas Koperasi Usaha Kecil Menengah Perdagangan dan Perindustrian Kabupaten Sumedang** dan dapat diakses melalui [GitHub Repository](https://raw.githubusercontent.com/sendhy12/datasetd/refs/heads/main/data_produk_pasar.csv). Dataset ini berfokus pada harga produk beras di pasar-pasar rakyat Sumedang dan memiliki 7630 entri serta 12 kolom. Data ini mencakup periode dari tahun 2022 hingga 2024.

### **Struktur Dataset**

Dataset ini terdiri dari 12 kolom sebagai berikut:

1. **id**: ID unik untuk setiap entri (integer).
2. **satuan**: Informasi satuan produk, namun kolom ini berisi nilai **null** (float).
3. **pasar**: ID pasar tempat produk dijual (integer).
4. **tanggal**: Tanggal pencatatan harga produk (string).
5. **nama_item**: ID produk yang dijual (integer).
6. **keterangan**: Deskripsi atau keterangan tentang produk (string).
7. **harga**: Harga produk per satuan (integer) yang menjadi target prediksi.
8. **jumlah**: Jumlah barang yang tersedia atau terjual (integer).
9. **kebutuhan**: Jumlah kebutuhan barang (integer).
10. **item_barang**: Nama produk (string).
11. **satuan_item**: Satuan produk (string).
12. **nama_pasar**: Nama pasar tempat barang dijual (string).

### **Informasi Tambahan**
- **Jumlah Baris**: 7630 baris data.
- **Jumlah Kolom**: 12 kolom data.
- **Tipe Data**: Kombinasi antara integer, string, dan float.
- **Periode Data**: Data ini mencakup rentang waktu dari tahun 2022 hingga 2024.

### **Target Prediksi**
Kolom **harga** adalah target prediksi untuk model ini, yang merujuk pada harga beras Medium yang diperdagangkan di pasar-pasar Sumedang.

### **Variabel Penting**
Dua variabel yang dianggap paling penting untuk memprediksi harga beras Medium adalah:
- **tanggal**: Tanggal pencatatan harga yang memungkinkan adanya tren musiman atau pola berdasarkan waktu.
- **nama_pasar**: Nama pasar yang dapat memberikan wawasan tentang fluktuasi harga berdasarkan lokasi pasar.

### **Eksplorasi Data dan Visualisasi**
Beberapa visualisasi yang telah dilakukan untuk memahami distribusi data adalah sebagai berikut:
- **Distribusi Harga Beras Medium**: Menganalisis harga beras Medium di seluruh pasar.
- **Frekuensi Nama Pasar**: Menampilkan jumlah data yang tercatat untuk setiap pasar.
- **Distribusi Waktu (Tahun & Bulan)**: Memahami pola fluktuasi harga berdasarkan waktu.
- **Harga vs Bulan**: Menggambarkan bagaimana harga beras berubah sepanjang bulan.
- **Harga vs Nama Pasar**: Memahami variasi harga beras di setiap pasar.
- **Korelasi Antar Fitur Numerik**: Menilai hubungan antara harga, bulan, tahun, dan pasar.

---

## **Data Preparation**

Pada tahap ini, beberapa langkah penting dalam mempersiapkan data untuk pemodelan dilakukan agar data siap digunakan oleh algoritma pembelajaran mesin. Berikut adalah langkah-langkah yang diambil dalam proses persiapan data:

### **1. Pembersihan Data**
- **Menghapus Kolom yang Tidak Terpakai:** Kolom **`satuan`** memiliki banyak nilai yang hilang (missing values) dan tidak berkontribusi terhadap analisis atau prediksi harga beras. Oleh karena itu, kolom ini dihapus dari dataset.
  
- **Menghapus Outlier pada Kolom Harga:** Untuk memastikan bahwa model tidak terpengaruh oleh nilai ekstrem yang tidak wajar, dilakukan proses deteksi dan penghapusan outlier pada kolom **`harga`** menggunakan metode **Interquartile Range (IQR)**. Data yang berada di luar rentang [Q1 - 1.5 * IQR, Q3 + 1.5 * IQR] dianggap sebagai outlier dan dihapus.

  ```python
  Q1 = df['harga'].quantile(0.25)
  Q3 = df['harga'].quantile(0.75)
  IQR = Q3 - Q1
  df = df[~((df['harga'] < (Q1 - 1.5 * IQR)) | (df['harga'] > (Q3 + 1.5 * IQR)))]
  ```

### **2. Transformasi Data**
- **Konversi Kolom Tanggal:** Kolom **`tanggal`** yang awalnya berformat string diubah menjadi format **`datetime`** menggunakan fungsi `pd.to_datetime()`. Setelah itu, elemen waktu diekstrak menjadi dua kolom baru, yaitu **`tahun`** dan **`bulan`**, untuk mempermudah analisis musiman atau tren tahunan.

  ```python
  df['tanggal'] = pd.to_datetime(df['tanggal'])
  df['tahun'] = df['tanggal'].dt.year
  df['bulan'] = df['tanggal'].dt.month
  ```

- **Pengkodean Variabel Kategorikal:** Kolom **`nama_pasar`** yang merupakan variabel kategorikal, dikodekan menggunakan **LabelEncoder**. Hal ini dilakukan untuk mengonversi nama pasar menjadi representasi numerik yang bisa diterima oleh model pembelajaran mesin.

  ```python
  le = LabelEncoder()
  df['pasar_encoded'] = le.fit_transform(df['nama_pasar'])
  ```

### **3. Pemilihan Fitur**
- **Fitur untuk Model:** Dalam proses pemilihan fitur, kolom **`tahun`**, **`bulan`**, dan **`pasar_encoded`** dipilih sebagai fitur input (**X**) untuk memprediksi harga beras. Kolom **`harga`** dipilih sebagai target output (**y**).

  ```python
  X = df[['tahun', 'bulan', 'pasar_encoded']]
  y = df['harga']
  ```

### **4. Normalisasi Data**
- **Normalisasi untuk Regresi Linear:** Karena model regresi linear sensitif terhadap skala data, fitur input dinormalisasi menggunakan **MinMaxScaler** untuk mengubah nilai fitur menjadi rentang [0, 1]. Proses normalisasi ini dilakukan pada data latih (training) dan data uji (testing).

  ```python
  scaler = MinMaxScaler()
  scaler.fit(X_train)
  X_train_scaled = scaler.transform(X_train)
  X_test_scaled = scaler.transform(X_test)
  ```

### **5. Pembagian Data**
- **Split Data:** Data dibagi menjadi data latih (training) dan data uji (testing) dengan perbandingan 80:20 menggunakan fungsi `train_test_split`. Data latih digunakan untuk melatih model, sementara data uji digunakan untuk menguji akurasi model setelah pelatihan.

  ```python
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  ```

  Hasil pembagian data (setelah penghapusan outlier):
  - **Total datasets:** (tergantung jumlah data tersisa setelah outlier dihapus)
  - **Data Latih (Training):** ~80% dari total
  - **Data Uji (Testing):** ~20% dari total

### **6. Visualisasi dan Analisis Awal**
- Visualisasi dan eksplorasi data telah dilakukan pada bagian **Data Understanding**, untuk memahami distribusi harga, hubungan antar fitur, dan pola waktu yang relevan. Visualisasi ini membantu dalam pengambilan keputusan terkait pemilihan fitur dan pemahaman tentang data.

---

## Modeling

Dalam proyek ini, digunakan tiga model regresi untuk memprediksi harga beras Medium berdasarkan data historis dari Kabupaten Sumedang, yaitu:

### Linear Regression
Linear Regression digunakan sebagai baseline model karena sifatnya yang sederhana dan interpretatif. Model ini diasumsikan memiliki hubungan linier antara fitur (tahun, bulan, dan pasar_encoded) dengan target harga. Sebelum pelatihan, fitur dilakukan normalisasi menggunakan `MinMaxScaler`.

**Kelebihan:**
- Mudah diinterpretasikan
- Cepat dilatih

**Kekurangan:**
- Tidak menangkap hubungan non-linier dengan baik

---

### Decision Tree Regressor
Model pohon keputusan digunakan untuk menangkap hubungan non-linear antar fitur. Model ini disetel dengan `max_depth=5` untuk menghindari overfitting.

**Kelebihan:**
- Dapat menangkap hubungan non-linear
- Tidak memerlukan normalisasi

**Kekurangan:**
- Rentan terhadap overfitting jika tidak dikendalikan

---

### Random Forest Regressor
Random Forest, sebagai ensembel dari banyak pohon keputusan, digunakan untuk meningkatkan performa dengan mengurangi variansi. Model ini disetel dengan `n_estimators=100` dan `max_depth=7`.

**Kelebihan:**
- Lebih stabil dan akurat dibanding satu pohon keputusan
- Mengurangi risiko overfitting

**Kekurangan:**
- Interpretasi lebih sulit
- Lebih berat secara komputasi

---

Model terbaik dipilih berdasarkan performa pada metrik evaluasi, seperti dijelaskan di bawah.

---

## Evaluation

### 5.1 Metrik Evaluasi

Model dievaluasi menggunakan empat metrik utama regresi berikut:

- **MAE (Mean Absolute Error)**  
  MAE mengukur rata-rata dari selisih absolut antara nilai aktual dan nilai prediksi. Semakin kecil nilai MAE, semakin akurat model.

  \[
  MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
  \]

- **MSE (Mean Squared Error)**  
  MSE mengukur rata-rata dari kuadrat selisih antara nilai aktual dan prediksi. Metrik ini memberikan penalti yang lebih besar terhadap error yang besar.

  \[
  MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
  \]

- **RMSE (Root Mean Squared Error)**  
  RMSE adalah akar dari MSE. RMSE berguna karena satuannya sama dengan target aslinya (harga), sehingga lebih mudah diinterpretasikan.

  \[
  RMSE = \sqrt{MSE}
  \]

- **R² Score (Koefisien Determinasi)**  
  R² mengukur proporsi variasi dari variabel target yang dapat dijelaskan oleh fitur. Nilai R² berkisar antara 0 hingga 1. Semakin mendekati 1, semakin baik performa model.

  \[
  R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
  \]

### Hasil Evaluasi

Berikut adalah hasil evaluasi dari ketiga model:

| Model              | MAE        | MSE         | RMSE       | R²       |
|-------------------|------------|-------------|------------|----------|
| Linear Regression | 624.22     | 630,262.50  | 793.89     | 0.7024   |
| Decision Tree     | 257.02     | 168,816.39  | 410.87     | 0.9203   |
| Random Forest     | **153.14** | **88,601.36** | **297.66** | **0.9582** |

### Analisis

Model **Random Forest Regressor** menunjukkan performa terbaik di semua metrik, dengan R² sebesar 0.958 yang berarti mampu menjelaskan 95.8% variasi harga. MAE dan RMSE yang rendah menunjukkan prediksi yang konsisten dan akurat. Oleh karena itu, **Random Forest dipilih sebagai model akhir**.

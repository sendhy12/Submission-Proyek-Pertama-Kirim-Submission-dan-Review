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

Dataset yang digunakan dalam proyek ini bersumber langsung dari **Dinas Koperasi Usaha Kecil Menengah Perdagangan dan Perindustrian (DiskopUKMPP) Kabupaten Sumedang**, yang merupakan data internal dan relevan dengan konteks lokal untuk kebutuhan skripsi. Dataset tersebut telah disimpan dan dibagikan melalui repositori GitHub agar mudah diakses dan dikelola:  
🔗 [Link Dataset – GitHub](https://raw.githubusercontent.com/sendhy12/datasetd/refs/heads/main/data_produk_pasar.csv)

Dataset ini berisi **7.630 baris dan 12 kolom**, dengan periode data mencakup **tahun 2022 hingga 2024**. Proyek ini berfokus pada prediksi harga **Beras Medium** berdasarkan data historis pasar lokal.

---

### **Fitur yang Digunakan**

Fitur-fitur utama yang digunakan dalam proyek ini meliputi:

- `tanggal`: Tanggal pencatatan harga, berformat `datetime`. Fitur ini akan diekstrak menjadi dua kolom turunan: `tahun` dan `bulan`.
- `nama_pasar`: Nama pasar tempat data harga dikumpulkan, berformat `object` (kategori).
- `harga`: Harga beras medium per kilogram, berformat `integer`. Ini merupakan **target (label)** yang akan diprediksi dalam model.

Catatan:  
Fitur lain seperti `satuan` memiliki missing value dan tidak relevan terhadap kebutuhan analisis, sehingga dihapus dari dataset.

---

### **Eksplorasi Awal & Visualisasi**

Beberapa langkah eksplorasi data telah dilakukan untuk memahami karakteristik dataset, antara lain:

- **Distribusi Harga Beras Medium:** Untuk mengetahui sebaran harga dan mendeteksi outlier.
- **Frekuensi Nama Pasar:** Untuk mengetahui jumlah observasi per pasar dan kontribusinya terhadap total data.
- **Distribusi Waktu (Tahun & Bulan):** Untuk mengecek kelengkapan data per periode dan potensi pola musiman.
- **Harga vs Bulan:** Untuk mengamati tren harga berdasarkan waktu.
- **Harga vs Nama Pasar:** Untuk melihat variasi harga antar pasar.
- **Korelasi antar Fitur Numerik:** Untuk mengidentifikasi hubungan antara waktu dan harga serta mengevaluasi potensi fitur prediktif lainnya.

---

## Data Preparation

Tahapan persiapan data meliputi:

1. **Filtering**: Hanya mengambil data dengan `item_barang` = "Beras Medium".
2. **Konversi tanggal**: Mengubah kolom `tanggal` ke format datetime lalu mengekstrak `bulan` dan `tahun`.
3. **Drop kolom tidak penting**: Kolom `satuan` dihapus karena mengandung missing values dan tidak relevan.
4. **Handling Outlier**: Outlier pada kolom `harga` dihapus dengan metode IQR (Interquartile Range).
5. **Encoding**: Kolom `nama_pasar` diubah ke angka dengan `LabelEncoder`.

---

## Modeling

Tiga model regresi digunakan:

1. **Linear Regression**  
   - Model baseline sederhana.
   - Tidak menangani relasi non-linear dengan baik.

2. **Decision Tree Regressor**  
   - Menangani hubungan non-linear.
   - Mudah overfitting jika tidak dikontrol.

3. **Random Forest Regressor**  
   - Ensembling Decision Tree untuk performa lebih stabil dan akurat.
   - Cocok untuk dataset dengan noise dan non-linearitas.

**Fitur yang digunakan untuk prediksi**:
- `bulan`
- `tahun`
- `pasar_encoded`

Model dilatih dengan pembagian data 80% training dan 20% testing.

---

## Evaluation

### Metrik Evaluasi:

- **MAE (Mean Absolute Error)**: Rata-rata selisih absolut antara nilai aktual dan prediksi.
- **MSE (Mean Squared Error)**: Rata-rata kuadrat dari selisih.
- **R² Score (Coefficient of Determination)**: Seberapa baik model menjelaskan variansi data.

### Hasil Evaluasi:

| Model                  | MAE   | MSE   | R² Score |
|------------------------|-------|-------|----------|
| Linear Regression      | 456.1 | 371820.3 | 0.48     |
| Decision Tree Regressor | 235.4 | 167243.8 | 0.76     |
| Random Forest Regressor| 196.2 | 122321.5 | **0.83** |

**Kesimpulan**:
Random Forest memberikan performa terbaik dengan R² tertinggi dan error terkecil. Oleh karena itu, dipilih sebagai model akhir untuk prediksi harga *Beras Medium*.
